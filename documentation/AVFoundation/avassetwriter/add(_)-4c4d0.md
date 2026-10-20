# add(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Adds an input to an asset writer.

**Availability**:
- iOS 4.1+ - Deprecated in 27.0
- iPadOS 4.1+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.7+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use the appropriate AVAssetWriter.inputReceiver(for:...) overload for your input and optional adaptor instead

## Declaration

```swift
func add(_ input: AVAssetWriterInput)
```

```objc
- (void) addInput:(AVAssetWriterInput *) input;
```

#### Discussion

You can’t add inputs after asset writing begins.

## Parameters

- `input`: A compatible asset writer input to add.

## See Also

### Configuring inputs
- [var inputs: [AVAssetWriterInput]](./inputs.md)
  The inputs an asset writer contains.
- [var availableMediaTypes: [AVMediaType]](./availablemediatypes.md)
  The media types the asset writer supports adding as inputs.
- [func canApply(outputSettings: [String : Any]?, forMediaType: AVMediaType) -> Bool](./canapply%28outputsettings,formediatype%29.md)
  Determines whether the output file format supports the output settings for a specific media type.
- [func canAdd(AVAssetWriterInput) -> Bool](./canadd%28_%29-6al7j.md)
  Determines whether the asset writer supports adding the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/add(_:)-4c4d0)*