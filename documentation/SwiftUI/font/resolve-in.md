# resolve(in:)

**Framework**: SwiftUI  
**Kind**: method

Evaluates this font to a resolved font given the current context.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func resolve(in context: Font.Context) -> Font.Resolved
```

#### Discussion

The system resolves a font’s value at the time it uses the font in a given environment’s context because [`Font`](font.md) is a late-binding token.

> **Note**: [`fontResolutionContext`](environmentvalues/fontresolutioncontext.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/resolve(in:))*