# PTChannelManager

**Framework**: Push to Talk  
**Kind**: class  
**Role**: Class

An object that represents a push-to-talk channel manager.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
class PTChannelManager
```

```objc
@interface PTChannelManager : NSObject
```

## Mentions

- [Creating a Push to Talk app](./creating-a-push-to-talk-app.md)

#### Overview

You must create a channel manager upon launching your app, otherwise the system tears down channels and their ability to receive push notifications. By providing a [`PTChannelRestorationDelegate`](./ptchannelrestorationdelegate.md), an app can rejoin or leave a previously active channel the system knows about. Once the channel resoration process completes, the system provides a [`PTChannelManager`](./ptchannelmanager.md) instance.

```swift
// Create a channel manager instance.    
channelManager = try await PTChannelManager.channelManager(delegate: self,
                                                           restorationDelegate: self)
```

Multiple calls to [`channelManager(delegate:restorationDelegate:completionHandler:)`](./ptchannelmanager/channelmanager%28delegate,restorationdelegate,completionhandler%29.md) result in the system returning the same shared instance, so store the channel manager in an instance variable.

## Topics

### Creating a channel manager
- [class func channelManager(delegate: any PTChannelManagerDelegate, restorationDelegate: any PTChannelRestorationDelegate, completionHandler: (PTChannelManager?, (any Error)?) -> Void)](./ptchannelmanager/channelmanager%28delegate,restorationdelegate,completionhandler%29.md)
  Creates a channel manager with the configuration you specify.
### Inspecting the channel manager
- [var activeChannelUUID: UUID?](./ptchannelmanager/activechanneluuid.md)
  The unique identifier of the active channel for the app.
### Joining and leaving a channel
- [func requestJoinChannel(channelUUID: UUID, descriptor: PTChannelDescriptor)](./ptchannelmanager/requestjoinchannel%28channeluuid,descriptor%29.md)
  Joins a channel with the identifier and descriptor you specify.
- [func leaveChannel(channelUUID: UUID)](./ptchannelmanager/leavechannel%28channeluuid%29.md)
  Leaves a channel with the identifier.
### Setting the transmission mode
- [func setTransmissionMode(PTTransmissionMode, channelUUID: UUID, completionHandler: (((any Error)?) -> Void)?)](./ptchannelmanager/settransmissionmode%28_,channeluuid,completionhandler%29.md)
  Sets the audio transmission mode for the channel you specify.
### Starting and stopping transmission
- [func requestBeginTransmitting(channelUUID: UUID)](./ptchannelmanager/requestbegintransmitting%28channeluuid%29.md)
  Begins an audio transmission with the channel identifer you specify.
- [func stopTransmitting(channelUUID: UUID)](./ptchannelmanager/stoptransmitting%28channeluuid%29.md)
  Stops an audio transmission with the channel identifer you specify.
- [func setAccessoryButtonEventsEnabled(Bool, channelUUID: UUID, completionHandler: (((any Error)?) -> Void)?)](./ptchannelmanager/setaccessorybuttoneventsenabled%28_,channeluuid,completionhandler%29.md)
  Maps supported accessory button events to actions that begin and end transmission.
### Setting participants
- [func setActiveRemoteParticipant(PTParticipant?, channelUUID: UUID, completionHandler: (((any Error)?) -> Void)?)](./ptchannelmanager/setactiveremoteparticipant%28_,channeluuid,completionhandler%29.md)
  Sets the active remote participant with the channel identifier.
### Setting the channel descriptor
- [func setChannelDescriptor(PTChannelDescriptor, channelUUID: UUID, completionHandler: (((any Error)?) -> Void)?)](./ptchannelmanager/setchanneldescriptor%28_,channeluuid,completionhandler%29.md)
  Sets the channel description.
### Setting the service status
- [func setServiceStatus(PTServiceStatus, channelUUID: UUID, completionHandler: (((any Error)?) -> Void)?)](./ptchannelmanager/setservicestatus%28_,channeluuid,completionhandler%29.md)
  Sets the service connection status.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Essentials
- [Creating a Push to Talk app](./creating-a-push-to-talk-app.md)
  Build a walkie-talkie style app with system user interface controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanager)*