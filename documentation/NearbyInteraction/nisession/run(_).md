# run(_:)

**Framework**: Nearby Interaction  
**Kind**: method  
**Role**: Instance Method

Starts a session with a nearby peer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
func run(_ configuration: NIConfiguration)
```

```objc
- (void) runWithConfiguration:(NIConfiguration *) configuration;
```

#### Discussion

This function starts an interaction session between two devices.

Before calling this function, ensure the device supports the features your app requires by first inspecting global [`deviceCapabilities`](./devicecapabilities.md).

##### Restart an Interaction Session

To restart a session as the result of unpausing, call this function as described in [`pause()`](./pause%28%29.md). The app calls this function when resuming from session suspension, as described in [`sessionSuspensionEnded(_:)`](../nisessiondelegate/sessionsuspensionended%28_%29.md).

> **Note**:  A session’s [`discoveryToken`](./discoverytoken.md) maintains its original value through restarts.

##### Prompt for User Approval

The framework prompts for user permission to provide its relative position to nearby peers when it calls this function the first time the app launches. On subsequent calls to this function, the framework consults a preference in Settings that stores the user’s decision. For more information, see [Initiating and maintaining a session](../initiating-and-maintaining-a-session.md).

## Parameters

- `configuration`: An object that indicates an interaction session’s features.

## See Also

### Connecting to a peer device
- [var discoveryToken: NIDiscoveryToken?](./discoverytoken.md)
  A temporary, random identifier for a device.
- [class NIDiscoveryToken](../nidiscoverytoken.md)
  An object that uniquely identifies a peer that participates in an interaction session.
- [var configuration: NIConfiguration?](./configuration.md)
  The configuration run by the session.
- [var delegateQueue: dispatch_queue_t?](./delegatequeue.md)
  The dispatch queue on which the session invokes delegate callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession/run(_:))*