# keysToFetch

**Framework**: Contacts  
**Kind**: property

The properties to fetch in the returned contacts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var keysToFetch: [any CNKeyDescriptor] { get set }
```

#### Discussion

An array of contact property keys or key descriptors from contact objects to be fetched in the returned contacts. For example, [`CNContactEmailAddressesKey`](cncontactemailaddresseskey.md), [`CNContactPhoneNumbersKey`](cncontactphonenumberskey.md), [`CNContactFormatterStyle.fullName`](cncontactformatterstyle/fullname.md) fetches the contact’s email addresses, phone numbers, and contact’s full name with the contact formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/keystofetch)*