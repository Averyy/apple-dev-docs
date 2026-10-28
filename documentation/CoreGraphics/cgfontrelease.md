# CGFontRelease

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Decrements the retain count of a font.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGFontRelease(CGFontRef font);
```

## Discussion

This function is equivalent to [`CFRelease`](../CoreFoundation/cfrelease.md), except that it does not cause an error if the `font` parameter is `NULL`.

## Parameters

- `font`: The font to release.

## See Also

### Retaining and Releasing a CGFont Object
- [CGFontRetain](./cgfontretain.md)
  Increments the retain count of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfontrelease)*