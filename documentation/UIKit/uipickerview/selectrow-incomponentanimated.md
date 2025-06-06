# selectRow(_:inComponent:animated:)

**Framework**: UIKit  
**Kind**: method

Selects a row in a specified component of the picker view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func selectRow(_ row: Int, inComponent component: Int, animated: Bool)
```

## Parameters

- `row`: A zero-indexed number identifying a row of  .
- `component`: A zero-indexed number identifying a component of the picker view.
- `animated`:   to animate the selection by spinning the wheel (component) to the new value; if you specify  , the new selection is shown immediately.

## See Also

- [func selectedRow(inComponent: Int) -> Int](uipickerview/selectedrow(incomponent:).md)
  Returns the index of the selected row in a given component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerview/selectrow(_:incomponent:animated:))*