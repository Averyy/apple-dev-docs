# GroupSessionMessenger

**Framework**: Group Activities  
**Kind**: class

An object that transfers app-specific data between the devices joined in a group session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
final class GroupSessionMessenger
```

## Mentions

- [Synchronizing data during a SharePlay activity](synchronizing-data-during-a-shareplay-activity.md)
- [Configure your visionOS app for sharing with people nearby](configure-your-app-for-sharing-with-people-nearby.md)

#### Overview

Use a `GroupSessionMessenger` object to coordinate your app’s behavior across the devices attached to a group session. This object leverages the existing FaceTime communication channel to send app-specific data related to a SharePlay experience. For example, a movie-watching app might share user comments or tags while the movie plays.

You create a `GroupSessionMessenger` object directly and use it to send and receive app data. Create the messenger using an active [`GroupSession`](groupsession.md) object, which manages the underlying communication channel. Store a strong reference to your `GroupSessionMessenger` object for the lifetime of the session. The following example shows a custom object for managing a movie-watching experience. The object stores the GroupSession object associated with the experience and creates a `GroupSessionMessenger` for sending messages between participants.

```swift
class CowatchingExperience : ObservableObject {
    let groupSession: GroupSession<Trailer>
    let messenger: GroupSessionMessenger

    init(groupSession: GroupSession<Trailer>, item: Trailer) {
        self.groupSession = groupSession
        self.messenger = GroupSessionMessenger(session: groupSession)

        self.groupSession.join()
        // …
    }
}
```

For more information about establishing a group session, see [`GroupSession`](groupsession.md).

##### Receive Messages From Other Devices

The system delivers messages to your app asynchronously when they arrive and adds them to a message sequence. Use the [`messages(of:)`](groupsessionmessenger/messages(of:)-626qo.md) or [`messages(of:)`](groupsessionmessenger/messages(of:)-jvoz.md) method to retrieve the sequence you want and iterate over its results. Use a `for`-`in` loop with the `await` keyword to iterate asynchronously over the results. The following example shows how a Tic Tac Toe game might retrieve moves sent by the current opponent. After receiving each move, the code adds that move to the current participant’s board.

```swift
let sessionMessenger = GroupSessionMessenger(session: groupSession)

async {
    for await move in sessionMessenger.messages(of: TicTacToe.Move.self) {
        self.board.addMove(move)
    }
}
```

## Topics

### Creating a group session messenger
- [init<Activity>(session: GroupSession<Activity>)](groupsessionmessenger/init(session:).md)
  Creates a new group session messenger with [`GroupSessionMessenger.DeliveryMode.reliable`](groupsessionmessenger/deliverymode-swift.enum/reliable.md) delivery mode and associates it with the specified session object.
### Sending data to the group
- [func send(Data, to: Participants) async throws](groupsessionmessenger/send(_:to:)-4o52m.md)
  Sends a standard data object asynchronously to other participants in the group session.
- [func send<Message>(Message, to: Participants) async throws](groupsessionmessenger/send(_:to:)-2a4ku.md)
  Sends a custom type asynchronously to other participants in the group session.
- [func send(Data, to: Participants, completion: ((any Error)?) -> Void)](groupsessionmessenger/send(_:to:completion:)-zufl.md)
  Sends a standard data object to other participants in the group session.
- [func send<Message>(Message, to: Participants, completion: ((any Error)?) -> Void)](groupsessionmessenger/send(_:to:completion:)-9e0sn.md)
  Sends a custom type to other participants in the group session.
- [enum Participants](participants.md)
  The set of participants to include in messages.
### Receiving data from other participants
- [func messages(of: Data.Type) -> GroupSessionMessenger.Messages<Data>](groupsessionmessenger/messages(of:)-626qo.md)
  Returns the asynchronous sequence of messages that contain a generic data object.
- [func messages<Message>(of: Message.Type) -> GroupSessionMessenger.Messages<Message>](groupsessionmessenger/messages(of:)-jvoz.md)
  Returns the asynchronous sequence of messages that match the app-specific type.
- [GroupSessionMessenger.Messages](groupsessionmessenger/messages.md)
  An asynchronous sequence of messages sent to the session.
- [GroupSessionMessenger.MessageContext](groupsessionmessenger/messagecontext.md)
  A structure that contains additional information about an incoming message, such as which device sent it.
### Initializers
- [init<Activity>(session: GroupSession<Activity>, deliveryMode: GroupSessionMessenger.DeliveryMode)](groupsessionmessenger/init(session:deliverymode:).md)
  Creates a new group session messenger with the specified delivery mode, [`GroupSessionMessenger.DeliveryMode`](groupsessionmessenger/deliverymode-swift.enum.md), and associates it with the specified session object.
### Instance Properties
- [let deliveryMode: GroupSessionMessenger.DeliveryMode](groupsessionmessenger/deliverymode-swift.property.md)
  The [`GroupSessionMessenger.DeliveryMode`](groupsessionmessenger/deliverymode-swift.enum.md) specified at initialization time (defaults to `reliable`).
### Enumerations
- [GroupSessionMessenger.DeliveryMode](groupsessionmessenger/deliverymode-swift.enum.md)
  The transmission characteristics to apply to the delivery of messages.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Synchronizing data during a SharePlay activity](synchronizing-data-during-a-shareplay-activity.md)
  Send custom messages and data between devices to synchronize content for your activity, and incorporate messages your app receives from other participants.
- [class GroupSessionJournal](groupsessionjournal.md)
  An object that manages file and data transfers between participants joined in a group session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionmessenger)*