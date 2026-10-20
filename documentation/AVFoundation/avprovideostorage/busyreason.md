# AVProVideoStorage.BusyReason

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A reason that Pro Video Storage may be busy.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
struct BusyReason
```

```c
typedef NSString * AVProVideoStorageBusyReason;
```

## Topics

### Initializers
- [init(rawValue: String)](./busyreason/init%28rawvalue%29.md)
### Type Properties
- [static let adjustingCapacity: AVProVideoStorage.BusyReason](./busyreason/adjustingcapacity.md)
  Pro Video Storage is being created or resized.
- [static let capturing: AVProVideoStorage.BusyReason](./busyreason/capturing.md)
  A capture to Pro Video Storage is in progress.
- [static let replenishing: AVProVideoStorage.BusyReason](./busyreason/replenishing.md)
  Pro Video Storage capacity is being replenished.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Determining whether storage is busy
- [var busyReasons: Set<AVProVideoStorage.BusyReason>](./busyreasons.md)
  Whether Pro Video Storage is busy and the associated reasons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avprovideostorage/busyreason)*