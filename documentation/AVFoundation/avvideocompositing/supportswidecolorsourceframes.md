# supportsWideColorSourceFrames

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) BOOL supportsWideColorSourceFrames;
```

## Mentions

- [Tagging media with video color information](../tagging-media-with-video-color-information.md)

## See Also

### Inspecting processing requirements
- [var sourcePixelBufferAttributes: [String : any Sendable]?](./sourcepixelbufferattributes.md)
  The pixel buffer attributes that the compositor accepts for source frames.
- [var requiredPixelBufferAttributesForRenderContext: [String : any Sendable]](./requiredpixelbufferattributesforrendercontext.md)
  The pixel buffer attributes that the compositor requires for pixel buffers that it creates.
- [var supportsHDRSourceFrames: Bool](./supportshdrsourceframes.md)
  A Boolean value that indicates whether the compositor handles source frames that contain high dynamic range (HDR) properties.
- [var canConformColorOfSourceFrames: Bool](./canconformcolorofsourceframes.md)
  A Boolean value that indicates whether the compositor conforms the color space of source frames to the composition color space.
- [var supportsSourceTaggedBuffers: Bool](./supportssourcetaggedbuffers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositing/supportswidecolorsourceframes)*