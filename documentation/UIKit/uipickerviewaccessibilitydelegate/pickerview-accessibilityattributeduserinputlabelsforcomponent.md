# pickerView(_:accessibilityAttributedUserInputLabelsForComponent:)

**Framework**: UIKit  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pickerView(_ pickerView: UIPickerView, accessibilityAttributedUserInputLabelsForComponent component: Int) -> [NSAttributedString]
```

## See Also

- [func pickerView(UIPickerView, accessibilityLabelForComponent: Int) -> String?](uipickerviewaccessibilitydelegate/pickerview(_:accessibilitylabelforcomponent:).md)
  Returns a string that identifies the picker view component.
- [func pickerView(UIPickerView, accessibilityAttributedLabelForComponent: Int) -> NSAttributedString?](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributedlabelforcomponent:).md)
  Returns an attributed string that identifies the picker view component.
- [func pickerView(UIPickerView, accessibilityHintForComponent: Int) -> String?](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityhintforcomponent:).md)
  Returns a string that describes the result of performing an action on the component.
- [func pickerView(UIPickerView, accessibilityAttributedHintForComponent: Int) -> NSAttributedString?](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributedhintforcomponent:).md)
  Returns an attributed string that describes the result of performing an action on the specified component.
- [func pickerView(UIPickerView, accessibilityUserInputLabelsForComponent: Int) -> [String]](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityuserinputlabelsforcomponent:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributeduserinputlabelsforcomponent:))*