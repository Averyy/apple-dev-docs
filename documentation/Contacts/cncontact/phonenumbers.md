# phoneNumbers

**Framework**: Contacts  
**Kind**: property

An array of labeled phone numbers for a contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var phoneNumbers: [CNLabeledValue<CNPhoneNumber>] { get }
```

#### Discussion

This property is an array of [`CNLabeledValue`](cnlabeledvalue.md) objects, each of which has a label and a [`CNPhoneNumber`](cnphonenumber.md) value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/phonenumbers)*