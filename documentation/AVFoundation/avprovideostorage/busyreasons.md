# busyReasons

**Framework**: AVFoundation  
**Kind**: property

Whether Pro Video Storage is busy and the associated reasons.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
var busyReasons: Set<AVProVideoStorage.BusyReason> { get }
```

#### Discussion

A non-empty set indicates that Pro Video Storage is currently being modified. While this is non-empty, starting a video capture will fail with an error. This property is key-value observable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avprovideostorage/busyreasons)*