# EmptyContent

**Framework**: SwiftUI  
**Kind**: typealias

Content which contains nothing.

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
typealias EmptyContent = EmptyView
```

#### Discussion

You will rarely, if ever, need to create an `EmptyContent` directly. Instead, `EmptyContent` represents the absence of content.

This type should be conformed to builder DSL protocols to represent empty content in that DSL.

DSLs should use `EmptyContent` in situations where a content type defines one or more children with generic parameters, and allows the child content to be absent. When absent, the child content’s type in the generic type parameter is `EmptyContent`. `ContentBuilder` also returns `EmptyContent` from `buildBlock()`.

`EmptyContent` defines a `body` property of type `Never` to improve the ergonomics of conforming to multiple DSL protocols, which should all use `Never` as the universal “primitive body” type.

## See Also

- [struct TupleContent](tuplecontent.md)
  Content created from a tuple of content to be treated as siblings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/emptycontent)*