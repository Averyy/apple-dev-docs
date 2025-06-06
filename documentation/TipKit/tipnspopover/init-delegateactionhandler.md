# init(_:delegate:actionHandler:)

**Framework**: TipKit  
**Kind**: init

Initializes a popover with the specified tip.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
@preconcurrency required init(_ tip: any Tip, delegate: (any NSPopoverDelegate)? = nil, actionHandler: @escaping (Tips.Action) -> Void = { _ in })
```

## Parameters

- `tip`: The tip to display.
- `delegate`: A set of optional methods that a popover delegate can implement to provide additional or custom functionality
- `actionHandler`: The closure to perform when the user triggers a tip’s action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipnspopover/init(_:delegate:actionhandler:))*