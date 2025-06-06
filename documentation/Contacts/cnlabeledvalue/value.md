# value

**Framework**: Contacts  
**Kind**: property

A contact property value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var value: ValueType { get }
```

#### Discussion

A contact property value, such as [`CNPhoneNumber`](cnphonenumber.md) for a phone number, NSString for an email address, and so on. For valid values, see [`CNContact`](cncontact.md) properties that are arrays of labeled value objects.

## See Also

- [var label: String?](cnlabeledvalue/label.md)
  The label for a contact property value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnlabeledvalue/value)*