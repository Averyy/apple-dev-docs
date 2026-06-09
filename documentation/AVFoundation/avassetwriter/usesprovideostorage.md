# usesProVideoStorage

**Framework**: AVFoundation  
**Kind**: property

Indicates whether to use pre-allocated storage.

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

The default value is `NO`. See more detailed description of ProVideoStorage in `AVProVideoStorage.h`.

An exception will be thrown if clients try to set `YES` if the value of the `proVideoStorageSupported` property is `NO`.

An exception will be thrown if clients try to set this property after `-startWriting` has been called on the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/usesprovideostorage)*