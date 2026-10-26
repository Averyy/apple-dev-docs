# phoneNumberWithStringValue:

**Framework**: Contacts  
**Kind**: method  
**Role**: Type Method

Returns a new phone number object initialized with the specified phone number string.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) phoneNumberWithStringValue:(NSString *) stringValue;
```

#### Return Value

A newly initialize the phone number object.

#### Discussion

This is a convenience class method that provides the same functionality as [`init(stringValue:)`](./init%28stringvalue%29.md). This method returns `nil` when the value of  `stringValue` is `nil`.

## Parameters

- `stringValue`: A string value with which to initialize phone number object.

## See Also

### Creating a Phone Number Object
- [init(stringValue: String)](./init%28stringvalue%29.md)
  Returns a new phone number object initialized with the specified phone number string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnphonenumber/phonenumberwithstringvalue:)*