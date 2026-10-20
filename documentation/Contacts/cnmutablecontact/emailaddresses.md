# emailAddresses

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

An array of labeled email addresses for the contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var emailAddresses: [CNLabeledValue<NSString>] { get set }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy) NSArray<CNLabeledValue<NSString *> *> * emailAddresses;
```

*macOS*

```objc
@property (atomic, copy) NSArray<CNLabeledValue<NSString *> *> * emailAddresses;
```

#### Discussion

This property is an array of [`CNLabeledValue`](../cnlabeledvalue.md) objects, each of which has a label and a [`NSString`](../../Foundation/nsstring.md) value.

## See Also

### Setting Addresses
- [var postalAddresses: [CNLabeledValue<CNPostalAddress>]](./postaladdresses.md)
  An array of labeled postal addresses for a contact.
- [var urlAddresses: [CNLabeledValue<NSString>]](./urladdresses.md)
  An array of labeled URL addresses for a contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnmutablecontact/emailaddresses)*