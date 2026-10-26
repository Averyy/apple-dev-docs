# makeCoordinator()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Creates a `Coordinator` instance to coordinate with the `NSView`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewrepresentable/makecoordinator()-6l2eg)*