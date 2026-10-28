# Snapshot

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type representing the document’s content after reading.

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

## Discussion

This can be any type: a `String`, a custom struct, or even the document type itself. SwiftUI delivers it to [`apply(snapshot:previous:)`](../readabledocument/apply%28snapshot,previous%29.md) on the main actor after reading completes.

## See Also

### Reading a document
- [func read(from: sending Self.Source, progress: consuming Subprogress) async throws -> sending Self.Snapshot](./read%28from,progress%29.md)
  Reads the document’s content from disk.
- [associatedtype Source = URL](./source.md)
  The type of the source location to read from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentreader/snapshot)*