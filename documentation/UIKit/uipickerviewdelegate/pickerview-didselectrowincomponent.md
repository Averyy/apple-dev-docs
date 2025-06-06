# pickerView(_:didSelectRow:inComponent:)

**Framework**: UIKit  
**Kind**: method

Called by the picker view when the user selects a row in a component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int)
```

#### Discussion

To determine what value the user selected, the delegate uses the `row` index to access the value at the corresponding position in the array used to construct the component.

## Parameters

- `pickerView`: An object representing the picker view requesting the data.
- `row`: A zero-indexed number identifying a row of  . Rows are numbered top-to-bottom.
- `component`: A zero-indexed number identifying a component of  . Components are numbered left-to-right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/pickerview(_:didselectrow:incomponent:))*