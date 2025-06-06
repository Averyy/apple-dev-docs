# pickerView(_:viewForRow:forComponent:reusing:)

**Framework**: UIKit  
**Kind**: method

Called by the picker view when it needs the view to use for a given row in a given component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pickerView(_ pickerView: UIPickerView, viewForRow row: Int, forComponent component: Int, reusing view: UIView?) -> UIView
```

#### Return Value

A view object to use as the content of `row`. The object can be any subclass of [`UIView`](uiview.md), such as [`UILabel`](uilabel.md), [`UIImageView`](uiimageview.md), or even a custom view.

#### Discussion

If the previously used view (the `view` parameter) is adequate, return that. If you return a different view, the previously used view is released. The picker view centers the returned view in the rectangle for `row`.

## Parameters

- `pickerView`: An object representing the picker view requesting the data.
- `row`: A zero-indexed number identifying a row of  . Rows are numbered top-to-bottom.
- `component`: A zero-indexed number identifying a component of  . Components are numbered left-to-right.
- `view`: A view object that was previously used for this row, but is now hidden and cached by the picker view.

## See Also

- [func pickerView(UIPickerView, titleForRow: Int, forComponent: Int) -> String?](uipickerviewdelegate/pickerview(_:titleforrow:forcomponent:).md)
  Called by the picker view when it needs the title to use for a given row in a given component.
- [func pickerView(UIPickerView, attributedTitleForRow: Int, forComponent: Int) -> NSAttributedString?](uipickerviewdelegate/pickerview(_:attributedtitleforrow:forcomponent:).md)
  Called by the picker view when it needs the styled title to use for a given row in a given component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/pickerview(_:viewforrow:forcomponent:reusing:))*