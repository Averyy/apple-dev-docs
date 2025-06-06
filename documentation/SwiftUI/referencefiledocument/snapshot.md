# Snapshot

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Required**: Yes

A type that represents the document’s stored content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
associatedtype Snapshot
```

#### Discussion

Define this type to represent all the data that your document stores. When someone issues a Save command, SwiftUI asks your document for a value of this type by calling the document’s [`snapshot(contentType:)`](referencefiledocument/snapshot(contenttype:).md) method. SwiftUI sends the snapshot that you provide to the document’s [`fileWrapper(snapshot:configuration:)`](referencefiledocument/filewrapper(snapshot:configuration:).md) method, where you serialize the contents of the snapshot into a file wrapper.

## See Also

- [func snapshot(contentType: UTType) throws -> Self.Snapshot](referencefiledocument/snapshot(contenttype:).md)
  Creates a snapshot that represents the current state of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/referencefiledocument/snapshot)*