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

## Declaration

```swift
@MainActor
@preconcurrency init(_ tip: (any Tip)?, arrowEdge: Edge? = nil, action: @escaping @MainActor (Tips.Action) -> Void = { _ in }) where Content == AnyTip
```

#### Discussion

- arrowEdge: The edge of the tip view that displays the arrow.
- action: The closure to perform when the user triggers a tip’s action.

> 💡 **Tip**: The tip to display.

#### Overview

Use a `TipView` when you want to indicate the UI element to which the tip applies, but don’t want to directly anchor the tip view to that element. Use the [`popoverTip(_:arrowEdge:action:)`](https://developer.apple.com/documentation/SwiftUI/View/popoverTip(_:arrowEdge:action:)) to anchor your tip to an element.

## See Also

- [init((any Tip)?, isPresented: Binding<Bool>?, arrowEdge: Edge?, action: (Tips.Action) -> Void)](tipview/init(_:ispresented:arrowedge:action:).md)
  Creates a tip view with an optional arrow.
- [init<AnchorID>((any Tip)?, isPresented: Binding<Bool>?, arrowEdge: Edge?, anchorID: AnchorID, action: (Tips.Action) -> Void)](tipview/init(_:ispresented:arrowedge:anchorid:action:).md)
  Creates a tip view with an optional arrow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipview/init(_:arrowedge:action:))*