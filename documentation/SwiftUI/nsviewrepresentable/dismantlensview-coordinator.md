# dismantleNSView(_:coordinator:)

**Framework**: SwiftUI  
**Kind**: method  
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
- `coordinator`: The custom coordinator you use to communicate changes   back to SwiftUI. If you do not use a custom coordinator instance, the   system provides a default instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewrepresentable/dismantlensview(_:coordinator:))*