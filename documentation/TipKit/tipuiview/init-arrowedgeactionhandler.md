# init(_:arrowEdge:actionHandler:)

**Framework**: TipKit  
**Kind**: init

Creates a tip view with an optional arrow edge and action handler.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ tip: any Tip, arrowEdge: Edge? = nil, actionHandler: @escaping @MainActor (Tips.Action) -> Void = { _ in })
```

#### Discussion

Use a `TipUIView` when you want to indicate the UI element to which the tip applies, but do not want to directly anchor the tip view to that element.

## Parameters

- `tip`: The tip to display.
- `arrowEdge`: The edge of the tip view that displays the arrow.
- `actionHandler`: The closure to perform when the user triggers a tip’s action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipuiview/init(_:arrowedge:actionhandler:))*