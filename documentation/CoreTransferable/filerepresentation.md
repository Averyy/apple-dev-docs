# FileRepresentation

**Framework**: Core Transferable  
**Kind**: struct

A transfer representation for types that transfer as a file URL.

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
struct FileRepresentation<Item> where Item : Transferable
```

## Mentions

- [Choosing a transfer representation for a model type](choosing-a-transfer-representation-for-a-model-type.md)

#### Overview

Use a [`FileRepresentation`](filerepresentation.md) for transferring types that involve a large amount of data. For example, if your app defines a `Movie` type that could represent a lengthy video, use a `FileRepresentation` instance to transfer the video data to another app or process.

```swift
struct Movie: Transferable {
    let url: URL
    static var transferRepresentation: some TransferRepresentation {
        FileRepresentation(contentType: .mpeg4Movie) { movie in
            SentTransferredFile(movie.url)
        } importing: { received in
            let copy = URL(fileURLWithPath: "<#...#>")
            try FileManager.default.copyItem(at: received.file, to: copy)
            return Self(url: copy)
        }
    }
}
```

Note that the overall recommendation is to specify the content type that describes the file content as close as possible. For example, if you are sharing a PDF file, declare a [`FileRepresentation`](filerepresentation.md) of a `UTType.pdf` content type, instead of `UTType.fileURL` or `UTType.content` so the data can be dragged, shared, or imported to apps that support that data type:

```swift
  struct PDFDocument: Transferable {
      var file: URL

      static var transferRepresentation: some TransferRepresentation {
          FileRepresentation(contentType: .pdf) { ...
          } importing: { ... }
      }
  }
```

It’s efficient to pass data around as a file and the receiver loads it into memory only if it’s required.

## Topics

### Creating a transfer representation
- [init(contentType: UTType, shouldAttemptToOpenInPlace: Bool, exporting: (Item) async throws -> SentTransferredFile, importing: (ReceivedTransferredFile) async throws -> Item)](filerepresentation/init(contenttype:shouldattempttoopeninplace:exporting:importing:).md)
  Creates a transfer representation for importing and exporting transferable items as files.
- [init(importedContentType: UTType, shouldAttemptToOpenInPlace: Bool, importing: (ReceivedTransferredFile) async throws -> Item)](filerepresentation/init(importedcontenttype:shouldattempttoopeninplace:importing:).md)
  Creates a transfer representation for importing transferable items as files.
- [init(exportedContentType: UTType, shouldAllowToOpenInPlace: Bool, exporting: (Item) async throws -> SentTransferredFile)](filerepresentation/init(exportedcontenttype:shouldallowtoopeninplace:exporting:).md)
  Creates a transfer representation for exporting transferable items as files.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TransferRepresentation](transferrepresentation.md)

## See Also

- [struct SentTransferredFile](senttransferredfile.md)
  A description of a file from the perspective of the sender.
- [struct ReceivedTransferredFile](receivedtransferredfile.md)
  A description of a file from the perspective of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/filerepresentation)*