# writableContentTypes

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The file types that the document supports saving or exporting to.

**Availability**:
- iOS 14.0+ - Deprecated in 27.3
- iPadOS 14.0+ - Deprecated in 27.3
- Mac Catalyst 14.0+ - Deprecated in 27.3
- macOS 11.0+ - Deprecated in 27.3
- visionOS 1.0+ - Deprecated in 27.3

> **Deprecated**: Conform your type to Document instead.

## Declaration

```swift
static var writableContentTypes: [UTType] { get }
```

## Discussion

By default, SwiftUI assumes that your document reads and writes the same set of content types. Only define this property if you need to indicate a different set of types for writing files. Otherwise, the default implementation of this property returns the list that you specify in your implementation of [`readableContentTypes`](./readablecontenttypes.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filedocument/writablecontenttypes-289b3)*