# AVProVideoStorage.BusyReason

**Framework**: AVFoundation  
**Kind**: struct

A reason that Pro Video Storage may be busy.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
struct BusyReason
```

## Topics

### Initializers
- [init(rawValue: String)](avprovideostorage/busyreason/init(rawvalue:).md)
### Type Properties
- [static let adjustingCapacity: AVProVideoStorage.BusyReason](avprovideostorage/busyreason/adjustingcapacity.md)
  Pro Video Storage is being created or resized.
- [static let capturing: AVProVideoStorage.BusyReason](avprovideostorage/busyreason/capturing.md)
  A capture to Pro Video Storage is in progress.
- [static let replenishing: AVProVideoStorage.BusyReason](avprovideostorage/busyreason/replenishing.md)
  Pro Video Storage capacity is being replenished.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var busyReasons: Set<AVProVideoStorage.BusyReason>](avprovideostorage/busyreasons.md)
  Whether Pro Video Storage is busy and the associated reasons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avprovideostorage/busyreason)*