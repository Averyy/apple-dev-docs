# previewContext(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Declares a context for the preview.

**Availability**:
- iOS 14.0+ - Deprecated in 27.0
- iPadOS 14.0+ - Deprecated in 27.0
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 14.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 7.0+ - Deprecated in 27.0

> **Deprecated**: Use [`Preview(_:body:)`](../preview%28_,body%29.md) with a WidgetKit timeline provider or entries instead.

## Declaration

```swift
nonisolated
func previewContext<C>(_ value: C) -> some View where C : PreviewContext
```

## Parameters

- `value`: The context for the preview; the default is `nil`.

## See Also

### Setting a context
- [protocol PreviewContext](../previewcontext.md)
  A context type for use with a preview.
- [protocol PreviewContextKey](../previewcontextkey.md)
  A key type for a preview context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/previewcontext(_:))*