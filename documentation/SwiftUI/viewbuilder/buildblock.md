# buildBlock(_:)

**Framework**: SwiftUI  
**Kind**: method

Passes a single view written as a child view through unmodified.

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
static func buildBlock<Content>(_ content: Content) -> Content where Content : View
```

#### Discussion

An example of a single view written as a child view is `{ Text("Hello") }`.

## See Also

- [static func buildBlock() -> EmptyView](viewbuilder/buildblock.md)
  Builds an empty view from a block containing no statements.
- [static func buildExpression<Content>(Content) -> Content](viewbuilder/buildexpression(_:).md)
  Builds an expression within the builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildblock(_:))*