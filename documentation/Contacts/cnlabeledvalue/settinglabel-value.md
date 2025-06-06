# settingLabel(_:value:)

**Framework**: Contacts  
**Kind**: method

Returns a labeled value object with the specified label and value with the existing identifier.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func settingLabel(_ label: String?, value: ValueType) -> Self
```

#### Return Value

A labeled value object with the existing identifier.

## Parameters

- `label`: The label of the copied labeled value object, or   if the contact property value doesn’t have a label.
- `value`: The copied labeled value object. For valid values, see   properties that are arrays of labeled value objects.

## See Also

- [func settingLabel(String?) -> Self](cnlabeledvalue/settinglabel(_:).md)
  Returns a labeled value object with an existing value and identifier.
- [func settingValue(ValueType) -> Self](cnlabeledvalue/settingvalue(_:).md)
  Returns a new value for an existing label and identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnlabeledvalue/settinglabel(_:value:))*