# respondToEachPassDescription(on:using:)

**Framework**: AVFoundation  
**Kind**: method

Tells the input to invoke a callback whenever it begins a new pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func respondToEachPassDescription(on queue: dispatch_queue_t, using block: @escaping () -> Void)
```

#### Discussion

A typical implemementation of the callback block performs the following steps:

1. Gets the value of the [`currentPassDescription`](avassetwriterinput/currentpassdescription.md) property and configures media data source accordingly.
2. Calls the [`requestMediaDataWhenReady(on:using:)`](avassetwriterinput/requestmediadatawhenready(on:using:).md) method to begin appending data for the current pass.

After you’ve appended all media data for the current pass, call the [`markCurrentPassAsFinished()`](avassetwriterinput/markcurrentpassasfinished().md) method have the system determine whether to perform another pass. If it performs an additional pass the system invokes the callback to begin the next pass. When it determines that it requires no additional passes, the system invokes the callback one final time so the client can invoke [`markAsFinished()`](avassetwriterinput/markasfinished().md) in response to the value of [`currentPassDescription`](avassetwriterinput/currentpassdescription.md) becoming `nil`.

> ❗ **Important**:  Before calling this method, you must add the input to an asset writer and call the writer’s [`startWriting()`](avassetwriter/startwriting().md) method.

## Parameters

- `queue`: The queue on which to invoke the callback.
- `block`: A callback the input invokes at the beginning of each pass.

## See Also

- [var canPerformMultiplePasses: Bool](avassetwriterinput/canperformmultiplepasses.md)
  A Boolean value that indicates whether the input may perform multiple passes over appended media data.
- [var currentPassDescription: AVAssetWriterInputPassDescription?](avassetwriterinput/currentpassdescription.md)
  An object that describes the requirements for the current pass.
- [class AVAssetWriterInputPassDescription](avassetwriterinputpassdescription.md)
  An object that defines the interface to query for the requirements of the current pass.
- [func markCurrentPassAsFinished()](avassetwriterinput/markcurrentpassasfinished.md)
  Tells the input to analyze the appended media to determine whether it can improve the results by reencoding certain segments.
- [var performsMultiPassEncodingIfSupported: Bool](avassetwriterinput/performsmultipassencodingifsupported.md)
  A Boolean value that indicates whether the input attempts to encode the source media data using multiple passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/respondtoeachpassdescription(on:using:))*