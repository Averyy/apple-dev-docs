# init(_:sourceItem:actionHandler:)

**Framework**: TipKit  
**Kind**: init

Initializes a popover controller with the specified tip.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(_ tip: any Tip, sourceItem: any UIPopoverPresentationControllerSourceItem, actionHandler: @escaping (Tips.Action) -> Void = { _ in })
```

## Parameters

- `tip`: The tip to display.
- `sourceItem`: The item on which to anchor the tip popover.
- `actionHandler`: The closure to perform when the user triggers a tip’s action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipuipopoverviewcontroller/init(_:sourceitem:actionhandler:))*