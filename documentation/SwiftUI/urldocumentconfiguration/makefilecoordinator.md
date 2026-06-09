# makeFileCoordinator()

**Framework**: SwiftUI  
**Kind**: method

A coordinator that can be used to coordinate additional read and write operations to prevent document corruption.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
final func makeFileCoordinator() -> sending NSFileCoordinator
```

#### Discussion

Call this every time to get a new coordinator for each separate read or write operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/urldocumentconfiguration/makefilecoordinator())*