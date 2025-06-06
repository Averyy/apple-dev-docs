# urlAddresses

**Framework**: Contacts  
**Kind**: property

An array of labeled URL addresses for a contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var urlAddresses: [CNLabeledValue<NSString>] { get set }
```

#### Discussion

This property is an array of [`CNLabeledValue`](cnlabeledvalue.md) objects, each of which has a label and a [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) value that contains the URL.

## See Also

- [var postalAddresses: [CNLabeledValue<CNPostalAddress>]](cnmutablecontact/postaladdresses.md)
  An array of labeled postal addresses for a contact.
- [var emailAddresses: [CNLabeledValue<NSString>]](cnmutablecontact/emailaddresses.md)
  An array of labeled email addresses for the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnmutablecontact/urladdresses)*