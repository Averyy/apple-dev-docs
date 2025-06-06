# init(contentType:shouldAttemptToOpenInPlace:exporting:importing:)

**Framework**: Core Transferable  
**Kind**: init

Creates a transfer representation for importing and exporting transferable items as files.

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
init(contentType: UTType, shouldAttemptToOpenInPlace: Bool = false, exporting: @escaping (Item) async throws -> SentTransferredFile, importing: @escaping (ReceivedTransferredFile) async throws -> Item)
```

## Parameters

- `contentType`: A uniform type identifier that best describes the item.
- `shouldAttemptToOpenInPlace`: A Boolean value that   indicates whether the receiver gains access to the original item on disk   and can edit it,   or to a copy made by the system.
- `exporting`: A closure that provides a file representation of the given item.
- `importing`: A closure that instantiates the item with given file promise.   The file referred to by the    property of the    instance   is only guaranteed to exist within the   closure. If you need the file   to be around for a longer period, make a copy in the   closure.

## See Also

- [init(importedContentType: UTType, shouldAttemptToOpenInPlace: Bool, importing: (ReceivedTransferredFile) async throws -> Item)](filerepresentation/init(importedcontenttype:shouldattempttoopeninplace:importing:).md)
  Creates a transfer representation for importing transferable items as files.
- [init(exportedContentType: UTType, shouldAllowToOpenInPlace: Bool, exporting: (Item) async throws -> SentTransferredFile)](filerepresentation/init(exportedcontenttype:shouldallowtoopeninplace:exporting:).md)
  Creates a transfer representation for exporting transferable items as files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/filerepresentation/init(contenttype:shouldattempttoopeninplace:exporting:importing:))*