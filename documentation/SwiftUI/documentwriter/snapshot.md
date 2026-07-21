# Snapshot

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Required**: Yes

The type representing the document’s content to write.

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

This is the same type returned by [`snapshot(contentType:)`](writabledocument/snapshot(contenttype:).md). It crosses an actor boundary (from main actor to background), so use `sending` annotations or make it `Sendable`.

## See Also

- [func write(snapshot: sending Self.Snapshot, to: sending Self.Destination, previous: sending Self.Snapshot?, progress: consuming Subprogress) async throws](documentwriter/write(snapshot:to:previous:progress:).md)
  Writes the document content to disk.
- [associatedtype Destination = URL](documentwriter/destination.md)
  The type of the destination location to write to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentwriter/snapshot)*