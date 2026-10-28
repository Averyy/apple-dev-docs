# contactType

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

An enum identifying the contact type.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var contactType: CNContactType { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, readonly) CNContactType contactType;
```

*macOS*

```objc
@property (atomic, readonly) CNContactType contactType;
```

## Discussion

For a list of predefined contact types, see [`CNContactType`](../cncontacttype.md).

## See Also

### Identifying the Contact
- [var identifier: String](./identifier.md)
  A value that uniquely identifies a contact on the device.
- [enum CNContactType](../cncontacttype.md)
  The types a contact can be.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/contacttype)*