# add(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Adds an output to the reader.

**Availability**:
- iOS 4.1+ - Deprecated in 27.0
- iPadOS 4.1+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.7+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use the appropriate AVAssetReader.outputProvider(for:...) overload for your output and optional adaptor instead

## Declaration

```swift
func add(_ output: AVAssetReaderOutput)
```

```objc
- (void) addOutput:(AVAssetReaderOutput *) output;
```

#### Discussion

Add outputs to read from one or more tracks of an asset. You can only add outputs that retrieve media data from the asset that you associate with the asset reader.

You can’t add an output after you start reading.

## Parameters

- `output`: The asset reader output to add.

## See Also

### Managing outputs
- [func canAdd(AVAssetReaderOutput) -> Bool](./canadd%28_%29.md)
  Determines whether you can add the output to the asset reader.
- [var outputs: [AVAssetReaderOutput]](./outputs.md)
  The outputs from which you read media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/add(_:))*