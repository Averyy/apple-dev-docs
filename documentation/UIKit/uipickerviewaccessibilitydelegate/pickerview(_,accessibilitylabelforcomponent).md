# pickerView(_:accessibilityLabelForComponent:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a string that identifies the picker view component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func pickerView(_ pickerView: UIPickerView, accessibilityLabelForComponent component: Int) -> String?
```

```objc
- (NSString *) pickerView:(UIPickerView *) pickerView accessibilityLabelForComponent:(NSInteger) component;
```

## Return Value

A succinct label, in a localized string, that identifies the picker view component.

## Discussion

Implement this optional method to ensure that the accessibility element representing the picker view provides an appropriate label for each component. The system prefers the [`pickerView(_:accessibilityAttributedLabelForComponent:)`](./pickerview%28_,accessibilityattributedlabelforcomponent%29.md) method over this one. For in-depth information on how to create an appropriate label, see [Crafting Useful Labels and Hints](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Making_Application_Accessible/Making_Application_Accessible.html#//apple_ref/doc/uid/TP40008785-CH102-SW6).

## Parameters

- `pickerView`: The picker view object.
- `component`: The component in the picker view that requires a label.

## See Also

### Providing descriptive information
- [func pickerView(UIPickerView, accessibilityAttributedLabelForComponent: Int) -> NSAttributedString?](./pickerview%28_,accessibilityattributedlabelforcomponent%29.md)
  Returns an attributed string that identifies the picker view component.
- [func pickerView(UIPickerView, accessibilityHintForComponent: Int) -> String?](./pickerview%28_,accessibilityhintforcomponent%29.md)
  Returns a string that describes the result of performing an action on the component.
- [func pickerView(UIPickerView, accessibilityAttributedHintForComponent: Int) -> NSAttributedString?](./pickerview%28_,accessibilityattributedhintforcomponent%29.md)
  Returns an attributed string that describes the result of performing an action on the specified component.
- [func pickerView(UIPickerView, accessibilityUserInputLabelsForComponent: Int) -> [String]](./pickerview%28_,accessibilityuserinputlabelsforcomponent%29.md)
- [func pickerView(UIPickerView, accessibilityAttributedUserInputLabelsForComponent: Int) -> [NSAttributedString]](./pickerview%28_,accessibilityattributeduserinputlabelsforcomponent%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate/pickerview(_:accessibilitylabelforcomponent:))*