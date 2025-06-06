# pickerView(_:attributedTitleForRow:forComponent:)

**Framework**: UIKit  
**Kind**: method

Called by the picker view when it needs the styled title to use for a given row in a given component.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pickerView(_ pickerView: UIPickerView, attributedTitleForRow row: Int, forComponent component: Int) -> NSAttributedString?
```

#### Return Value

The attributed string to use as the title of the indicated component row.

#### Discussion

If you implement both this method and the [`pickerView(_:titleForRow:forComponent:)`](uipickerviewdelegate/pickerview(_:titleforrow:forcomponent:).md) method, the picker view prefers the use of this method. However, if your implementation of this method returns `nil`, the picker view falls back to using the string returned by the [`pickerView(_:titleForRow:forComponent:)`](uipickerviewdelegate/pickerview(_:titleforrow:forcomponent:).md) method.

## Parameters

- `pickerView`: An object representing the picker view requesting the data.
- `row`: A zero-indexed number identifying a row of  . Rows are numbered top-to-bottom.
- `component`: A zero-indexed number identifying a component of  . Components are numbered left-to-right.

## See Also

- [func pickerView(UIPickerView, titleForRow: Int, forComponent: Int) -> String?](uipickerviewdelegate/pickerview(_:titleforrow:forcomponent:).md)
  Called by the picker view when it needs the title to use for a given row in a given component.
- [func pickerView(UIPickerView, viewForRow: Int, forComponent: Int, reusing: UIView?) -> UIView](uipickerviewdelegate/pickerview(_:viewforrow:forcomponent:reusing:).md)
  Called by the picker view when it needs the view to use for a given row in a given component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/pickerview(_:attributedtitleforrow:forcomponent:))*