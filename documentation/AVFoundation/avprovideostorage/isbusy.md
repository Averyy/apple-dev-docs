# isBusy

**Framework**: AVFoundation  
**Kind**: property

Indicates whether Pro Video Storage is currently busy.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
var isBusy: Bool { get }
```

#### Discussion

A value of `YES` indicates that Pro Video Storage is currently being modified (e.g., during capacity changes or file creation/deletion). While this is `YES`, if a client tries to start a video capture an exception will be raised. This property is key-value observable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avprovideostorage/isbusy)*