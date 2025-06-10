# scaled(by:)

**Framework**: SwiftUI  
**Kind**: method

Scales the point size of the font.

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
func scaled(by factor: CGFloat) -> Font
```

#### Discussion

Calls to scale are multiplicative, based on the size of the resolved font. For example,

```swift
Font.body
    .scaled(by: 2)
    .bold()
    .scaled(by: 3)
```

results in a bold body font 6x its usual size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/scaled(by:))*