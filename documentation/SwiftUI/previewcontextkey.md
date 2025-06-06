# PreviewContextKey

**Framework**: SwiftUI  
**Kind**: protocol

A key type for a preview context.

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
protocol PreviewContextKey
```

#### Overview

The default value is `nil`.

## Topics

### Setting a default
- [static var defaultValue: Self.Value](previewcontextkey/defaultvalue.md)
  The default value of the key.
- [associatedtype Value](previewcontextkey/value.md)
  The type of the value returned by the key.

## See Also

- [func previewContext<C>(C) -> some View](view/previewcontext(_:).md)
  Declares a context for the preview.
- [protocol PreviewContext](previewcontext.md)
  A context type for use with a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewcontextkey)*