# dismantleNSView(_:coordinator:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Cleans up the presented AppKit view (and coordinator) in anticipation of their removal.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency static func dismantleNSView(_ nsView: Self.NSViewType, coordinator: Self.Coordinator)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewrepresentable/dismantlensview(_:coordinator:)-21agq)*