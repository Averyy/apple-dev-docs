# canAdd(_:)

**Framework**: AVFoundation  
**Kind**: method

Determines whether the asset writer supports adding the input.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func canAdd(_ input: AVAssetWriterInput) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if you can add the input to the asset writer; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `input`: The asset writer input to add.

## See Also

- [var inputs: [AVAssetWriterInput]](avassetwriter/inputs.md)
  The inputs an asset writer contains.
- [var availableMediaTypes: [AVMediaType]](avassetwriter/availablemediatypes.md)
  The media types the asset writer supports adding as inputs.
- [func canApply(outputSettings: [String : Any]?, forMediaType: AVMediaType) -> Bool](avassetwriter/canapply(outputsettings:formediatype:).md)
  Determines whether the output file format supports the output settings for a specific media type.
- [func add(AVAssetWriterInput)](avassetwriter/add(_:)-4c4d0.md)
  Adds an input to an asset writer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/canadd(_:)-6al7j)*