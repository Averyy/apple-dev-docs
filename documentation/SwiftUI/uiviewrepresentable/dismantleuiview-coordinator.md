# dismantleUIView(_:coordinator:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Cleans up the presented UIKit view (and coordinator) in anticipation of their removal.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func dismantleUIView(_ uiView: Self.UIViewType, coordinator: Self.Coordinator)
```

#### Discussion

Use this method to perform additional clean-up work related to your custom view. For example, you might use this method to remove observers or update other parts of your SwiftUI interface.

## Parameters

- `uiView`: Your custom view object.
- `coordinator`: The custom coordinator instance you use to communicate   changes back to SwiftUI. If you do not use a custom coordinator, the   system provides a default instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiviewrepresentable/dismantleuiview(_:coordinator:))*