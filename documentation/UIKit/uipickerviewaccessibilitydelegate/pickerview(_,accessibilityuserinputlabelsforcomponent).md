# pickerView(_:accessibilityUserInputLabelsForComponent:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func pickerView(_ pickerView: UIPickerView, accessibilityUserInputLabelsForComponent component: Int) -> [String]
```

```objc
- (NSArray<NSString *> *) pickerView:(UIPickerView *) pickerView accessibilityUserInputLabelsForComponent:(NSInteger) component;
```

## See Also

### Providing descriptive information
- [func pickerView(UIPickerView, accessibilityLabelForComponent: Int) -> String?](./pickerview%28_,accessibilitylabelforcomponent%29.md)
  Returns a string that identifies the picker view component.
- [func pickerView(UIPickerView, accessibilityAttributedLabelForComponent: Int) -> NSAttributedString?](./pickerview%28_,accessibilityattributedlabelforcomponent%29.md)
  Returns an attributed string that identifies the picker view component.
- [func pickerView(UIPickerView, accessibilityHintForComponent: Int) -> String?](./pickerview%28_,accessibilityhintforcomponent%29.md)
  Returns a string that describes the result of performing an action on the component.
- [func pickerView(UIPickerView, accessibilityAttributedHintForComponent: Int) -> NSAttributedString?](./pickerview%28_,accessibilityattributedhintforcomponent%29.md)
  Returns an attributed string that describes the result of performing an action on the specified component.
- [func pickerView(UIPickerView, accessibilityAttributedUserInputLabelsForComponent: Int) -> [NSAttributedString]](./pickerview%28_,accessibilityattributeduserinputlabelsforcomponent%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate/pickerview(_:accessibilityuserinputlabelsforcomponent:))*