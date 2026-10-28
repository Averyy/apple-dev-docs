# labeledValueWithLabel:value:

**Framework**: Contacts  
**Kind**: method  
**Role**: Type Method

Returns a new labeled value identifier.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) labeledValueWithLabel:(NSString *) label value:(ValueType) value;
```

## Return Value

A new labeled value object.

## Parameters

- `label`: A string value for the label of the labeled value object, or `nil` if the value doesn’t have a label.
- `value`: A value for the labeled value object. For valid values, see [`CNContact`](../cncontact.md) properties that are arrays of labeled value objects.

## See Also

### Creating a labeled value
- [init(label: String?, value: ValueType)](./init%28label,value%29.md)
  Returns a new labeled value identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnlabeledvalue/labeledvaluewithlabel:value:)*