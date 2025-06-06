# UIPickerViewAccessibilityDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of methods you can implement to provide accessibility information for individual components of a picker view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIPickerViewAccessibilityDelegate : UIPickerViewDelegate
```

## Topics

### Providing descriptive information
- [func pickerView(UIPickerView, accessibilityLabelForComponent: Int) -> String?](uipickerviewaccessibilitydelegate/pickerview(_:accessibilitylabelforcomponent:).md)
  Returns a string that identifies the picker view component.
- [func pickerView(UIPickerView, accessibilityAttributedLabelForComponent: Int) -> NSAttributedString?](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributedlabelforcomponent:).md)
  Returns an attributed string that identifies the picker view component.
- [func pickerView(UIPickerView, accessibilityHintForComponent: Int) -> String?](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityhintforcomponent:).md)
  Returns a string that describes the result of performing an action on the component.
- [func pickerView(UIPickerView, accessibilityAttributedHintForComponent: Int) -> NSAttributedString?](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributedhintforcomponent:).md)
  Returns an attributed string that describes the result of performing an action on the specified component.
- [func pickerView(UIPickerView, accessibilityUserInputLabelsForComponent: Int) -> [String]](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityuserinputlabelsforcomponent:).md)
- [func pickerView(UIPickerView, accessibilityAttributedUserInputLabelsForComponent: Int) -> [NSAttributedString]](uipickerviewaccessibilitydelegate/pickerview(_:accessibilityattributeduserinputlabelsforcomponent:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIPickerViewDelegate](uipickerviewdelegate.md)

## See Also

- [class UIAccessibilityElement](uiaccessibilityelement.md)
  An element that should be accessible to users with disabilities, but that isn’t accessible by default.
- [protocol UIScrollViewAccessibilityDelegate](uiscrollviewaccessibilitydelegate.md)
  A set of methods you can implement to provide accessibility information for a scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerviewaccessibilitydelegate)*