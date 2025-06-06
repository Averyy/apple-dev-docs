# settingLabel(_:)

**Framework**: Contacts  
**Kind**: method

Returns a labeled value object with an existing value and identifier.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func settingLabel(_ label: String?) -> Self
```

#### Return Value

A labeled value object with an existing value and identifier.

## Parameters

- `label`: The label of the copied labeled value object, or   if the contact property value doesn’t have a label.

## See Also

- [func settingLabel(String?, value: ValueType) -> Self](cnlabeledvalue/settinglabel(_:value:).md)
  Returns a labeled value object with the specified label and value with the existing identifier.
- [func settingValue(ValueType) -> Self](cnlabeledvalue/settingvalue(_:).md)
  Returns a new value for an existing label and identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnlabeledvalue/settinglabel(_:))*