# DocumentReader

**Framework**: SwiftUI  
**Kind**: protocol

A type that reads a document’s content from a file.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol DocumentReader<Snapshot>
```

#### Overview

SwiftUI calls your document’s [`reader(configuration:)`](readabledocument/reader(configuration:).md) method to obtain a `DocumentReader`, then invokes [`read(from:progress:)`](documentreader/read(from:progress:).md) in the background with coordinated file access. The returned snapshot is delivered to [`apply(snapshot:previous:)`](readabledocument/apply(snapshot:previous:).md) on the main actor.

Use [`FileWrapperDocumentReader`](filewrapperdocumentreader.md) for cases that don’t require custom file read logic. Implement a `DocumentReader` when you need direct URL access for frameworks like Core Graphics, AVFoundation, or PDFKit:

```swift
struct ImageReader: DocumentReader {
    @concurrent
    func read(from source: URL, progress: consuming Subprogress)
        async throws -> sending CGImage {
        guard let provider =
            CGDataProvider(url: source as CFURL),
              let image = CGImage(
                  jpegDataProviderSource: provider,
                  decode: nil, shouldInterpolate: true,
                  intent: .defaultIntent
              ) else {
            throw CocoaError(.fileReadCorruptFile)
        }
        return image
    }
}
```

SwiftUI provides the document’s file URL as the reader’s source.

## Topics

### Reading a document
- [func read(from: sending Self.Source, progress: consuming Subprogress) async throws -> sending Self.Snapshot](documentreader/read(from:progress:).md)
  Reads the document’s content from disk.
- [associatedtype Snapshot](documentreader/snapshot.md)
  The type representing the document’s content after reading.
- [associatedtype Source = URL](documentreader/source.md)
  The type of the source location to read from.

## Relationships

### Conforming Types
- [FileWrapperDocumentReader](filewrapperdocumentreader.md)

## See Also

- [struct DocumentReadConfiguration](documentreadconfiguration.md)
  The context SwiftUI passes to [`reader(configuration:)`](readabledocument/reader(configuration:).md).
- [struct DocumentWriteConfiguration](documentwriteconfiguration.md)
  The context SwiftUI passes to [`writer(configuration:)`](writabledocument/writer(configuration:).md).
- [protocol DocumentWriter](documentwriter.md)
  A type that writes a document’s content to a file.
- [struct FileWrapperDocumentReader](filewrapperdocumentreader.md)
  A document reader that deserializes a `FileWrapper` into a snapshot.
- [struct FileWrapperDocumentWriter](filewrapperdocumentwriter.md)
  A document writer that serializes a snapshot into a `FileWrapper`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentreader)*