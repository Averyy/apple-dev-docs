# canAdd(_:)

**Framework**: AVFoundation  
**Kind**: method

Determines whether you can add the output to the asset reader.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func canAdd(_ output: AVAssetReaderOutput) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if you can add the output; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

You may only add outputs that retrieve media data from the asset that you associate with the asset reader.

## Parameters

- `output`: The asset reader output to test.

## See Also

- [func add(AVAssetReaderOutput)](avassetreader/add(_:).md)
  Adds an output to the reader.
- [var outputs: [AVAssetReaderOutput]](avassetreader/outputs.md)
  The outputs from which you read media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/canadd(_:))*