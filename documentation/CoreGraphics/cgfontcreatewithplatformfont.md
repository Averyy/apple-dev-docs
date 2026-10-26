# CGFontCreateWithPlatformFont

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Creates a font object from an Apple Type Services (ATS) font.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use Core Text, documented in [Core Text](../CoreText/CoreText.md), instead.

## Declaration

```c
extern CGFontRefCGFontCreateWithPlatformFont(void *platformFontReference);
```

#### Return Value

The font object, or `NULL` if the platform font could not be located. In Objective-C, you’re responsible for releasing this object using [`CGFontRelease`](./cgfontrelease.md).

#### Discussion

Before drawing text in a Core Graphics context, you must set the font in the current graphics state. For ATS Fonts, call this function to create a font, and pass it to [`setFont(_:)`](./cgcontext/setfont%28_%29.md).

##### Special Considerations

This function is deprecated because it takes a pointer to an `ATSFontRef` object—itself deprecated—and is used almost solely by QuickDraw-based applications. There’s no direct one-to-one replacement for the function. Clients using ATSUI and QuickDraw should move to Core Text and Core Graphics instead.

## Parameters

- `platformFontReference`: A generic pointer to a font object. The font should be of a type appropriate to the platform on which your program is running. For macOS, you should pass a pointer to an ATS font.

## See Also

### Creating Font Objects
- [init?(CGDataProvider)](./cgfont/init%28_%29-9aour.md)
  Creates a font object from data supplied from a data provider.
- [init?(CFString)](./cgfont/init%28_%29-1p4b.md)
  Creates a font object corresponding to the font specified by a PostScript or full name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfontcreatewithplatformfont)*