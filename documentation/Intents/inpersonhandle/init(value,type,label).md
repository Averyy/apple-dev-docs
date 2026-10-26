# init(value:type:label:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes and returns a person handle with the specified data.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.1+

## Declaration

```swift
init(value: String?, type: INPersonHandleType, label: INPersonHandleLabel?)
```

```objc
- (instancetype) initWithValue:(NSString *) value type:(INPersonHandleType) type label:(INPersonHandleLabel) label;
```

#### Return Value

An initialized person handle object.

## Parameters

- `value`: The data to associate with the handle. Specify the data as a user-readable string.
- `type`: A constant indicating the type of information in the *value* parameter. For a list of possible values, see [`INPersonHandleType`](../inpersonhandletype.md).
- `label`: The label to apply to the information. Use this information to help differentiate labels of similar types but with different meanings. For example, use this parameter to specify whether a phone number is the user’s home or work phone.

## See Also

### Initializing a Person Handle
- [convenience init(value: String?, type: INPersonHandleType)](./init%28value,type%29.md)
  Initializes and returns a person handle with the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpersonhandle/init(value:type:label:))*