# contentHeadroom

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var contentHeadroom: Float { get }
```

```c
extern float CGImageGetContentHeadroom(CGImageRef image);
```

## See Also

### Adopting high dynamic range (HDR)
- [Enhancing high dynamic range image rendering](../adopting-advancements-in-hdr-image-rendering.md)
  Improve your app’s High Dynamic Range (HDR) image support with metadata.
- [var calculatedContentHeadroom: Float](./calculatedcontentheadroom.md)
- [var contentAverageLightLevel: Float](./contentaveragelightlevel.md)
- [var calculatedContentAverageLightLevel: Float](./calculatedcontentaveragelightlevel.md)
- [func copy(contentAverageLightLevel: Float) -> CGImage?](./copy%28contentaveragelightlevel%29.md)
- [func copyWithCalculatedHDRStats() -> CGImage?](./copywithcalculatedhdrstats%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgimage/contentheadroom)*