# sourcePixelBufferAttributes

**Framework**: AVFoundation  
**Kind**: property  
**Required**: Yes

The pixel buffer attributes that the compositor accepts for source frames.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sourcePixelBufferAttributes: [String : any Sendable]? { get }
```

#### Discussion

The property is required to provide a [`kCVPixelBufferPixelFormatTypeKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferPixelFormatTypeKey) key in the dictionary, along with attributes for which the compositor needs specific values to work properly. Omitted attributes will be supplied by the composition engine to allow for the best performance. If the attribute [`kCVPixelBufferPixelFormatTypeKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferPixelFormatTypeKey) key is not in the dictionary an exception will be raised. The value of the [`kCVPixelBufferPixelFormatTypeKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferPixelFormatTypeKey) is an array of `kCVPixelFormatType_*` constants as defined in Pixel_Format_Types.

If the custom compositor is meant to be used with an [`AVVideoCompositionCoreAnimationTool`](avvideocompositioncoreanimationtool.md) created using the [`init(additionalLayer:asTrackID:)`](avvideocompositioncoreanimationtool/init(additionallayer:astrackid:).md) method, [`kCVPixelFormatType_32BGRA`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_32BGRA) should be included as one of the supported pixel format types.

Missing attributes will be set by the composition engine to values allowing the best performance.

This property is queried once before any composition request is sent to the compositor. Changing source buffer attributes afterwards is not supported.

## See Also

- [var requiredPixelBufferAttributesForRenderContext: [String : any Sendable]](avvideocompositing/requiredpixelbufferattributesforrendercontext.md)
  The pixel buffer attributes that the compositor requires for pixel buffers that it creates.
- [var supportsHDRSourceFrames: Bool](avvideocompositing/supportshdrsourceframes.md)
  A Boolean value that indicates whether the compositor handles source frames that contain high dynamic range (HDR) properties.
- [var supportsWideColorSourceFrames: Bool](avvideocompositing/supportswidecolorsourceframes.md)
  A Boolean value that indicates whether the compositor handles source frames that contains wide color properties.
- [var canConformColorOfSourceFrames: Bool](avvideocompositing/canconformcolorofsourceframes.md)
  A Boolean value that indicates whether the compositor conforms the color space of source frames to the composition color space.
- [var supportsSourceTaggedBuffers: Bool](avvideocompositing/supportssourcetaggedbuffers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositing/sourcepixelbufferattributes)*