# Snapshot

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

A type that represents the document’s stored content.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+

> **Deprecated**: Use Document protocol instead.

## Declaration

```swift
associatedtype Snapshot
```

## Discussion

Define this type to represent all the data that your document stores. When someone issues a Save command, SwiftUI asks your document for a value of this type by calling the document’s [`snapshot(contentType:)`](./snapshot%28contenttype%29.md) method. SwiftUI sends the snapshot that you provide to the document’s [`fileWrapper(snapshot:configuration:)`](./filewrapper%28snapshot,configuration%29.md) method, where you serialize the contents of the snapshot into a file wrapper.

## See Also

### Getting a snapshot
- [func snapshot(contentType: UTType) throws -> Self.Snapshot](./snapshot%28contenttype%29.md)
  Creates a snapshot that represents the current state of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/referencefiledocument/snapshot)*