# pickerView(_:accessibilityAttributedHintForComponent:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns an attributed string that describes the result of performing an action on the specified component.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func pickerView(_ pickerView: UIPickerView, accessibilityAttributedHintForComponent component: Int) -> NSAttributedString?
```

```objc
- (NSAttributedString *) pickerView:(UIPickerView *) pickerView accessibilityAttributedHintForComponent:(NSInteger) component;
```

#### Return Value

The localized attributed string that describes the results of performing an action on the specified component.

#### Discussion

Implement this optional method to ensure that the accessibility element representing the picker view provides an appropriate hint for each component. Your attributed string may include the [`UIAccessibilitySpeechAttributeLanguage`](../uiaccessibilityspeechattributelanguage.md) attribute, which lets you use different language synthesizers for different parts of the string. The system prefers this method over the [`pickerView(_:accessibilityHintForComponent:)`](./pickerview%28_,accessibilityhintforcomponent%29.md) method.

For in-depth information on how to create an appropriate hint, see [Guidelines for Creating Hints](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Making_Application_Accessible/Making_Application_Accessible.html#//apple_ref/doc/uid/TP40008785-CH102-SW11).

## Parameters

- `pickerView`: The picker view object.
- `component`: The component in the picker view that requires a hint.

## See Also

### Providing descriptive information
- [func pickerView(UIPickerView, accessibilityLabelForComponent: Int) -> String?](./pickerview%28_,accessibilitylabelforcomponent%29.md)
  Returns a string that identifies the picker view component.
- [func pickerView(UIPickerView, accessibilityAttributedLabelForComponent: Int) -> NSAttributedString?](./pickerview%28_,accessibilityattributedlabelforcomponent%29.md)
  Returns an attributed string that identifies the picker view component.
- [func pickerView(UIPickerView, accessibilityHintForComponent: Int) -> String?](./pickerview%28_,accessibilityhintforcomponent%29.md)
  Returns a string that describes the result of performing an action on the component.
- [func pickerView(UIPickerView, accessibilityUserInputLabelsForComponent: Int) -> [String]](./pickerview%28_,accessibilityuserinputlabelsforcomponent%29.md)
- [func pickerView(UIPickerView, accessibilityAttributedUserInputLabelsForComponent: Int) -> [NSAttributedString]](./pickerview%28_,accessibilityattributeduserinputlabelsforcomponent%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributedhintforcomponent:))*