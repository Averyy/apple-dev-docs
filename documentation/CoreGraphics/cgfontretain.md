# CGFontRetain

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Increments the retain count of a font.

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
extern CGFontRefCGFontRetain(CGFontRef font);
```

#### Return Value

The same font you specified in the `font` parameter.

#### Discussion

This function is equivalent to [`CFRetain`](../CoreFoundation/cfretain.md), except that it does not cause an error if the `font` parameter is `NULL`.

## Parameters

- `font`: The font to retain.

## See Also

### Retaining and Releasing a CGFont Object
- [CGFontRelease](./cgfontrelease.md)
  Decrements the retain count of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfontretain)*