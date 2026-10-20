# STScreenTimeConfigurationObserver

**Framework**: Screen Time  
**Kind**: class  
**Role**: Class

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

```objc
@interface STScreenTimeConfigurationObserver : NSObject
```

#### Overview

Use this class to start and stop observing the current configuration. For example, you can opt to disable private browsing in your web browser’s view controller when [`enforcesChildRestrictions`](./stscreentimeconfiguration/enforceschildrestrictions.md) is `true`.

## Topics

### Initializers
- [init(updateQueue: dispatch_queue_t)](./stscreentimeconfigurationobserver/init%28updatequeue%29.md)
  Creates a configuration observer that reports updates on the queue you specify.
### Instance properties
- [var configuration: STScreenTimeConfiguration?](./stscreentimeconfigurationobserver/configuration.md)
  The configuration being observed.
### Instance methods
- [func startObserving()](./stscreentimeconfigurationobserver/startobserving%28%29.md)
  Starts observing changes to the current configuration.
- [func stopObserving()](./stscreentimeconfigurationobserver/stopobserving%28%29.md)
  Stops observing changes to the current configuration.

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

## See Also

### Configuration queries
- [class STScreenTimeConfiguration](./stscreentimeconfiguration.md)
  The configuration for this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stscreentimeconfigurationobserver)*