# init(_:)

**Framework**: UIKit  
**Kind**: init

Creates a new band selection interaction object with the provided handler code.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
init(_ selectionHandler: @escaping (UIBandSelectionInteraction) -> Void)
```

#### Return Value

An initialized band selection interaction object. Add the returned object to a view to begin detecting interactions.

## Parameters

- `selectionHandler`: The handler block you use to process interaction-related events. The handler block has no return value and takes the following parameter: - **interaction**: The band selection interaction object that reported the event. Use the [`state`](uibandselectioninteraction/state-swift.property.md) property of this object to determine what actions to take. For example, when the value of the property is [`UIBandSelectionInteraction.State.selecting`](uibandselectioninteraction/state-swift.enum/selecting.md), get the current selection rectangle and intersect it with the items in your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibandselectioninteraction/init(_:))*