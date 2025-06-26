# NISession

**Framework**: Nearby Interaction  
**Kind**: class

An object that identifies a unique connection between two peer devices.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
class NISession
```

## Mentions

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)
- [Discovering peers with Multipeer Connectivity](discovering-peers-with-multipeer-connectivity.md)
- [Extending advanced direction finding and ranging](extending-advanced-direction-finding-and-ranging.md)

#### Overview

This class represents the central mechanism to interact with nearby objects, for example, a peer Apple device or third-party accessory. After creating an [`NISession`](nisession.md) for a nearby object, the app interacts with the object by receiving [`NISessionDelegate`](nisessiondelegate.md) callbacks.

One session represents an interaction between the user and a single nearby object. To interact with multiple nearby objects, create a separate session for each.

For more information, see [`Initiating and maintaining a session`](initiating-and-maintaining-a-session.md).

## Topics

### Ensuring feature support
- [class var deviceCapabilities: any NIDeviceCapability](nisession/devicecapabilities.md)
  An object that communicates the device’s supported framework features.
- [protocol NIDeviceCapability](nidevicecapability.md)
  An interface that adds Boolean values that indicate an interaction session feature support.
### Connecting to A Peer Device
- [var discoveryToken: NIDiscoveryToken?](nisession/discoverytoken.md)
  A temporary, random identifier for a device.
- [class NIDiscoveryToken](nidiscoverytoken.md)
  An object that uniquely identifies a peer that participates in an interaction session.
- [func run(NIConfiguration)](nisession/run(_:).md)
  Starts a session with a nearby peer.
- [var configuration: NIConfiguration?](nisession/configuration.md)
  The configuration run by the session.
- [var delegateQueue: dispatch_queue_t?](nisession/delegatequeue.md)
  The dispatch queue on which the session invokes delegate callbacks.
### Managing life cycle
- [var delegate: (any NISessionDelegate)?](nisession/delegate.md)
  An object that the framework notifies of session events.
- [func pause()](nisession/pause.md)
  Stops sending distance and direction updates to the peer.
- [func invalidate()](nisession/invalidate.md)
  Stops a running session.
### Utilizing Camera Assistance
- [func setARSession(ARSession)](nisession/setarsession(_:).md)
  Provides the framework with an existing AR session to use for Camera Assistance.
- [func worldTransform(for: NINearbyObject) -> simd_float4x4?](nisession/worldtransform(for:).md)
  Returns a world transform to integrate a nearby object in an AR experience.
### Deprecated
- [class var isSupported: Bool](nisession/issupported.md)
  A Boolean value that indicates whether the device supports basic interaction-session functionality.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)
  Measure the relative position of a nearby device and coach the user to sustain interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession)*