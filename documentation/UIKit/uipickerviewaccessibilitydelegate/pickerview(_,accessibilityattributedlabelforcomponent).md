# pickerView(_:accessibilityAttributedLabelForComponent:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns an attributed string that identifies the picker view component.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func pickerView(_ pickerView: UIPickerView, accessibilityAttributedLabelForComponent component: Int) -> NSAttributedString?
```

```objc
- (NSAttributedString *) pickerView:(UIPickerView *) pickerView accessibilityAttributedLabelForComponent:(NSInteger) component;
```

## Return Value

The attributed string that identifies the picker view component

## Discussion

Use this method to provide descriptive information for the components of a picker view. Your attributed string may include the [`UIAccessibilitySpeechAttributeLanguage`](../uiaccessibilityspeechattributelanguage.md) attribute, which lets you use different language synthesizers for different parts of the string. The system prefers this method over the [`pickerView(_:accessibilityLabelForComponent:)`](./pickerview%28_,accessibilitylabelforcomponent%29.md) method. For in-depth information on how to create an appropriate descriptive string, see [Crafting Useful Labels and Hints](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Making_Application_Accessible/Making_Application_Accessible.html#//apple_ref/doc/uid/TP40008785-CH102-SW6).

## Parameters

- `pickerView`: The picker view object.
- `component`: The component in the picker view that requires a label.

## See Also

### Providing descriptive information
- [func pickerView(UIPickerView, accessibilityLabelForComponent: Int) -> String?](./pickerview%28_,accessibilitylabelforcomponent%29.md)
  Returns a string that identifies the picker view component.
- [func pickerView(UIPickerView, accessibilityHintForComponent: Int) -> String?](./pickerview%28_,accessibilityhintforcomponent%29.md)
  Returns a string that describes the result of performing an action on the component.
- [func pickerView(UIPickerView, accessibilityAttributedHintForComponent: Int) -> NSAttributedString?](./pickerview%28_,accessibilityattributedhintforcomponent%29.md)
  Returns an attributed string that describes the result of performing an action on the specified component.
- [func pickerView(UIPickerView, accessibilityUserInputLabelsForComponent: Int) -> [String]](./pickerview%28_,accessibilityuserinputlabelsforcomponent%29.md)
- [func pickerView(UIPickerView, accessibilityAttributedUserInputLabelsForComponent: Int) -> [NSAttributedString]](./pickerview%28_,accessibilityattributeduserinputlabelsforcomponent%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributedlabelforcomponent:))*