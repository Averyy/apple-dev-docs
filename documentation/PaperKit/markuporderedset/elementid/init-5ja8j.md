# init(_:)

**Framework**: PaperKit  
**Kind**: init

Creates a new element ID from a markup ID.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init<T>(_ id: MarkupID<T>) where T : Markup
```

#### Discussion

Supports all PaperKit types, will `fatalError` if used for an unsupported type.

## See Also

- [init(UUID)](markuporderedset/elementid/init(_:)-5ykum.md)
  Creates a new element ID from a stroke UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuporderedset/elementid/init(_:)-5ja8j)*