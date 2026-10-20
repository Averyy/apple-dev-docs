# PreviewContext

**Framework**: SwiftUI  
**Kind**: protocol  
**Role**: Protocol

A context type for use with a preview.

**Availability**:
- iOS 14.0+ - Deprecated in 27.0
- iPadOS 14.0+ - Deprecated in 27.0
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 14.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 7.0+ - Deprecated in 27.0

> **Deprecated**: Use [`Preview(_:body:)`](./preview%28_,body%29.md) with a WidgetKit timeline provider or entries instead.

## Declaration

```swift
protocol PreviewContext
```

## Topics

### Accessing a preview context
- [subscript<Key>(Key.Type) -> Key.Value](./previewcontext/subscript%28_%29.md)
  Returns the context’s value for a key, or a the key’s default value if the context doesn’t define a value for the key.

## See Also

### Setting a context
- [func previewContext<C>(C) -> some View](./view/previewcontext%28_%29.md)
  Declares a context for the preview.
- [protocol PreviewContextKey](./previewcontextkey.md)
  A key type for a preview context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewcontext)*