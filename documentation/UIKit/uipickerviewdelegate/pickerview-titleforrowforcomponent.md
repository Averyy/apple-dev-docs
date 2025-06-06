# pickerView(_:titleForRow:forComponent:)

**Framework**: UIKit  
**Kind**: method

Called by the picker view when it needs the title to use for a given row in a given component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String?
```

#### Return Value

The string to use as the title of the indicated component row.

#### Discussion

If you implement both this method and the [`pickerView(_:attributedTitleForRow:forComponent:)`](uipickerviewdelegate/pickerview(_:attributedtitleforrow:forcomponent:).md) method, the picker view prefers the [`pickerView(_:attributedTitleForRow:forComponent:)`](uipickerviewdelegate/pickerview(_:attributedtitleforrow:forcomponent:).md) method. However, if that method returns `nil`, the picker view falls back to using the string returned by this method.

## Parameters

- `pickerView`: An object representing the picker view requesting the data.
- `row`: A zero-indexed number identifying a row of  . Rows are numbered top-to-bottom.
- `component`: A zero-indexed number identifying a component of  . Components are numbered left-to-right.

## See Also

- [func pickerView(UIPickerView, attributedTitleForRow: Int, forComponent: Int) -> NSAttributedString?](uipickerviewdelegate/pickerview(_:attributedtitleforrow:forcomponent:).md)
  Called by the picker view when it needs the styled title to use for a given row in a given component.
- [func pickerView(UIPickerView, viewForRow: Int, forComponent: Int, reusing: UIView?) -> UIView](uipickerviewdelegate/pickerview(_:viewforrow:forcomponent:reusing:).md)
  Called by the picker view when it needs the view to use for a given row in a given component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/pickerview(_:titleforrow:forcomponent:))*