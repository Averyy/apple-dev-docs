# Snapshot

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Required**: Yes

The type representing the document’s content after reading.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
associatedtype Snapshot
```

#### Discussion

This can be any type: a `String`, a custom struct, or even the document type itself. SwiftUI delivers it to [`apply(snapshot:previous:)`](readabledocument/apply(snapshot:previous:).md) on the main actor after reading completes.

## See Also

- [func read(from: sending Self.Source, progress: consuming Subprogress) async throws -> sending Self.Snapshot](documentreader/read(from:progress:).md)
  Reads the document’s content from disk.
- [associatedtype Source = URL](documentreader/source.md)
  The type of the source location to read from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentreader/snapshot)*