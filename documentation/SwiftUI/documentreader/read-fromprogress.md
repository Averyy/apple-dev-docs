# read(from:progress:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Reads the document from disk.

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

## Parameters

- `source`: The source to read from.
- `progress`: The subprogress to report reading progress to SwiftUI.

## See Also

- [associatedtype Snapshot](documentreader/snapshot.md)
  A type that represents the document’s stored content.
- [associatedtype Source = URL](documentreader/source.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentreader/read(from:progress:))*