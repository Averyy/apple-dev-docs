# buildBlock(_:)

**Framework**: SwiftUI  
**Kind**: method

Passes a single piece of content written as a child view through unmodified.

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
static func buildBlock<Content>(_ content: Content) -> Content
```

#### Discussion

An example of a single item written as child content is `{ Text("Hello") }`.

## See Also

- [static buildBlock()](viewbuilder/buildblock.md)
  Builds an empty content from a block containing no statements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildblock(_:))*