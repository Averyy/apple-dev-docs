# bold(_:)

**Framework**: SwiftUI  
**Kind**: method

Adds or removes bold or emphasized styling on the font.

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
func bold(_ isActive: Bool) -> Font
```

#### Discussion

For fonts created from text styles, passing `true` could mean applying emphasized styling, which does not necessarily mean the bold weight specifically, so this modifier is not to be confused with [`weight(_:)`](Font/weight(_:).md).

For example:

```swift
Font.body.bold(true)
```

will most likely get you the emphasized version of body text style, which is often in [`semibold`](Font/Weight/semibold.md) weight. While

```swift
Font.body.weight(.bold)
```

will specifically get you the body text style font in the [`bold`](Font/Weight/bold.md) weight.

Using:

```swift
Font.body.bold(false)
```

will remove any emphasized styling from the font returning to its default weight which is most likely but not guaranteed to be 0.0 or [`regular`](font/weight/regular.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/bold(_:))*