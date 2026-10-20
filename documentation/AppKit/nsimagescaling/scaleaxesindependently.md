# NSImageScaling.scaleAxesIndependently

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Scale each dimension to exactly fit destination.

**Availability**:
- macOS 10.5+

## Declaration

```swift
case scaleAxesIndependently
```

```c
NSImageScaleAxesIndependently
```

#### Discussion

This setting does not preserve the aspect ratio of the image.

## See Also

### Constants
- [NSImageScaling.scaleProportionallyDown](./scaleproportionallydown.md)
  If it is too large for the destination, scale the image down while preserving the aspect ratio.
- [NSImageScaling.scaleNone](./scalenone.md)
  Do not scale the image.
- [NSImageScaling.scaleProportionallyUpOrDown](./scaleproportionallyupordown.md)
  Scale the image to its maximum possible dimensions while both staying within the destination area and preserving its aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagescaling/scaleaxesindependently)*