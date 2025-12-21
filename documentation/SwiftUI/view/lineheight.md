# lineHeight(_:)

**Framework**: SwiftUI  
**Kind**: method

A modifier for the default line height in the view hierarchy.

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
nonisolated
func lineHeight(_ lineHeight: AttributedString.LineHeight?) -> some View
```

#### Discussion

The default value is `nil`. In that case, SwiftUI automatically chooses an appropriate line height setting for each context.

> **Note**: [`lineHeight`](environmentvalues/lineheight.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/lineheight(_:))*