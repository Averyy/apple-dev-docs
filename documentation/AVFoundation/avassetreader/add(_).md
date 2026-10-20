# add(_:)

**Framework**: AVFoundation  
**Kind**: method

Adds an output to the reader.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func add(_ output: AVAssetReaderOutput)
```

#### Discussion

Add outputs to read from one or more tracks of an asset. You can only add outputs that retrieve media data from the asset that you associate with the asset reader.

You can’t add an output after you start reading.

## Parameters

- `output`: The asset reader output to add.

## See Also

- [func canAdd(AVAssetReaderOutput) -> Bool](avassetreader/canadd(_:).md)
  Determines whether you can add the output to the asset reader.
- [var outputs: [AVAssetReaderOutput]](avassetreader/outputs.md)
  The outputs from which you read media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/add(_:))*