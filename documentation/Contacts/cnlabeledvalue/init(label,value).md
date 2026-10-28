# init(label:value:)

**Framework**: Contacts  
**Kind**: init  
**Role**: Initializer

Returns a new labeled value identifier.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(label: String?, value: ValueType)
```

```objc
- (instancetype) initWithLabel:(NSString *) label value:(ValueType) value;
```

## Return Value

A new labeled value object.

## Parameters

- `label`: A string value for the label portion of the object, or `nil` if the value doesn’t have a label.
- `value`: A value for the labeled value object. For valid values, see [`CNContact`](../cncontact.md) properties that are arrays of labeled value objects.

## See Also

### Creating a labeled value
- [+ labeledValueWithLabel:value:](./labeledvaluewithlabel_value_.md)
  Returns a new labeled value identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnlabeledvalue/init(label:value:))*