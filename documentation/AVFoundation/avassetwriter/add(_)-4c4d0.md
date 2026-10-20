# add(_:)

**Framework**: AVFoundation  
**Kind**: method

Adds an input to an asset writer.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func add(_ input: AVAssetWriterInput)
```

#### Discussion

You can’t add inputs after asset writing begins.

## Parameters

- `input`: A compatible asset writer input to add.

## See Also

- [var inputs: [AVAssetWriterInput]](avassetwriter/inputs.md)
  The inputs an asset writer contains.
- [var availableMediaTypes: [AVMediaType]](avassetwriter/availablemediatypes.md)
  The media types the asset writer supports adding as inputs.
- [func canApply(outputSettings: [String : Any]?, forMediaType: AVMediaType) -> Bool](avassetwriter/canapply(outputsettings:formediatype:).md)
  Determines whether the output file format supports the output settings for a specific media type.
- [func canAdd(AVAssetWriterInput) -> Bool](avassetwriter/canadd(_:)-6al7j.md)
  Determines whether the asset writer supports adding the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/add(_:)-4c4d0)*