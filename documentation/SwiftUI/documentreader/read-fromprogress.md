# read(from:progress:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Reads the document’s content from disk.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@concurrent
func read(from source: sending Self.Source, progress: consuming Subprogress) async throws -> sending Self.Snapshot
```

#### Return Value

A snapshot representing the document’s content.

#### Discussion

SwiftUI calls this method in the background with coordinated file access. Perform all deserialization and disk access here — the returned snapshot is delivered to [`apply(snapshot:previous:)`](readabledocument/apply(snapshot:previous:).md) on the main actor.

For most documents, use [`FileWrapperDocumentReader`](filewrapperdocumentreader.md) instead of implementing a custom reader. Only implement `read` yourself when you need capabilities `FileWrapperDocumentReader` doesn’t provide — such as direct URL access for Core Graphics, AVFoundation, or other frameworks that operate on file paths:

```swift
@concurrent
func read(from source: URL, progress: consuming Subprogress)
    async throws -> sending CGImage {
    guard let imageSource =
        CGImageSourceCreateWithURL(source as CFURL, nil),
          let image = CGImageSourceCreateImageAtIndex(
              imageSource, 0, nil
          ) else {
        throw CocoaError(.fileReadCorruptFile)
    }
    return image
}
```

## Parameters

- `source`: The file URL to read from.
- `progress`: A `Subprogress` value to report reading progress. Consume it once with `reporter(totalCount:)` and call `complete(count:)` as units finish.

## See Also

- [associatedtype Snapshot](documentreader/snapshot.md)
  The type representing the document’s content after reading.
- [associatedtype Source = URL](documentreader/source.md)
  The type of the source location to read from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentreader/read(from:progress:))*