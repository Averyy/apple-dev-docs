# settingLabel(_:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (instancetype) labeledValueBySettingLabel:(NSString *) label;
```

#### Return Value

A labeled value object with an existing value and identifier.

## Parameters

- `label`: The label of the copied labeled value object, or `nil` if the contact property value doesn’t have a label.

## See Also

### Setting labels and values
- [func settingLabel(String?, value: ValueType) -> Self](./settinglabel%28_,value%29.md)
  Returns a labeled value object with the specified label and value with the existing identifier.
- [func settingValue(ValueType) -> Self](./settingvalue%28_%29.md)
  Returns a new value for an existing label and identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnlabeledvalue/settinglabel(_:))*