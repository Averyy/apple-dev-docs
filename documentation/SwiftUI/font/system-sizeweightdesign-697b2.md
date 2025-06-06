# system(size:weight:design:)

**Framework**: SwiftUI  
**Kind**: method

Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.

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
static func system(size: CGFloat, weight: Font.Weight? = nil, design: Font.Design? = nil) -> Font
```

#### Discussion

Use this function to create a system font by specifying the size and weight, and a type design together. The following styles the system font as 17 point, [`semibold`](font/weight/semibold.md) text:

```swift
Text("Hello").font(.system(size: 17, weight: .semibold))
```

While the following styles the text as 17 point [`bold`](font/weight/bold.md), and applies a `serif` [`Font.Design`](font/design.md) to the system font:

```swift
Text("Hello").font(.system(size: 17, weight: .bold, design: .serif))
```

Both `weight` and `design` can be optional. When you do not provide a `weight` or `design`, the system can pick one based on the current context, which may not be [`regular`](font/weight/regular.md) or [`Font.Design.default`](font/design/default.md) in certain context. The following example styles the text as 17 point system font using [`Font.Design.rounded`](font/design/rounded.md) design, while its weight can depend on the current context:

```swift
Text("Hello").font(.system(size: 17, design: .rounded))
```

## See Also

- [static func system(Font.TextStyle, design: Font.Design?, weight: Font.Weight?) -> Font](font/system(_:design:weight:).md)
  Gets a system font that uses the specified style, design, and weight.
- [Font.Design](font/design.md)
  A design to use for fonts.
- [Font.TextStyle](font/textstyle.md)
  A dynamic text style to use for fonts.
- [struct Weight](font/weight.md)
  A weight to use for fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/system(size:weight:design:)-697b2)*