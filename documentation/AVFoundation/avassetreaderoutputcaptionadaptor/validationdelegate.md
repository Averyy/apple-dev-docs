# validationDelegate

**Framework**: AVFoundation  
**Kind**: property

A delegate object that handles callbacks to the caption adaptor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
weak var validationDelegate: (any AVAssetReaderCaptionValidationHandling)? { get set }
```

## See Also

- [protocol AVAssetReaderCaptionValidationHandling](avassetreadercaptionvalidationhandling.md)
  A protocol that defines the methods for caption validation events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputcaptionadaptor/validationdelegate)*