# pickerView(_:rowHeightForComponent:)

**Framework**: UIKit  
**Kind**: method

Called by the picker view when it needs the row height to use for drawing row content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pickerView(_ pickerView: UIPickerView, rowHeightForComponent component: Int) -> CGFloat
```

#### Return Value

A float value indicating the height of the row in points.

## Parameters

- `pickerView`: The picker view requesting this information.
- `component`: A zero-indexed number identifying a component of  . Components are numbered left-to-right.

## See Also

- [func pickerView(UIPickerView, widthForComponent: Int) -> CGFloat](uipickerviewdelegate/pickerview(_:widthforcomponent:).md)
  Called by the picker view when it needs the row width to use for drawing row content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/pickerview(_:rowheightforcomponent:))*