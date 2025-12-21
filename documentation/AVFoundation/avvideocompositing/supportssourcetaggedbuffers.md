# supportsSourceTaggedBuffers

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
optional var supportsSourceTaggedBuffers: Bool { get }
```

## See Also

- [var sourcePixelBufferAttributes: [String : any Sendable]?](avvideocompositing/sourcepixelbufferattributes.md)
  The pixel buffer attributes that the compositor accepts for source frames.
- [var requiredPixelBufferAttributesForRenderContext: [String : any Sendable]](avvideocompositing/requiredpixelbufferattributesforrendercontext.md)
  The pixel buffer attributes that the compositor requires for pixel buffers that it creates.
- [var supportsHDRSourceFrames: Bool](avvideocompositing/supportshdrsourceframes.md)
  A Boolean value that indicates whether the compositor handles source frames that contain high dynamic range (HDR) properties.
- [var supportsWideColorSourceFrames: Bool](avvideocompositing/supportswidecolorsourceframes.md)
  A Boolean value that indicates whether the compositor handles source frames that contains wide color properties.
- [var canConformColorOfSourceFrames: Bool](avvideocompositing/canconformcolorofsourceframes.md)
  A Boolean value that indicates whether the compositor conforms the color space of source frames to the composition color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositing/supportssourcetaggedbuffers)*