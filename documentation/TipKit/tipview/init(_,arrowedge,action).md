# init(_:arrowEdge:action:)

**Framework**: TipKit  
**Kind**: init  
**Role**: Initializer

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
@preconcurrency init(_ tip: (any Tip)?, arrowEdge: Edge? = nil, action: @escaping @MainActor @Sendable (Tips.Action) -> Void = { _ in }) where Content == AnyTip
```

Available when `Content` conforms to `Tip`.

#### Discussion

- arrowEdge: The edge of the tip view that displays the arrow.
- action: The closure to perform when the user triggers a tip’s action.

> 💡 **Tip**: The tip to display.

#### Overview

Use a `TipView` when you want to indicate the UI element to which the tip applies, but don’t want to directly anchor the tip view to that element. Use the [`popoverTip(_:arrowEdge:action:)`](../../SwiftUI/view/popovertip%28_,arrowedge,action%29.md) to anchor your tip to an element.

## See Also

### Creating a tip view
- [init((any Tip)?, isPresented: Binding<Bool>?, arrowEdge: Edge?, action: (Tips.Action) -> Void)](./init%28_,ispresented,arrowedge,action%29.md)
  Creates a tip view with an optional arrow.
- [init<AnchorID>((any Tip)?, isPresented: Binding<Bool>?, arrowEdge: Edge?, anchorID: AnchorID, action: (Tips.Action) -> Void)](./init%28_,ispresented,arrowedge,anchorid,action%29.md)
  Creates a tip view with an optional arrow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipview/init(_:arrowedge:action:))*