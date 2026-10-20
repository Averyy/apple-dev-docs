# canApply(outputSettings:forMediaType:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) canApplyOutputSettings:(NSDictionary<NSString *,id> *) outputSettings forMediaType:(AVMediaType) mediaType;
```

#### Return Value

[`true`](../../Swift/true.md) if the format supports the output settings; otherwise, [`false`](../../Swift/false.md).

#### Discussion

Use this method to determine the compatibility of output settings for a particular media type. For example, video compression settings that specify H.264 compression aren’t compatible with file formats that don’t contain H.264-compressed video.

## Parameters

- `outputSettings`: The output settings to validate.
- `mediaType`: The media type to validate the output settings for.

## See Also

### Configuring inputs
- [var inputs: [AVAssetWriterInput]](./inputs.md)
  The inputs an asset writer contains.
- [var availableMediaTypes: [AVMediaType]](./availablemediatypes.md)
  The media types the asset writer supports adding as inputs.
- [func canAdd(AVAssetWriterInput) -> Bool](./canadd%28_%29-6al7j.md)
  Determines whether the asset writer supports adding the input.
- [func add(AVAssetWriterInput)](./add%28_%29-4c4d0.md)
  Adds an input to an asset writer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/canapply(outputsettings:formediatype:))*