# Defining your app’s SharePlay activities

**Framework**: Group Activities

Configure your app’s SharePlay support and define the activities that people can perform from your app.

#### Overview

SharePlay activities are an organic way to create experiences that people can enjoy together. When you add the Group Activities framework to your app, you gain the ability to share your app’s features over FaceTime, Messages, and AirDrop. Some examples of experiences people can share together include:

- Watching or listening to content
- Participating in an online fitness class
- Creating content on a shared whiteboard or painter’s canvas
- Shopping for food, clothes, or other online products
- Planning a trip or browsing the web
- Reading a book or taking an online class

Consider the preceding list of activities, and any other activities your app supports, and build SharePlay support for them. Think about how people might enjoy those activities if they were together in the same physical space. Consider the types of interactions that can occur in the real world, and build support for those interactions into your activities. For example, a movie-watching app needs to pause playback for all participants when one person hits the pause button. A shared whiteboard app needs to transmit newly drawn content to other participants, and send all of the content to someone who arrives late.

> **Note**: Make activities available on all the platforms your app supports to ensure people can join from any device. Customize the experience as needed for each platform to give it a more intuitive feel.

After configuring your SharePlay activities, you can display and start them from the share sheet. See [`Presenting SharePlay activities from your app’s UI`](promoting-shareplay-activities-from-your-apps-ui.md) for more information.

##### Configure the Group Activities Capability

Before you start adding SharePlay support to your app, add the `Group Activities` capability to your Xcode project. Because SharePlay involves communication with other devices, you need this capability to support activities. To add the capability to your app:

1. Open your Xcode project.
2. Select your app target.
3. Go to the Signing & Capabilities pane.
4. Add the Group Activities capability to the target.

Configure this capability only for app targets. When you add the Group Activities capability, Xcode adds the necessary entitlements to your app and updates its provisioning profile.
For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/xcode/adding-capabilities-to-your-app).

##### Create an Activity

Create a SharePlay experience by defining a struct conforming to the [`GroupActivity`](groupactivity.md) protocol. This protocol provides the basic definition of a SharePlay activity and provides the information that SharePlay needs to promote that activity to participants.

Ensure the data being shared during your activity conforms to [`Codable`](https://developer.apple.com/documentation/swift/codable). If you want to use the share sheet in SwiftUI to share an activity, it requires items to support the [`Transferable`](https://developer.apple.com/documentation/coretransferable/transferable) protocol. Adopt this protocol in your custom data types and implement the [`transferRepresentation`](https://developer.apple.com/documentation/coretransferable/transferable/transferrepresentation) property.

Most of the content in a [`GroupActivity`](groupactivity.md) type is the data you use to support the activity itself. Include data that is critical for performing the activity, such as the type of game in a game-playing activity. Include information to support the overall experience, such as a title, to display in the SharePlay UI. Store as little data as possible to support the activity. For instance, store a link to a video rather than the file itself. Also share state information instead of detailed changes wherever possible. The following example defines a `BoardGame` type that stores information about the type of game, and a group activity to share the experience:

```swift
enum BoardGame: String, Codable, Transferable {
    case chess, checkers

    static var transferRepresentation: some TransferRepresentation {
        // Define a custom `UTType`. 
        CodableRepresentation(contentType: .boardGame)
    }
}

struct BoardGameActivity: GroupActivity, Transferable {
    var boardGame: BoardGame

    init(boardGame: BoardGame) {
        self.boardGame = boardGame
    }
}
```

Ensure your [`GroupActivity`](groupactivity.md) type conforms to [`Transferable`](https://developer.apple.com/documentation/coretransferable/transferable). This conformance allows SwiftUI to present possible activities from your UI and enables SharePlay to share them via AirDrop. When including a [`ShareLink`](https://developer.apple.com/documentation/swiftui/sharelink) view in your SwiftUI app, specify the transferable data type as the shareable item from that view. When someone taps or clicks the link, the system displays a share sheet with options for starting the associated activity. For information on starting an activity and using a `ShareLink`, see [`Presenting SharePlay activities from your app’s UI`](promoting-shareplay-activities-from-your-apps-ui.md).

> **Note**: If you have multiple activities in your app, each [`GroupActivity`](groupactivity.md) type must have a unique string in its [`activityIdentifier`](groupactivity/activityidentifier.md) property.

##### Provide Descriptive Information About the Activity

Each activity contains a [`GroupActivityMetadata`](groupactivitymetadata.md) type that stores descriptive information about the activity. When inviting people to join the activity, the system incorporates this metadata into the system UI. A concise title, a short description of the activity, and an image help people understand which activity they’re joining. You can also provide additional details, such as a fallback URL that someone can use to join the activity from a web browser.

Create a [`GroupActivityMetadata`](groupactivitymetadata.md) type dynamically from your activity, and populate it with activity-related details. Fill in as much of the information as possible, and make your descriptions concise and clear. People need to quickly identify the purpose of the activity and whether it’s one they want to join, so make sure your descriptions are clear enough for someone to make a decision.

```swift
extension BoardGameActivity {
    // Provide information about the activity.
    var metadata: GroupActivityMetadata {
        var metadata = GroupActivityMetadata()
        metadata.type = .generic
        metadata.title = boardGame.rawValue
        return metadata
    }
}
```

Classify your app’s activities by specifying an appropriate value for the [`type`](groupactivitymetadata/type.md) property of [`GroupActivityMetadata`](groupactivitymetadata.md). In the SharePlay banner or share sheet, the system displays an icon that matches the type of the activity. The icon provides an additional visual cue about what people can expect from the activity.

## See Also

- [Supporting coordinated media playback](../avfoundation/supporting-coordinated-media-playback.md)
  Create synchronized media experiences that enable users to watch and listen across devices.
- [protocol GroupActivity](groupactivity.md)
  A type that can advertise your app’s activities to other participants.
- [struct GroupActivityMetadata](groupactivitymetadata.md)
  Text and image content that describes an activity to potential participants.
- [enum GroupActivityActivationResult](groupactivityactivationresult.md)
  The result of preparing to start a custom activity.
- [struct GroupActivityTransferRepresentation](groupactivitytransferrepresentation.md)
  A type that lets you start a group activity from a known context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/defining-your-apps-shareplay-activities)*