# init(pixelBufferAttributes:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a video output object using the specified pixel buffer attributes.

**Availability**:
- iOS 6.0+ - Deprecated in 27.0
- iPadOS 6.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.8+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use init(pixelBufferAttributes: CVPixelBuffer.Attributes) instead

## Declaration

```swift
init(pixelBufferAttributes: [String : any Sendable]? = nil)
```

```objc
- (instancetype) initWithPixelBufferAttributes:(NSDictionary<NSString *,id> *) pixelBufferAttributes;
```

## Return Value

An initialized video output object.

## Parameters

- `pixelBufferAttributes`: The pixel buffer attributes required for video output. For a list of pixel buffer attributes you can include in this dictionary, see the `CVPixelBuffer.h` header file in the Core Video framework.

## See Also

### Creating a video output
- [convenience init(pixelBufferAttributes: CVPixelBufferAttributes)](./init%28pixelbufferattributes%29-18izh.md)
  Initializes an instance of AVPlayerItemVideoOutput, using the specified pixel buffer attributes, for video image output
- [init(outputSettings: [String : any Sendable]?)](./init%28outputsettings%29.md)
  Creates a video output object initialized with the specified output settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/init(pixelbufferattributes:)-7n7v8)*