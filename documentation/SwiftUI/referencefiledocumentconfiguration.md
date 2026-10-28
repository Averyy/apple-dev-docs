# ReferenceFileDocumentConfiguration

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The properties of an open reference file document.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+

> **Deprecated**: Use Document protocol and URLDocumentConfiguration instead.

## Declaration

```swift
@MainActor
@preconcurrency struct ReferenceFileDocumentConfiguration<Document> where Document : ReferenceFileDocument
```

## Overview

You receive an instance of this structure when you create a [`DocumentGroup`](./documentgroup.md) with a reference file type. Use it to access the document in your viewer or editor.

## Topics

### Getting and setting the document
- [var document: Document](./referencefiledocumentconfiguration/document.md)
  The current document model.
- [var $document: ObservedObject<Document>.Wrapper](./referencefiledocumentconfiguration/dollardocument.md)
### Getting document properties
- [var fileURL: URL?](./referencefiledocumentconfiguration/fileurl.md)
  The URL of the open file document.
- [var isEditable: Bool](./referencefiledocumentconfiguration/iseditable.md)
  A Boolean that indicates whether you can edit the document.

## See Also

### Deprecated structures
- [struct FileDocumentConfiguration](./filedocumentconfiguration.md)
  The properties of an open file document.
- [struct FileDocumentReadConfiguration](./filedocumentreadconfiguration.md)
  The configuration for reading file contents.
- [struct FileDocumentWriteConfiguration](./filedocumentwriteconfiguration.md)
  The configuration for serializing file contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/referencefiledocumentconfiguration)*