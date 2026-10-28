# init(id:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a window group with an identifier.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0 (renamed: init(id:makeContent:))
- iPadOS 14.0+ - Deprecated in 18.0 (renamed: init(id:makeContent:))
- Mac Catalyst 14.0+ - Deprecated in 18.0 (renamed: init(id:makeContent:))
- macOS 11.0+ - Deprecated in 15.0 (renamed: init(id:makeContent:))
- tvOS 14.0+ - Deprecated in 18.0 (renamed: init(id:makeContent:))
- visionOS 1.0+ - Deprecated in 2.0 (renamed: init(id:makeContent:))
- watchOS 7.0+ - Deprecated in 11.0 (renamed: init(id:makeContent:))

> **Deprecated**: Use the initializer which takes an escaping content builder instead.

## Declaration

```swift
nonisolated
init(id: String, @ContentBuilder content: () -> Content)
```

## Discussion

The window group uses the given view as a template to form the content of each window in the group.

## Parameters

- `id`: A string that uniquely identifies the window group. Identifiers must be unique among the window groups in your app.
- `content`: A closure that creates the content for each instance of the group.

## See Also

### Deprecated
- [init(content: () -> Content)](./init%28content%29.md)
  Creates a window group.
- [init(_:content:)](./init%28_,content%29.md)
  Creates a window group with a text view title.
- [init(_:id:content:)](./init%28_,id,content%29.md)
  Creates a window group with a text view title and an identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowgroup/init(id:content:))*