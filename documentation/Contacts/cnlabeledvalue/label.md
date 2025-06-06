# label

**Framework**: Contacts  
**Kind**: property

The label for a contact property value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var label: String? { get }
```

#### Discussion

A contact property can have a label, such as Home, Work, iPhone, etc. For some predefined label constants, see[`CNPhoneNumber`](cnphonenumber.md), and [`CNContactRelation`](cncontactrelation.md). Custom labels can also be used. Labels are not used for [`CNSocialProfile`](cnsocialprofile.md) and [`CNInstantMessageAddress`](cninstantmessageaddress.md) properties.

## See Also

- [var value: ValueType](cnlabeledvalue/value.md)
  A contact property value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnlabeledvalue/label)*