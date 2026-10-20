# system(size:weight:design:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`system(size:weight:design:)`](./system%28size,weight,design%29-697b2.md) instead.

## Declaration

```swift
static func system(size: CGFloat, weight: Font.Weight = .regular, design: Font.Design = .default) -> Font
```

**Other overloads**:

```swift
static func system(size: CGFloat, weight: Font.Weight? = nil, design: Font.Design? = nil) -> Font
```

#### Discussion

Use this function to create a system font by specifying the size and weight, and a type design together. The following styles the system font as 17 point, [`semibold`](./weight/semibold.md) text:

```swift
Text("Hello").font(.system(size: 17, weight: .semibold))
```

While the following styles the text as 17 point [`bold`](./weight/bold.md), and applies a `serif` [`Font.Design`](./design.md) to the system font:

```swift
Text("Hello").font(.system(size: 17, weight: .bold, design: .serif))
```

If you want to use the default [`Font.Weight`](./weight.md) ([`regular`](./weight/regular.md)), you don’t need to specify the `weight` in the method. The following example styles the text as 17 point [`regular`](./weight/regular.md), and uses a [`Font.Design.rounded`](./design/rounded.md) system font:

```swift
Text("Hello").font(.system(size: 17, design: .rounded))
```

## See Also

### Getting system fonts
- [static func system(Font.TextStyle, design: Font.Design?, weight: Font.Weight?) -> Font](./system%28_,design,weight%29.md)
  Gets a system font that uses the specified style, design, and weight.
- [Font.Design](./design.md)
  A design to use for fonts.
- [Font.TextStyle](./textstyle.md)
  A dynamic text style to use for fonts.
- [struct Weight](./weight.md)
  A weight to use for fonts.
- [static func system(size: CGFloat, weight: Font.Weight?, design: Font.Design?) -> Font](./system%28size,weight,design%29-697b2.md)
  Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.
- [static func system(Font.TextStyle, design: Font.Design) -> Font](./system%28_,design%29.md)
  Gets a system font with the given text style and design.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/system(size:weight:design:)-73a88)*