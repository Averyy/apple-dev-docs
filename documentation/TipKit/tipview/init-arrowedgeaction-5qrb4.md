# init(_:arrowEdge:action:)

**Framework**: TipKit  
**Kind**: init

Creates a tip view with an optional arrow.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ tip: Content, arrowEdge: Edge? = nil, action: @escaping (Tips.Action) -> Void = { _ in })
```

#### Discussion

Use a `TipView` when you want to indicate the UI element to which the tip applies, but don’t want to directly anchor the tip view to that element. Use the [`popoverTip(_:arrowEdge:action:)`](https://developer.apple.com/documentation/SwiftUI/View/popoverTip(_:arrowEdge:action:)) to anchor your tip to an element.

## Parameters

- `tip`: The tip to display.
- `arrowEdge`: The edge of the tip view that displays the arrow.
- `action`: The closure to perform when the user triggers a tip’s action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipview/init(_:arrowedge:action:)-5qrb4)*