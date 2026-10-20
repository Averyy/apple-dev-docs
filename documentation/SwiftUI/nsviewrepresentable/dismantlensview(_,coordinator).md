# dismantleNSView(_:coordinator:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method  
**Required**: Yes

Cleans up the presented AppKit view (and coordinator) in anticipation of their removal.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency static func dismantleNSView(_ nsView: Self.NSViewType, coordinator: Self.Coordinator)
```

#### Discussion

Use this method to perform additional clean-up work related to your custom view. For example, you might use this method to remove observers or update other parts of your SwiftUI interface.

## Parameters

- `nsView`: Your custom view object.
- `coordinator`: The custom coordinator you use to communicate changes back to SwiftUI. If you do not use a custom coordinator instance, the system provides a default instance.

## Default Implementations

### NSViewRepresentable Implementations
- [static func dismantleNSView(Self.NSViewType, coordinator: Self.Coordinator)](./dismantlensview%28_,coordinator%29-21agq.md)
  Cleans up the presented AppKit view (and coordinator) in anticipation of their removal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewrepresentable/dismantlensview(_:coordinator:))*