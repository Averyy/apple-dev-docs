# pickerView(_:attributedTitleForRow:forComponent:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called by the picker view when it needs the styled title to use for a given row in a given component.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func pickerView(_ pickerView: UIPickerView, attributedTitleForRow row: Int, forComponent component: Int) -> NSAttributedString?
```

```objc
- (NSAttributedString *) pickerView:(UIPickerView *) pickerView attributedTitleForRow:(NSInteger) row forComponent:(NSInteger) component;
```

## Return Value

The attributed string to use as the title of the indicated component row.

## Discussion

If you implement both this method and the [`pickerView(_:titleForRow:forComponent:)`](./pickerview%28_,titleforrow,forcomponent%29.md) method, the picker view prefers the use of this method. However, if your implementation of this method returns `nil`, the picker view falls back to using the string returned by the [`pickerView(_:titleForRow:forComponent:)`](./pickerview%28_,titleforrow,forcomponent%29.md) method.

## Parameters

- `pickerView`: An object representing the picker view requesting the data.
- `row`: A zero-indexed number identifying a row of `component`. Rows are numbered top-to-bottom.
- `component`: A zero-indexed number identifying a component of `pickerView`. Components are numbered left-to-right.

## See Also

### Setting the content of component rows
- [func pickerView(UIPickerView, titleForRow: Int, forComponent: Int) -> String?](./pickerview%28_,titleforrow,forcomponent%29.md)
  Called by the picker view when it needs the title to use for a given row in a given component.
- [func pickerView(UIPickerView, viewForRow: Int, forComponent: Int, reusing: UIView?) -> UIView](./pickerview%28_,viewforrow,forcomponent,reusing%29.md)
  Called by the picker view when it needs the view to use for a given row in a given component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/pickerview(_:attributedtitleforrow:forcomponent:))*