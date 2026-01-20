# cgImage

**Framework**: Core Image  
**Kind**: property

The CoreGraphics image object this image was created from, if applicable.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var cgImage: CGImage? { get }
```

#### Discussion

If this image was created using the [`init(cgImage:)`](ciimage/init(cgimage:).md) or [`init(contentsOf:)`](ciimage/init(contentsof:).md) initializer, this property’s value is the [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) object that provides the image’s underlying image data. Otherwise, this property’s value is `nil`—in this case you can obtain a CoreGraphics image by rendering the image with the [`CIContext`](cicontext.md) [`createCGImage(_:from:)`](cicontext/createcgimage(_:from:).md) method.

## See Also

- [var pixelBuffer: CVPixelBuffer?](ciimage/pixelbuffer.md)
  The CoreVideo pixel buffer this image was created from, if applicable.
- [var depthData: AVDepthData?](ciimage/depthdata.md)
  Depth data associated with the image.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](ciimage/portraiteffectsmatte.md)
  The portrait effects matte associated with the image.
- [var semanticSegmentationMatte: AVSemanticSegmentationMatte?](ciimage/semanticsegmentationmatte.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/cgimage)*