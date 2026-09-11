# usesProVideoStorage

**Framework**: AVFoundation  
**Kind**: property

Indicates whether to use pre-allocated storage.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

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