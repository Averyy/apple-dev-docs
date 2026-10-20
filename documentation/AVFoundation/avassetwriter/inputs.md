# inputs

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The inputs an asset writer contains.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var inputs: [AVAssetWriterInput] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVAssetWriterInput *> * inputs;
```

## See Also

### Configuring inputs
- [var availableMediaTypes: [AVMediaType]](./availablemediatypes.md)
  The media types the asset writer supports adding as inputs.
- [func canApply(outputSettings: [String : Any]?, forMediaType: AVMediaType) -> Bool](./canapply%28outputsettings,formediatype%29.md)
  Determines whether the output file format supports the output settings for a specific media type.
- [func canAdd(AVAssetWriterInput) -> Bool](./canadd%28_%29-6al7j.md)
  Determines whether the asset writer supports adding the input.
- [func add(AVAssetWriterInput)](./add%28_%29-4c4d0.md)
  Adds an input to an asset writer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/inputs)*