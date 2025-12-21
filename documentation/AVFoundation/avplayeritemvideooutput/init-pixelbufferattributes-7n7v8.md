# init(pixelBufferAttributes:)

**Framework**: AVFoundation  
**Kind**: init

Creates a video output object using the specified pixel buffer attributes.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(pixelBufferAttributes: [String : any Sendable]? = nil)
```

#### Return Value

An initialized video output object.

## Parameters

- `pixelBufferAttributes`: The pixel buffer attributes required for video output. For a list of pixel buffer attributes you can include in this dictionary, see the   header file in the Core Video framework.

## See Also

- [convenience init(pixelBufferAttributes: CVPixelBufferAttributes)](avplayeritemvideooutput/init(pixelbufferattributes:)-18izh.md)
  Initializes an instance of AVPlayerItemVideoOutput, using the specified pixel buffer attributes, for video image output
- [init(outputSettings: [String : any Sendable]?)](avplayeritemvideooutput/init(outputsettings:).md)
  Creates a video output object initialized with the specified output settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/init(pixelbufferattributes:)-7n7v8)*