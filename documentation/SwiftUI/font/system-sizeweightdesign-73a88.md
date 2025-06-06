# system(size:weight:design:)

**Framework**: SwiftUI  
**Kind**: method

Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static func system(size: CGFloat, weight: Font.Weight = .regular, design: Font.Design = .default) -> Font
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

If you want to use the default [`Font.Weight`](font/weight.md) ([`regular`](font/weight/regular.md)), you don’t need to specify the `weight` in the method. The following example styles the text as 17 point [`regular`](font/weight/regular.md), and uses a [`Font.Design.rounded`](font/design/rounded.md) system font:

```swift
Text("Hello").font(.system(size: 17, design: .rounded))
```

## See Also

- [static func system(Font.TextStyle, design: Font.Design) -> Font](font/system(_:design:).md)
  Gets a system font with the given text style and design.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/system(size:weight:design:)-73a88)*