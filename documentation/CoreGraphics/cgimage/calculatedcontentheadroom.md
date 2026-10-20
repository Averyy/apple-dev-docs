# calculatedContentHeadroom

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var calculatedContentHeadroom: Float { get }
```

```c
extern float CGImageCalculateContentHeadroom(CGImageRef image);
```

## See Also

### Adopting high dynamic range (HDR)
- [Enhancing high dynamic range image rendering](../adopting-advancements-in-hdr-image-rendering.md)
  Improve your app’s High Dynamic Range (HDR) image support with metadata.
- [var contentHeadroom: Float](./contentheadroom.md)
- [var contentAverageLightLevel: Float](./contentaveragelightlevel.md)
- [var calculatedContentAverageLightLevel: Float](./calculatedcontentaveragelightlevel.md)
- [func copy(contentAverageLightLevel: Float) -> CGImage?](./copy%28contentaveragelightlevel%29.md)
- [func copyWithCalculatedHDRStats() -> CGImage?](./copywithcalculatedhdrstats%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgimage/calculatedcontentheadroom)*