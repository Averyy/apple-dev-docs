# system(_:design:weight:)

**Framework**: SwiftUI  
**Kind**: method

Gets a system font that uses the specified style, design, and weight.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func system(_ style: Font.TextStyle, design: Font.Design? = nil, weight: Font.Weight? = nil) -> Font
```

#### Discussion

Use this method to create a system font that has the specified properties. The following example creates a system font with the [`Font.TextStyle.body`](font/textstyle/body.md) text style, a [`Font.Design.serif`](font/design/serif.md) design, and a [`bold`](font/weight/bold.md) weight, and applies the font to a [`Text`](text.md) view using the [`font(_:)`](view/font(_:).md) view modifier:

```swift
Text("Hello").font(.system(.body, design: .serif, weight: .bold))
```

The `design` and `weight` parameters are both optional. If you omit either, the system uses a default value for that parameter. The default values are typically [`Font.Design.default`](font/design/default.md) and [`regular`](font/weight/regular.md), respectively, but might vary depending on the context.

## See Also

- [static func system(size: CGFloat, weight: Font.Weight?, design: Font.Design?) -> Font](font/system(size:weight:design:)-697b2.md)
  Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.
- [Font.Design](font/design.md)
  A design to use for fonts.
- [Font.TextStyle](font/textstyle.md)
  A dynamic text style to use for fonts.
- [struct Weight](font/weight.md)
  A weight to use for fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/system(_:design:weight:))*