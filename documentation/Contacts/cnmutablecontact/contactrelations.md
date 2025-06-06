# contactRelations

**Framework**: Contacts  
**Kind**: property

An array of labeled contact relations for the contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var contactRelations: [CNLabeledValue<CNContactRelation>] { get set }
```

#### Discussion

This property is an array of [`CNLabeledValue`](cnlabeledvalue.md) objects, each of which has a label and a [`CNContactRelation`](cncontactrelation.md) value.

## See Also

- [var instantMessageAddresses: [CNLabeledValue<CNInstantMessageAddress>]](cnmutablecontact/instantmessageaddresses.md)
  An array of labeled IM addresses for the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnmutablecontact/contactrelations)*