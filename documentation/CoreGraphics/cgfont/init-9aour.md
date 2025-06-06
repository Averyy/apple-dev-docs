# init(_:)

**Framework**: Core Graphics  
**Kind**: init

Creates a font object from data supplied from a data provider.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(_ provider: CGDataProvider)
```

#### Return Value

The font object or `NULL` if the font can’t be created. In Objective-C, you’re responsible for releasing this object using [`CGFontRelease`](cgfontrelease.md).

#### Discussion

Before drawing text in a Core Graphics context, you must set the font in the current graphics state by calling the function [`setFontSize(_:)`](cgcontext/setfontsize(_:).md).

## Parameters

- `provider`: A data provider.

## See Also

- [init?(CFString)](cgfont/init(_:)-1p4b.md)
  Creates a font object corresponding to the font specified by a PostScript or full name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfont/init(_:)-9aour)*