# dismantleNSViewController(_:coordinator:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Cleans up the presented `NSViewController` (and coordinator) in anticipation of their removal.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency static func dismantleNSViewController(_ nsViewController: Self.NSViewControllerType, coordinator: Self.Coordinator)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentable/dismantlensviewcontroller(_:coordinator:)-t6ob)*