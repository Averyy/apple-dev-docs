# DocumentWriter

**Framework**: SwiftUI  
**Kind**: protocol

A type that writes a document’s content to a file.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol DocumentWriter<Snapshot>
```

#### Overview

SwiftUI calls your document’s [`snapshot(contentType:)`](writabledocument/snapshot(contenttype:).md) on the main actor to capture the current state, then obtains a `DocumentWriter` from [`writer(configuration:)`](writabledocument/writer(configuration:).md) and invokes `write(content:to:previous:progress:)` in the background with coordinated file access.

Use [`FileWrapperDocumentWriter`](filewrapperdocumentwriter.md) for cases cases that don’t require custom file write logic. Implement a `DocumentWriter` when you need direct URL access or streaming writes:

```swift
struct ImageWriter: DocumentWriter {
    @concurrent
    func write(content image: sending CGImage, to destination: URL,
        previous: sending CGImage?, progress: consuming Subprogress
    ) async throws {
        guard let imageDestination =
            CGImageDestinationCreateWithURL(
                destination as CFURL,
                UTType.jpeg.identifier as CFString,
                1, nil
            ) else {
            throw CocoaError(.fileWriteUnknown)
        }
        CGImageDestinationAddImage(
            imageDestination, image, nil
        )
        guard CGImageDestinationFinalize(
            imageDestination
        ) else {
            throw CocoaError(.fileWriteUnknown)
        }
    }
}
```

## Topics

### Writing a document
- [func write(snapshot: sending Self.Snapshot, to: sending Self.Destination, previous: sending Self.Snapshot?, progress: consuming Subprogress) async throws](documentwriter/write(snapshot:to:previous:progress:).md)
  Writes the document content to disk.
- [associatedtype Snapshot](documentwriter/snapshot.md)
  The type representing the document’s content to write.
- [associatedtype Destination = URL](documentwriter/destination.md)
  The type of the destination location to write to.

## Relationships

### Conforming Types
- [FileWrapperDocumentWriter](filewrapperdocumentwriter.md)

## See Also

- [struct DocumentReadConfiguration](documentreadconfiguration.md)
  The context SwiftUI passes to [`reader(configuration:)`](readabledocument/reader(configuration:).md).
- [struct DocumentWriteConfiguration](documentwriteconfiguration.md)
  The context SwiftUI passes to [`writer(configuration:)`](writabledocument/writer(configuration:).md).
- [protocol DocumentReader](documentreader.md)
  A type that reads a document’s content from a file.
- [struct FileWrapperDocumentReader](filewrapperdocumentreader.md)
  A document reader that deserializes a `FileWrapper` into a snapshot.
- [struct FileWrapperDocumentWriter](filewrapperdocumentwriter.md)
  A document writer that serializes a snapshot into a `FileWrapper`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentwriter)*