# selectedRow(inComponent:)

**Framework**: UIKit  
**Kind**: method

Returns the index of the selected row in a given component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func selectedRow(inComponent component: Int) -> Int
```

#### Return Value

A zero-indexed number identifying the selected row, or `-1` if no row is selected.

## Parameters

- `component`: A zero-indexed number identifying a component of the picker view.

## See Also

- [func selectRow(Int, inComponent: Int, animated: Bool)](uipickerview/selectrow(_:incomponent:animated:).md)
  Selects a row in a specified component of the picker view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerview/selectedrow(incomponent:))*