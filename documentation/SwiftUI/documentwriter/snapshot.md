# Snapshot

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type representing the document’s content to write.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
associatedtype Snapshot
```

#### Discussion

This is the same type returned by [`snapshot(contentType:)`](../writabledocument/snapshot%28contenttype%29.md). It crosses an actor boundary (from main actor to background), so use `sending` annotations or make it `Sendable`.

## See Also

### Writing a document
- [func write(snapshot: sending Self.Snapshot, to: sending Self.Destination, previous: sending Self.Snapshot?, progress: consuming Subprogress) async throws](./write%28snapshot,to,previous,progress%29.md)
  Writes the document content to disk.
- [associatedtype Destination = URL](./destination.md)
  The type of the destination location to write to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentwriter/snapshot)*