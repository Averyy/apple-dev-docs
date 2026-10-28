# usesProVideoStorage

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Whether this movie file output is configured to write to Pro Video Storage.

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

```objc
@property (nonatomic) BOOL usesProVideoStorage;
```

## Discussion

Default is `NO`. Raises an exception if set to `YES` while proVideoStorageSupported is `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/usesprovideostorage)*