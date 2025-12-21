# canPerformMultiplePasses

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the input may perform multiple passes over appended media data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var canPerformMultiplePasses: Bool { get }
```

#### Discussion

When the value for this property is [`true`](https://developer.apple.com/documentation/Swift/true), configure your source media data for random access. After appending the media data for the current pass, as specified by the [`currentPassDescription`](avassetwriterinput/currentpassdescription.md) property, call [`markCurrentPassAsFinished()`](avassetwriterinput/markcurrentpassasfinished().md) so the system can determine whether it needs to perform additional passes. The system may perform only the initial pass if it determines there’s no benefit to performing multiple passes.

When the value for this property is [`false`](https://developer.apple.com/documentation/Swift/false), your source for media data only needs to support sequential access. In this case, append all of the source media one time and call [`markAsFinished()`](avassetwriterinput/markasfinished().md).

The default value is [`false`](https://developer.apple.com/documentation/Swift/false). Currently the only way for this property to become [`true`](https://developer.apple.com/documentation/Swift/true) is when the value of [`performsMultiPassEncodingIfSupported`](avassetwriterinput/performsmultipassencodingifsupported.md) is [`true`](https://developer.apple.com/documentation/Swift/true). The final value is available after you call [`startWriting()`](avassetwriter/startwriting().md).

This property is key-value observable.

## See Also

- [var currentPassDescription: AVAssetWriterInputPassDescription?](avassetwriterinput/currentpassdescription.md)
  An object that describes the requirements for the current pass.
- [class AVAssetWriterInputPassDescription](avassetwriterinputpassdescription.md)
  An object that defines the interface to query for the requirements of the current pass.
- [func markCurrentPassAsFinished()](avassetwriterinput/markcurrentpassasfinished.md)
  Tells the input to analyze the appended media to determine whether it can improve the results by reencoding certain segments.
- [var performsMultiPassEncodingIfSupported: Bool](avassetwriterinput/performsmultipassencodingifsupported.md)
  A Boolean value that indicates whether the input attempts to encode the source media data using multiple passes.
- [func respondToEachPassDescription(on: dispatch_queue_t, using: () -> Void)](avassetwriterinput/respondtoeachpassdescription(on:using:).md)
  Tells the input to invoke a callback whenever it begins a new pass.
- [AVAssetWriterInput.MultiPassController](avassetwriterinput/multipasscontroller.md)
  Provides an interface to receive an async sequence of pass descriptions for the writer input receiver, if multi-pass is supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/canperformmultiplepasses)*