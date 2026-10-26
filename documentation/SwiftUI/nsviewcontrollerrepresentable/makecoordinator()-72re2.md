# makeCoordinator()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Creates an object to coordinate with the AppKit view controller.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency func makeCoordinator() -> Self.Coordinator
```

Available when `Coordinator` is `()`.

#### Discussion

`Coordinator` can be accessed via `Context`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentable/makecoordinator()-72re2)*