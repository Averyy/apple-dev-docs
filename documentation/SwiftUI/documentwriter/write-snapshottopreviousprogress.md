# write(snapshot:to:previous:progress:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Writes the document content to disk.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@concurrent
func write(snapshot: sending Self.Snapshot, to destination: sending Self.Destination, previous: sending Self.Snapshot?, progress: consuming Subprogress) async throws
```

#### Discussion

SwiftUI calls this method in the background after obtaining a snapshot via [`snapshot(contentType:)`](writabledocument/snapshot(contenttype:).md). Perform all serialization and disk access here.

For most documents, use [`FileWrapperDocumentWriter`](filewrapperdocumentwriter.md) instead of implementing a custom writer. Only implement `write` yourself when you need capabilities `FileWrapperDocumentWriter` doesn’t provide — such as direct URL access for Core Graphics, AVFoundation, or other frameworks that operate on file paths:

```swift
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
```

## Parameters

- `snapshot`: The snapshot to write to disk.
- `destination`: The file URL to write to.
- `previous`: The last successfully written snapshot, or `nil` on the first save. Compare to `content` to write only what changed in package documents.
- `progress`: A `Subprogress` value to report writing progress. Consume it once with `reporter(totalCount:)` and call `complete(count:)` as units finish.

## See Also

- [associatedtype Snapshot](documentwriter/snapshot.md)
  The type representing the document’s content to write.
- [associatedtype Destination = URL](documentwriter/destination.md)
  The type of the destination location to write to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentwriter/write(snapshot:to:previous:progress:))*