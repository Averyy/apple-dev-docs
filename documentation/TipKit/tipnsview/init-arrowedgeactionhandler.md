# init(_:arrowEdge:actionHandler:)

**Framework**: TipKit  
**Kind**: init

Creates a tip view with an optional arrow.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(_ tip: any Tip, arrowEdge: Edge? = nil, actionHandler: @escaping (Tips.Action) -> Void = { _ in })
```

#### Discussion

Use a `TipNSView` when you want to indicate the UI element to which the tip applies, but do not want to directly anchor the tip view to that element.

## Parameters

- `tip`: The tip to display.
- `arrowEdge`: The edge of the tip view that displays the arrow.
- `actionHandler`: The closure to perform when the user triggers a tip’s action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipnsview/init(_:arrowedge:actionhandler:))*