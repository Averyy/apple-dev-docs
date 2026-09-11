# Source

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Required**: Yes

The type of the source location to read from.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
associatedtype Source = URL
```

#### Discussion

SwiftUI provides the document’s file URL as the source.

## See Also

- [func read(from: sending Self.Source, progress: consuming Subprogress) async throws -> sending Self.Snapshot](documentreader/read(from:progress:).md)
  Reads the document’s content from disk.
- [associatedtype Snapshot](documentreader/snapshot.md)
  The type representing the document’s content after reading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentreader/source)*