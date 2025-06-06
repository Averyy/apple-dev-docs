# buildExpression(_:)

**Framework**: SwiftUI  
**Kind**: method

Builds an expression within the builder.

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
static func buildExpression<Content>(_ content: Content) -> Content where Content : View
```

## See Also

- [static func buildBlock() -> EmptyView](viewbuilder/buildblock.md)
  Builds an empty view from a block containing no statements.
- [static buildBlock(_:)](viewbuilder/buildblock(_:).md)
  Passes a single view written as a child view through unmodified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildexpression(_:))*