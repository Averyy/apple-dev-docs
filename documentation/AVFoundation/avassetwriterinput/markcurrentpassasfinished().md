# markCurrentPassAsFinished()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the input to analyze the appended media to determine whether it can improve the results by reencoding certain segments.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func markCurrentPassAsFinished()
```

```objc
- (void) markCurrentPassAsFinished;
```

## Discussion

When the value of the [`canPerformMultiplePasses`](./canperformmultiplepasses.md) property is [`true`](../../Swift/true.md), call this method after you append all of your media data. After the input determines if it warrants performing an additional pass, the value of [`currentPassDescription`](./currentpassdescription.md) changes (typically asynchronously) to describe how to set up for the next pass. Although it’s possible to use key-value observing to determine when the value of [`currentPassDescription`](./currentpassdescription.md) changes, it’s typically more convenient to call the [`respondToEachPassDescription(on:using:)`](./respondtoeachpassdescription%28on,using%29.md) method to start the work for each pass.

After reappending the media data for all of the time ranges of the new pass, call this method again to determine whether to reappend segments in another pass.

Calling this method effectively cancels any previous invocation of [`requestMediaDataWhenReady(on:using:)`](./requestmediadatawhenready%28on,using%29.md), which means that you may call [`requestMediaDataWhenReady(on:using:)`](./requestmediadatawhenready%28on,using%29.md) again for each new pass. This method provides a convenient way to consolidate these invocations in your code.

After each pass, you have the option of keeping the most recent results by calling [`markAsFinished()`](./markasfinished%28%29.md), instead of this method. If the value of [`currentPassDescription`](./currentpassdescription.md) is `nil` at the beginning of a pass, call [`markAsFinished()`](./markasfinished%28%29.md) to tell the input to not expect any further media data.

If the value of [`canPerformMultiplePasses`](./canperformmultiplepasses.md) is [`false`](../../Swift/false.md), the value of [`currentPassDescription`](./currentpassdescription.md) immediately becomes `nil` after calling this method.

> ❗ **Important**:  Before calling this method, you must add the input to an asset writer and call the writer’s [`startWriting()`](../avassetwriter/startwriting%28%29.md) method.

## See Also

### Performing multiple-pass encoding
- [var canPerformMultiplePasses: Bool](./canperformmultiplepasses.md)
  A Boolean value that indicates whether the input may perform multiple passes over appended media data.
- [var currentPassDescription: AVAssetWriterInputPassDescription?](./currentpassdescription.md)
  An object that describes the requirements for the current pass.
- [class AVAssetWriterInputPassDescription](../avassetwriterinputpassdescription.md)
  An object that defines the interface to query for the requirements of the current pass.
- [var performsMultiPassEncodingIfSupported: Bool](./performsmultipassencodingifsupported.md)
  A Boolean value that indicates whether the input attempts to encode the source media data using multiple passes.
- [func respondToEachPassDescription(on: dispatch_queue_t, using: () -> Void)](./respondtoeachpassdescription%28on,using%29.md)
  Tells the input to invoke a callback whenever it begins a new pass.
- [AVAssetWriterInput.MultiPassController](./multipasscontroller.md)
  Provides an interface to receive an async sequence of pass descriptions for the writer input receiver, if multi-pass is supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/markcurrentpassasfinished())*