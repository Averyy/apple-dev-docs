# PreviewContextKey

**Framework**: SwiftUI  
**Kind**: protocol  
**Role**: Protocol

A key type for a preview context.

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
protocol PreviewContextKey
```

## Overview

The default value is `nil`.

## Topics

### Setting a default
- [static var defaultValue: Self.Value](./previewcontextkey/defaultvalue.md)
  The default value of the key.
- [associatedtype Value](./previewcontextkey/value.md)
  The type of the value returned by the key.

## See Also

### Setting a context
- [func previewContext<C>(C) -> some View](./view/previewcontext%28_%29.md)
  Declares a context for the preview.
- [protocol PreviewContext](./previewcontext.md)
  A context type for use with a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewcontextkey)*