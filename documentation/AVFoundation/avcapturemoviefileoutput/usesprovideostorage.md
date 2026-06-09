# usesProVideoStorage

**Framework**: AVFoundation  
**Kind**: property

Whether this movie file output is configured to write to Pro Video Storage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
var usesProVideoStorage: Bool { get set }
```

#### Discussion

Default is `NO`. Raises an exception if set to `YES` while proVideoStorageSupported is `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/usesprovideostorage)*