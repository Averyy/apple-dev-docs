# dismantleNSViewController(_:coordinator:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method  
**Required**: Yes

Cleans up the presented view controller (and coordinator) in anticipation of its removal.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency static func dismantleNSViewController(_ nsViewController: Self.NSViewControllerType, coordinator: Self.Coordinator)
```

## Discussion

Use this method to perform additional clean-up work related to your custom view controller. For example, you might use this method to remove observers or update other parts of your SwiftUI interface.

## Parameters

- `nsViewController`: Your custom view controller object.
- `coordinator`: The custom coordinator instance you use to communicate changes back to SwiftUI. If you do not use a custom coordinator, the system provides a default instance.

## Default Implementations

### NSViewControllerRepresentable Implementations
- [static func dismantleNSViewController(Self.NSViewControllerType, coordinator: Self.Coordinator)](./dismantlensviewcontroller%28_,coordinator%29-t6ob.md)
  Cleans up the presented `NSViewController` (and coordinator) in anticipation of their removal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentable/dismantlensviewcontroller(_:coordinator:))*