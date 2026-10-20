# pickerView(_:viewForRow:forComponent:reusing:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called by the picker view when it needs the view to use for a given row in a given component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func pickerView(_ pickerView: UIPickerView, viewForRow row: Int, forComponent component: Int, reusing view: UIView?) -> UIView
```

```objc
- (UIView *) pickerView:(UIPickerView *) pickerView viewForRow:(NSInteger) row forComponent:(NSInteger) component reusingView:(UIView *) view;
```

#### Return Value

A view object to use as the content of `row`. The object can be any subclass of [`UIView`](../uiview.md), such as [`UILabel`](../uilabel.md), [`UIImageView`](../uiimageview.md), or even a custom view.

#### Discussion

If the previously used view (the `view` parameter) is adequate, return that. If you return a different view, the previously used view is released. The picker view centers the returned view in the rectangle for `row`.

## Parameters

- `pickerView`: An object representing the picker view requesting the data.
- `row`: A zero-indexed number identifying a row of `component`. Rows are numbered top-to-bottom.
- `component`: A zero-indexed number identifying a component of `pickerView`. Components are numbered left-to-right.
- `view`: A view object that was previously used for this row, but is now hidden and cached by the picker view.

## See Also

### Setting the content of component rows
- [func pickerView(UIPickerView, titleForRow: Int, forComponent: Int) -> String?](./pickerview%28_,titleforrow,forcomponent%29.md)
  Called by the picker view when it needs the title to use for a given row in a given component.
- [func pickerView(UIPickerView, attributedTitleForRow: Int, forComponent: Int) -> NSAttributedString?](./pickerview%28_,attributedtitleforrow,forcomponent%29.md)
  Called by the picker view when it needs the styled title to use for a given row in a given component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/pickerview(_:viewforrow:forcomponent:reusing:))*