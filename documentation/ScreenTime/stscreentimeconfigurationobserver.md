# STScreenTimeConfigurationObserver

**Framework**: Screen Time  
**Kind**: class

The object you use to observe changes to the current configuration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
class STScreenTimeConfigurationObserver
```

#### Overview

Use this class to start and stop observing the current configuration. For example, you can opt to disable private browsing in your web browser’s view controller when [`enforcesChildRestrictions`](stscreentimeconfiguration/enforceschildrestrictions.md) is `true`.

## Topics

### Initializers
- [init(updateQueue: dispatch_queue_t)](stscreentimeconfigurationobserver/init(updatequeue:).md)
  Creates a configuration observer that reports updates on the queue you specify.
### Instance properties
- [var configuration: STScreenTimeConfiguration?](stscreentimeconfigurationobserver/configuration.md)
  The configuration being observed.
### Instance methods
- [func startObserving()](stscreentimeconfigurationobserver/startobserving.md)
  Starts observing changes to the current configuration.
- [func stopObserving()](stscreentimeconfigurationobserver/stopobserving.md)
  Stops observing changes to the current configuration.

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

- [class STScreenTimeConfiguration](stscreentimeconfiguration.md)
  The configuration for this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stscreentimeconfigurationobserver)*