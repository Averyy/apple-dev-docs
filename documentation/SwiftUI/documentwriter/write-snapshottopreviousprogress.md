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

## Parameters

- `snapshot`: The snapshot to write to disk.
- `destination`: The destination to write to.
- `previous`: The previously written snapshot. Use it to skip writing unchanged data.
- `progress`: The subprogress to report writing progress to SwiftUI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentwriter/write(snapshot:to:previous:progress:))*