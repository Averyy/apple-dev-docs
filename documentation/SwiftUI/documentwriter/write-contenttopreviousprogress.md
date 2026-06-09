# write(content:to:previous:progress:)

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
nonisolated
func write(content: sending Self.Snapshot, to destination: sending Self.Destination, previous: sending Self.Snapshot?, progress: consuming Subprogress) async throws
```

## Parameters

- `content`: The content to write to disk.
- `destination`: The destination to write to.
- `previous`: The previously written content. Use it to skip writing unchanged data.
- `progress`: The subprogress to report writing progress to SwiftUI.

## See Also

- [associatedtype Snapshot](documentwriter/snapshot.md)
  A type that represents the document’s stored content.
- [associatedtype Destination](documentwriter/destination.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentwriter/write(content:to:previous:progress:))*