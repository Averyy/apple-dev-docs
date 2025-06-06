# pickerView(_:accessibilityHintForComponent:)

**Framework**: UIKit  
**Kind**: method

Returns a string that describes the result of performing an action on the component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pickerView(_ pickerView: UIPickerView, accessibilityHintForComponent component: Int) -> String?
```

#### Return Value

The localized string that describes the results of performing an action on the specified component.

#### Discussion

Implement this optional method to ensure that the accessibility element representing the picker view provides an appropriate hint for each component. The system prefers the [`pickerView(_:accessibilityAttributedHintForComponent:)`](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributedhintforcomponent:).md) method over this one. For in-depth information on how to create an appropriate hint, see [`Guidelines for Creating Hints`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Making_Application_Accessible/Making_Application_Accessible.html#//apple_ref/doc/uid/TP40008785-CH102-SW11).

## Parameters

- `pickerView`: The picker view object.
- `component`: The component in the picker view that requires a hint.

## See Also

- [func pickerView(UIPickerView, accessibilityLabelForComponent: Int) -> String?](uipickerviewaccessibilitydelegate/pickerview(_:accessibilitylabelforcomponent:).md)
  Returns a string that identifies the picker view component.
- [func pickerView(UIPickerView, accessibilityAttributedLabelForComponent: Int) -> NSAttributedString?](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributedlabelforcomponent:).md)
  Returns an attributed string that identifies the picker view component.
- [func pickerView(UIPickerView, accessibilityAttributedHintForComponent: Int) -> NSAttributedString?](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributedhintforcomponent:).md)
  Returns an attributed string that describes the result of performing an action on the specified component.
- [func pickerView(UIPickerView, accessibilityUserInputLabelsForComponent: Int) -> [String]](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityuserinputlabelsforcomponent:).md)
- [func pickerView(UIPickerView, accessibilityAttributedUserInputLabelsForComponent: Int) -> [NSAttributedString]](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributeduserinputlabelsforcomponent:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate/pickerview(_:accessibilityhintforcomponent:))*