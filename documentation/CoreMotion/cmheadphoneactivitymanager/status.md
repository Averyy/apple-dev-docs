# CMHeadphoneActivityManager.Status

**Framework**: Core Motion  
**Kind**: enum  
**Role**: Enumeration

Headphone connection status updates.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
enum Status
```

```c
enum CMHeadphoneActivityStatus : NSInteger;
```

## Topics

### Enumeration Cases
- [CMHeadphoneActivityManager.Status.connected](./status/connected.md)
  A compatible set of headphones is connected.
- [CMHeadphoneActivityManager.Status.disconnected](./status/disconnected.md)
  The headphones disconnected.
### Initializers
- [init?(rawValue: Int)](./status/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting Types
- [CMHeadphoneActivityManager.ActivityHandler](./activityhandler.md)
  The type for a handler to be invoked when headphone motion activity data is available.
- [CMHeadphoneActivityManager.StatusHandler](./statushandler.md)
  The type for a handler to be invoked with status updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/status)*