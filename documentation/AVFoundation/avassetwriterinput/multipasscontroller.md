# AVAssetWriterInput.MultiPassController

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

Provides an interface to receive an async sequence of pass descriptions for the writer input receiver, if multi-pass is supported.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class MultiPassController
```

## Topics

### Accessing pass descriptions
- [var passDescriptions: (some AsyncSequence<AVAssetWriterInputPassDescription, Never>)?](./multipasscontroller/passdescriptions.md)
  An async sequence of pass descriptions to iterate over if multi-pass is supported. This property is nil when multi-pass is not supported.

## See Also

### Performing multiple-pass encoding
- [var canPerformMultiplePasses: Bool](./canperformmultiplepasses.md)
  A Boolean value that indicates whether the input may perform multiple passes over appended media data.
- [var currentPassDescription: AVAssetWriterInputPassDescription?](./currentpassdescription.md)
  An object that describes the requirements for the current pass.
- [class AVAssetWriterInputPassDescription](../avassetwriterinputpassdescription.md)
  An object that defines the interface to query for the requirements of the current pass.
- [func markCurrentPassAsFinished()](./markcurrentpassasfinished%28%29.md)
  Tells the input to analyze the appended media to determine whether it can improve the results by reencoding certain segments.
- [var performsMultiPassEncodingIfSupported: Bool](./performsmultipassencodingifsupported.md)
  A Boolean value that indicates whether the input attempts to encode the source media data using multiple passes.
- [func respondToEachPassDescription(on: dispatch_queue_t, using: () -> Void)](./respondtoeachpassdescription%28on,using%29.md)
  Tells the input to invoke a callback whenever it begins a new pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/multipasscontroller)*