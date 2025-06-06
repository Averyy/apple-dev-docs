# Synchronizing data during a SharePlay activity

**Framework**: Groupactivities

Send custom messages and data between devices to synchronize content for your activity, and incorporate messages your app receives from other participants.

#### Overview

During a typical activity, you want the content one participant sees on their device to match the content other participants see. To make this happen, share data between devices to keep those devices in sync. For example, a drawing app might share the tool state and coordinate points for pen strokes. You then incorporate that shared data into your app, recreating the content that other participants created on their devices.

When an activity-related session is active, share data among participants using the objects of the Group Activities framework. You can share data with all participants or a subset of participants. For example, a quiz game might share different information with contestants and the people asking the questions. For time-sensitive messages, send small amounts of data using a [`GroupSessionMessenger`](groupsessionmessenger.md) object. When the amount of data is larger and the arrival time is less important, share that data using a [`GroupSessionJournal`](groupsessionjournal.md) object.

> **Note**: The [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation) framework supports the synchronization of movie playback without custom messages. For more information, see [`Supporting Coordinated Media Playback`](https://developer.apple.com/documentation/AVFoundation/supporting-coordinated-media-playback).

##### Define the Messages to Send

During the creation of an activity, think about what information you need to share among participants:

- A drawing app might share the state of the tools and the points for line segments.
- A movie-playback app might share commands to start and stop playback and synchronize the current frame.
- A shopping app might share the ID of the current product page and synchronize items in the shared shopping cart.
- A workout app might share workout stats for each participant and which track to play.

After you identify the information you want to send, design data types to encapsulate the relevant details. You can send the details using a [`Data`](https://developer.apple.com/documentation/Foundation/Data) object, or design your own custom types that adopt the [`Codable`](https://developer.apple.com/documentation/Swift/Codable) protocol. The following example shows a message structure for a drawing activity. Each message incorporates the next point in the line segment and the color of the segment. When someone draws, the app sends one message for each new point it receives. Small messages can include up to 256 kilobytes of data, but keep the total size as small as possible to minimize the time it takes to send and process the data.

```swift
struct PenStrokeMessage: Codable {
    let id: UUID
    let color: Stroke.Color
    let point: CGPoint
}
```

When you need to send photos, videos, audio, or other large data types, encode that information into a type that adopts the [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable) protocol. The [`GroupSessionJournal`](groupsessionjournal.md) object requires this protocol when sending types.

##### Send a Message to One or More Participants

When the person running your app on their device makes activity-related changes, send those changes to other affected participants using a [`GroupSessionMessenger`](groupsessionmessenger.md) object. When you send data, you’re actually sending it from one instance of your app to another instance of your app on a different device. The [`GroupSessionMessenger`](groupsessionmessenger.md) object delivers the data over the network to the part of your app configured to receive that data.

When creating the [`GroupSessionMessenger`](groupsessionmessenger.md) object, determine whether you need reliable or unreliable delivery for messages. Choose [`GroupSessionMessenger.DeliveryMode.reliable`](groupsessionmessenger/deliverymode-swift.enum/reliable.md) messaging for crucial data that all participants must have. With reliable messaging, the system performs additional checks to verify the delivery of messages, and resends them as needed. By contrast, [`GroupSessionMessenger.DeliveryMode.unreliable`](groupsessionmessenger/deliverymode-swift.enum/unreliable.md) messaging is generally faster, and is appropriate when the delivery time is more important than the guarantee of delivery. For example, for a movie-watching activity, you might send the name of the movie using reliable messaging, but send the emoji reactions of participants during the movie using unreliable messaging. All participants need to know which movie to watch, but the emoji reactions are time-critical and less important.

After creating your [`GroupSessionMessenger`](groupsessionmessenger.md) object, send your messages using one of the available methods. The following example sends a custom data type to all members of the group:

```swift
Task {
    try? await messenger.send(PenStrokeMessage(id: stroke.id, 
                color: stroke.color, point: point))
}
```

To send a message to a subset of participants, include the list of participants when calling the send method. The [`GroupSession`](groupsession.md) object maintains a set of [`Participant`](participant.md) structures, each of which identifies a member taking part in the activity. Use the [`UUID`](https://developer.apple.com/documentation/Foundation/UUID) of each participant to differentiate them within your app. For example, a quiz game app randomly chooses a subset of participants to take the quiz and share their unique IDs with the group. The person giving the quiz then sends only the questions to the people taking the quiz, and sends the questions and answers to everyone else. The following example subtracts the current participant from the set of all participants and sends a ready message to that subset of people:

```swift
let everyoneElse = session.activeParticipants.subtracting([session.localParticipant])
            
messenger.send(ReadyStateMessage(ready: true), to: .only(everyoneElse)) { error in
    if let error = error { print("Message failure:", error) }
}
```

##### Receive Messages From Other Participants

Messages targeting the current participant can arrive at any time, so it’s best to use a separate task to listen for them. The [`GroupSessionMessenger`](groupsessionmessenger.md) object delivers messages using an [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence), which makes it easy to receive those messages asynchronously. Respond to incoming messages as quickly as possible by updating your app’s data structures to include the new information.

When configuring your session, define a task to receive incoming messages for your activity. Inside the task, use a `for..in` loop to wait on the messages property of your [`GroupSessionMessenger`](groupsessionmessenger.md) object. Specify which message you want to receive as a parameter to the messages method. For example, the code below shows how to process incoming pen stroke messages. The function returns a tuple for each element, with each tuple containing the incoming message and any related contextual information. The message is the data structure you defined previously. The contextual information is a [`GroupSessionMessenger.MessageContext`](groupsessionmessenger/messagecontext.md) structure with additional details, such as the participant who sent the message.

```swift
var task = Task {
    for await (message, context) in messenger.messages(of: PenStrokeMessage.self) {
        print("Participant ID: \(context.source.id)")
        handle(message)
}
```

Create separate tasks to monitor each distinct message type your activity supports. If you have multiple activities, and each one has multiple messages, this results in multiple separate tasks. However, each task runs only when messages are available.

##### Share Files Among Participants

To share files and other large data objects with participants of an activity, use a [`GroupSessionJournal`](groupsessionjournal.md) object instead of a [`GroupSessionMessenger`](groupsessionmessenger.md). A [`GroupSessionJournal`](groupsessionjournal.md) object lets you associate multiple data objects or files with the activity as attachments to the session. The size limit for attachments is 100 megabytes, and the system provides end-to-end encryption for your data.

Attachments are ideal when you need to send more than just a few kilobytes of information to other participants, and want to do so as efficiently as possible. Use them to send images or large data objects that the group creates or adds to the activity. The Group Activities framework efficiently manages the transfer of attachments among devices, avoiding multiple downloads of the same data to each device.

> **Note**: Don’t use a [`GroupSessionJournal`](groupsessionjournal.md) object to store files larger than 100 megabytes, or when you need to protect or validate content before someone downloads it. Instead, store those files on your company’s server and let participants download them from there.

The [`GroupSessionJournal`](groupsessionjournal.md) object delivers attachments to your app using an [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) type. To receive attachments, configure a task and use a `for..in` loop and wait on the attachments property of your journal object, as shown in the following example. When attachments are available for your device, the system wakes up your task and delivers an array of [`GroupSessionJournal.Attachment`](groupsessionjournal/attachment.md) structures for you to process.

```swift
task = Task {
    for await images in journal.attachments {
        await handleImages(images)
    }
}
```

Use the [`GroupSessionJournal.Attachment`](groupsessionjournal/attachment.md) structures your app receives to download the attachment data and fetch any related metadata. You can then use that data to create any local data structures you need to update the state of your activity. The following example shows how to iterate over the attachments you receive and fetch the data for each one. The `ImageMetadataMessage` type is a custom structure the activity uses to store extra information about the image data.

```swift
func handleImages(_ attachments: GroupSessionJournal.Attachments.Element) async {
    attachments.forEach { attachment in
        let metadata = try await attachment.loadMetadata(of: 
            ImageMetadataMessage.self)
        let imageData = try await attachment.load(Data.self)
            
        // Use the data to create app-specific structures and
        // update the activity.
    }
}
```

For more information about storing files and data attachments, see [`GroupSessionJournal`](groupsessionjournal.md).

## See Also

- [class GroupSessionMessenger](groupsessionmessenger.md)
  An object that transfers app-specific data between the devices joined in a group session.
- [class GroupSessionJournal](groupsessionjournal.md)
  An object that manages file and data transfers between participants joined in a group session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/GroupActivities/synchronizing-data-during-a-shareplay-activity)*