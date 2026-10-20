# copy(contentAverageLightLevel:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

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
func copy(contentAverageLightLevel avll: Float) -> CGImage?
```

```c
extern CGImageRefCGImageCreateCopyWithContentAverageLightLevel(CGImageRef image, float avll);
```

## See Also

### Adopting high dynamic range (HDR)
- [Enhancing high dynamic range image rendering](../adopting-advancements-in-hdr-image-rendering.md)
  Improve your app’s High Dynamic Range (HDR) image support with metadata.
- [var contentHeadroom: Float](./contentheadroom.md)
- [var calculatedContentHeadroom: Float](./calculatedcontentheadroom.md)
- [var contentAverageLightLevel: Float](./contentaveragelightlevel.md)
- [var calculatedContentAverageLightLevel: Float](./calculatedcontentaveragelightlevel.md)
- [func copyWithCalculatedHDRStats() -> CGImage?](./copywithcalculatedhdrstats%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgimage/copy(contentaveragelightlevel:))*