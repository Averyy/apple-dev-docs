# canApply(outputSettings:forMediaType:)

**Framework**: AVFoundation  
**Kind**: method

Determines whether the output file format supports the output settings for a specific media type.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func canApply(outputSettings: [String : Any]?, forMediaType mediaType: AVMediaType) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the format supports the output settings; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Use this method to determine the compatibility of output settings for a particular media type. For example, video compression settings that specify H.264 compression aren’t compatible with file formats that don’t contain H.264-compressed video.

## Parameters

- `outputSettings`: The output settings to validate.
- `mediaType`: The media type to validate the output settings for.

## See Also

- [var inputs: [AVAssetWriterInput]](avassetwriter/inputs.md)
  The inputs an asset writer contains.
- [var availableMediaTypes: [AVMediaType]](avassetwriter/availablemediatypes.md)
  The media types the asset writer supports adding as inputs.
- [func canAdd(AVAssetWriterInput) -> Bool](avassetwriter/canadd(_:)-6al7j.md)
  Determines whether the asset writer supports adding the input.
- [func add(AVAssetWriterInput)](avassetwriter/add(_:)-4c4d0.md)
  Adds an input to an asset writer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/canapply(outputsettings:formediatype:))*