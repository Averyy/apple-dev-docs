# supportsWideColorSourceFrames

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the compositor handles source frames that contains wide color properties.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional var supportsWideColorSourceFrames: Bool { get }
```

## Mentions

- [Tagging Media with Video Color Information](tagging-media-with-video-color-information.md)

## See Also

- [var sourcePixelBufferAttributes: [String : any Sendable]?](avvideocompositing/sourcepixelbufferattributes.md)
  The pixel buffer attributes that the compositor accepts for source frames.
- [var requiredPixelBufferAttributesForRenderContext: [String : any Sendable]](avvideocompositing/requiredpixelbufferattributesforrendercontext.md)
  The pixel buffer attributes that the compositor requires for pixel buffers that it creates.
- [var supportsHDRSourceFrames: Bool](avvideocompositing/supportshdrsourceframes.md)
  A Boolean value that indicates whether the compositor handles source frames that contain high dynamic range (HDR) properties.
- [var canConformColorOfSourceFrames: Bool](avvideocompositing/canconformcolorofsourceframes.md)
  A Boolean value that indicates whether the compositor conforms the color space of source frames to the composition color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositing/supportswidecolorsourceframes)*