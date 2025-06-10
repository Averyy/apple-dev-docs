# configureTip(_:arrowEdge:actionHandler:)

**Framework**: TipKit  
**Kind**: method

Configures a reusable view with a tip view embedded.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@discardableResult
@MainActor @preconcurrency final func configureTip(_ tip: any Tip, arrowEdge: Edge? = nil, actionHandler: @escaping @MainActor (Tips.Action) -> Void = { _ in }) -> Self
```

#### Return Value

A collection reusable view that embeds the specified tip.

## Parameters

- `tip`: The tip to display.
- `arrowEdge`: The edge of the tip view that displays the arrow.
- `actionHandler`: The closure to perform when the user triggers a tip’s action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipuicollectionreusableview/configuretip(_:arrowedge:actionhandler:))*