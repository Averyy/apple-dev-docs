# Destination

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Required**: Yes

The type of the destination location to write to.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
associatedtype Destination = URL
```

#### Discussion

SwiftUI provides the document’s file URL as the destination.

## See Also

- [func write(snapshot: sending Self.Snapshot, to: sending Self.Destination, previous: sending Self.Snapshot?, progress: consuming Subprogress) async throws](documentwriter/write(snapshot:to:previous:progress:).md)
  Writes the document content to disk.
- [associatedtype Snapshot](documentwriter/snapshot.md)
  The type representing the document’s content to write.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentwriter/destination)*