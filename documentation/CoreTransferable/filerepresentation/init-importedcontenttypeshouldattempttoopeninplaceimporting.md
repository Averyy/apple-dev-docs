# init(importedContentType:shouldAttemptToOpenInPlace:importing:)

**Framework**: Core Transferable  
**Kind**: init

Creates a transfer representation for importing transferable items as files.

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
init(importedContentType: UTType, shouldAttemptToOpenInPlace: Bool = false, importing: @escaping (ReceivedTransferredFile) async throws -> Item)
```

## Parameters

- `importedContentType`: A uniform type identifier for the file promise,   returned by the   closure.
- `shouldAttemptToOpenInPlace`: A Boolean value that indicates whether   the receiver wants to gain access to the original item on disk   and can edit it.   If  , the receiver only has access to a copy of the file   made by the system.
- `importing`: A closure that creates the item with given file promise.   The file referred to by the   property of the    is only guaranteed to exist within the   closure. If you need the file   to be around for a longer period, make a copy in the   closure.

## See Also

- [init(contentType: UTType, shouldAttemptToOpenInPlace: Bool, exporting: (Item) async throws -> SentTransferredFile, importing: (ReceivedTransferredFile) async throws -> Item)](filerepresentation/init(contenttype:shouldattempttoopeninplace:exporting:importing:).md)
  Creates a transfer representation for importing and exporting transferable items as files.
- [init(exportedContentType: UTType, shouldAllowToOpenInPlace: Bool, exporting: (Item) async throws -> SentTransferredFile)](filerepresentation/init(exportedcontenttype:shouldallowtoopeninplace:exporting:).md)
  Creates a transfer representation for exporting transferable items as files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/filerepresentation/init(importedcontenttype:shouldattempttoopeninplace:importing:))*