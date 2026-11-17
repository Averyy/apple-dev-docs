# URLSessionTaskMetrics.EarlyDataStatus

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

Whether a request was sent in TLS early data, and whether the server accepted it.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
enum EarlyDataStatus
```

```c
enum NSURLSessionTaskMetricsEarlyDataStatus : NSInteger;
```

## Topics

### Enumeration Cases
- [URLSessionTaskMetrics.EarlyDataStatus.attempted](./earlydatastatus/attempted.md)
  The request was sent in early data, but the server didn’t accept it.
- [URLSessionTaskMetrics.EarlyDataStatus.attemptedAndAccepted](./earlydatastatus/attemptedandaccepted.md)
  The request was sent in early data, and the server accepted it.
- [URLSessionTaskMetrics.EarlyDataStatus.notAttempted](./earlydatastatus/notattempted.md)
  The request wasn’t sent in early data.
### Initializers
- [init?(rawValue: Int)](./earlydatastatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics/earlydatastatus)*