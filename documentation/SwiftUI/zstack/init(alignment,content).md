# init(alignment:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance with the given alignment.

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
nonisolated
init(alignment: Alignment = .center, @ContentBuilder content: () -> Content)
```

## Parameters

- `alignment`: The guide for aligning the subviews in this stack on both the x- and y-axes.
- `content`: A content builder that creates the content of this stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/zstack/init(alignment:content:))*