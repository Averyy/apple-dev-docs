# rowSize(forComponent:)

**Framework**: UIKit  
**Kind**: method

Returns the size of a row for a component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func rowSize(forComponent component: Int) -> CGSize
```

#### Return Value

The size of rows in the given component. This is generally the size required to display the largest string or view used as a row in the component.

#### Discussion

A picker view fetches the value of this property by calling the [`pickerView(_:widthForComponent:)`](uipickerviewdelegate/pickerview(_:widthforcomponent:).md) and [`pickerView(_:rowHeightForComponent:)`](uipickerviewdelegate/pickerview(_:rowheightforcomponent:).md) delegate methods, and caches it. The default value is (`0`, `0`).

## Parameters

- `component`: A zero-indexed number identifying a component.

## See Also

- [var numberOfComponents: Int](uipickerview/numberofcomponents.md)
  The number of components for the picker view.
- [func numberOfRows(inComponent: Int) -> Int](uipickerview/numberofrows(incomponent:).md)
  Returns the number of rows for a component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerview/rowsize(forcomponent:))*