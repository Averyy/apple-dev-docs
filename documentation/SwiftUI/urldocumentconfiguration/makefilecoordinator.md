# makeFileCoordinator()

**Framework**: SwiftUI  
**Kind**: method

Creates a file coordinator for coordinated disk access outside the normal read/write flow.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
final func makeFileCoordinator() -> sending NSFileCoordinator
```

#### Discussion

Call this every time to get a new coordinator for each separate read or write operation. SwiftUI coordinates file access for [`read(from:progress:)`](documentreader/read(from:progress:).md) and [`write(snapshot:to:previous:progress:)`](documentwriter/write(snapshot:to:previous:progress:).md) automatically. Use this method when you need to access the document’s file at other times — for example, to read a single sub-file of a package on demand.

Do not reuse coordinators across operations since `NSFileCoordinator` does not conform to `Sendable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/urldocumentconfiguration/makefilecoordinator())*