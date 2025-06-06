# pickerView(_:widthForComponent:)

**Framework**: UIKit  
**Kind**: method

Called by the picker view when it needs the row width to use for drawing row content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pickerView(_ pickerView: UIPickerView, widthForComponent component: Int) -> CGFloat
```

#### Return Value

A float value indicating the width of the row in points.

## Parameters

- `pickerView`: The picker view requesting this information.
- `component`: A zero-indexed number identifying a component of the picker view. Components are numbered left-to-right.

## See Also

- [func pickerView(UIPickerView, rowHeightForComponent: Int) -> CGFloat](uipickerviewdelegate/pickerview(_:rowheightforcomponent:).md)
  Called by the picker view when it needs the row height to use for drawing row content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/pickerview(_:widthforcomponent:))*