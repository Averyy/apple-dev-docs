# currentPassDescription

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An object that describes the requirements for the current pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var currentPassDescription: AVAssetWriterInputPassDescription? { get }
```

```objc
@property (readonly, nullable) AVAssetWriterInputPassDescription * currentPassDescription;
```

#### Discussion

If the value of this property is `nil`, call the asset writer input’s [`markAsFinished()`](./markasfinished%28%29.md) method because there are no more requests to fulfill.

During the first pass, the request contains a single time range value, from zero to positive infinity, that indicates to append all media from the source. This condition is also true when [`canPerformMultiplePasses`](./canperformmultiplepasses.md) is [`false`](../../Swift/false.md), in which case the asset writer only performs a single pass.

The value of this property is `nil` before you call [`startWriting()`](../avassetwriter/startwriting%28%29.md) on the containing asset writer. It transitions to an initial non-`nil` value during the call to [`startWriting()`](../avassetwriter/startwriting%28%29.md), and changes only after a call to [`markCurrentPassAsFinished()`](./markcurrentpassasfinished%28%29.md). You can use the [`respondToEachPassDescription(on:using:)`](./respondtoeachpassdescription%28on,using%29.md) to have the system call you at the beginning of each pass.

This property is key-value observable. The system doesn’t notify an observer on a specific thread.

## See Also

### Performing multiple-pass encoding
- [var canPerformMultiplePasses: Bool](./canperformmultiplepasses.md)
  A Boolean value that indicates whether the input may perform multiple passes over appended media data.
- [class AVAssetWriterInputPassDescription](../avassetwriterinputpassdescription.md)
  An object that defines the interface to query for the requirements of the current pass.
- [func markCurrentPassAsFinished()](./markcurrentpassasfinished%28%29.md)
  Tells the input to analyze the appended media to determine whether it can improve the results by reencoding certain segments.
- [var performsMultiPassEncodingIfSupported: Bool](./performsmultipassencodingifsupported.md)
  A Boolean value that indicates whether the input attempts to encode the source media data using multiple passes.
- [func respondToEachPassDescription(on: dispatch_queue_t, using: () -> Void)](./respondtoeachpassdescription%28on,using%29.md)
  Tells the input to invoke a callback whenever it begins a new pass.
- [AVAssetWriterInput.MultiPassController](./multipasscontroller.md)
  Provides an interface to receive an async sequence of pass descriptions for the writer input receiver, if multi-pass is supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/currentpassdescription)*