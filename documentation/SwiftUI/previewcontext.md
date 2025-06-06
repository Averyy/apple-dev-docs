# PreviewContext

**Framework**: SwiftUI  
**Kind**: protocol

A context type for use with a preview.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
protocol PreviewContext
```

## Topics

### Accessing a preview context
- [subscript<Key>(Key.Type) -> Key.Value](previewcontext/subscript(_:).md)
  Returns the context’s value for a key, or a the key’s default value if the context doesn’t define a value for the key.

## See Also

- [func previewContext<C>(C) -> some View](view/previewcontext(_:).md)
  Declares a context for the preview.
- [protocol PreviewContextKey](previewcontextkey.md)
  A key type for a preview context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewcontext)*