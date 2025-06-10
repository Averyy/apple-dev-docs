# pickerView(_:accessibilityAttributedLabelForComponent:)

**Framework**: UIKit  
**Kind**: method

Returns an attributed string that identifies the picker view component.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pickerView(_ pickerView: UIPickerView, accessibilityAttributedLabelForComponent component: Int) -> NSAttributedString?
```

#### Return Value

The attributed string that identifies the picker view component

#### Discussion

Use this method to provide descriptive information for the components of a picker view. Your attributed string may include the [`accessibilitySpeechLanguage`](https://developer.apple.com/documentation/Foundation/NSAttributedString/Key/accessibilitySpeechLanguage) (Swift) or [`UIAccessibilitySpeechAttributeLanguage`](uiaccessibilityspeechattributelanguage.md) (Objective-C) attribute, which lets you use different language synthesizers for different parts of the string. The system prefers this method over the [`pickerView(_:accessibilityLabelForComponent:)`](uipickerviewaccessibilitydelegate/pickerview(_:accessibilitylabelforcomponent:).md) method. For in-depth information on how to create an appropriate descriptive string, see [`Crafting Useful Labels and Hints`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Making_Application_Accessible/Making_Application_Accessible.html#//apple_ref/doc/uid/TP40008785-CH102-SW6).

## Parameters

- `pickerView`: The picker view object.
- `component`: The component in the picker view that requires a label.

## See Also

- [func pickerView(UIPickerView, accessibilityLabelForComponent: Int) -> String?](uipickerviewaccessibilitydelegate/pickerview(_:accessibilitylabelforcomponent:).md)
  Returns a string that identifies the picker view component.
- [func pickerView(UIPickerView, accessibilityHintForComponent: Int) -> String?](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityhintforcomponent:).md)
  Returns a string that describes the result of performing an action on the component.
- [func pickerView(UIPickerView, accessibilityAttributedHintForComponent: Int) -> NSAttributedString?](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributedhintforcomponent:).md)
  Returns an attributed string that describes the result of performing an action on the specified component.
- [func pickerView(UIPickerView, accessibilityUserInputLabelsForComponent: Int) -> [String]](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityuserinputlabelsforcomponent:).md)
- [func pickerView(UIPickerView, accessibilityAttributedUserInputLabelsForComponent: Int) -> [NSAttributedString]](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributeduserinputlabelsforcomponent:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributedlabelforcomponent:))*