# settingValue(_:)

**Framework**: Contacts  
**Kind**: method

Returns a new value for an existing label and identifier.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func settingValue(_ value: ValueType) -> Self
```

#### Return Value

The [`CNLabeledValue`](cnlabeledvalue.md) object with an existing label and identifier.

## Parameters

- `value`: A new value for the copied labeled value object. For valid values, see   properties that are arrays of labeled value objects.

## See Also

- [func settingLabel(String?) -> Self](cnlabeledvalue/settinglabel(_:).md)
  Returns a labeled value object with an existing value and identifier.
- [func settingLabel(String?, value: ValueType) -> Self](cnlabeledvalue/settinglabel(_:value:).md)
  Returns a labeled value object with the specified label and value with the existing identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnlabeledvalue/settingvalue(_:))*