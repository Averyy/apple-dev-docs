# AVAssetReaderCaptionValidationHandling

**Framework**: AVFoundation  
**Kind**: protocol

A protocol that defines the methods for caption validation events.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
protocol AVAssetReaderCaptionValidationHandling : NSObjectProtocol
```

## Topics

### Validating Captions
- [func captionAdaptor(AVAssetReaderOutputCaptionAdaptor, didVendCaption: AVCaption, skippingUnsupportedSourceSyntaxElements: [String])](avassetreadercaptionvalidationhandling/captionadaptor(_:didvendcaption:skippingunsupportedsourcesyntaxelements:).md)
  Tells the delegate that the adaptor ignored one or more syntax elements when it created the caption object.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var validationDelegate: (any AVAssetReaderCaptionValidationHandling)?](avassetreaderoutputcaptionadaptor/validationdelegate.md)
  A delegate object that handles callbacks to the caption adaptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreadercaptionvalidationhandling)*