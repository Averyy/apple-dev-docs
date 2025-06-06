# init(exportedContentType:shouldAllowToOpenInPlace:exporting:)

**Framework**: Core Transferable  
**Kind**: init

Creates a transfer representation for exporting transferable items as files.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(exportedContentType: UTType, shouldAllowToOpenInPlace: Bool = false, exporting: @escaping (Item) async throws -> SentTransferredFile)
```

## Parameters

- `exportedContentType`: A uniform type identifier for the file  ,   returned by the   closure.
- `shouldAllowToOpenInPlace`: A Boolean value that indicates whether   the receiver can try to gain access to the original item on disk   and can edit it.   If  , the receiver only has access to a copy of the file   made by the system.
- `exporting`: A closure that provides a file representation of the given item.

## See Also

- [init(contentType: UTType, shouldAttemptToOpenInPlace: Bool, exporting: (Item) async throws -> SentTransferredFile, importing: (ReceivedTransferredFile) async throws -> Item)](filerepresentation/init(contenttype:shouldattempttoopeninplace:exporting:importing:).md)
  Creates a transfer representation for importing and exporting transferable items as files.
- [init(importedContentType: UTType, shouldAttemptToOpenInPlace: Bool, importing: (ReceivedTransferredFile) async throws -> Item)](filerepresentation/init(importedcontenttype:shouldattempttoopeninplace:importing:).md)
  Creates a transfer representation for importing transferable items as files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/filerepresentation/init(exportedcontenttype:shouldallowtoopeninplace:exporting:))*