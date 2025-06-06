# supportsHDRSourceFrames

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the compositor handles source frames that contain high dynamic range (HDR) properties.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional var supportsHDRSourceFrames: Bool { get }
```

## See Also

- [var sourcePixelBufferAttributes: [String : any Sendable]?](avvideocompositing/sourcepixelbufferattributes.md)
  The pixel buffer attributes that the compositor accepts for source frames.
- [var requiredPixelBufferAttributesForRenderContext: [String : any Sendable]](avvideocompositing/requiredpixelbufferattributesforrendercontext.md)
  The pixel buffer attributes that the compositor requires for pixel buffers that it creates.
- [var supportsWideColorSourceFrames: Bool](avvideocompositing/supportswidecolorsourceframes.md)
  A Boolean value that indicates whether the compositor handles source frames that contains wide color properties.
- [var canConformColorOfSourceFrames: Bool](avvideocompositing/canconformcolorofsourceframes.md)
  A Boolean value that indicates whether the compositor conforms the color space of source frames to the composition color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositing/supportshdrsourceframes)*