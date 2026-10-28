# identifier

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

A value that uniquely identifies a contact on the device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var identifier: String { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * identifier;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * identifier;
```

## Discussion

It is recommended that you use the [`identifier`](./identifier.md) when re-fetching the contact. An identifier can be persisted between the app launches. Note that this identifier only uniquely identifies the contact on the current device.

## See Also

### Identifying the Contact
- [var contactType: CNContactType](./contacttype.md)
  An enum identifying the contact type.
- [enum CNContactType](../cncontacttype.md)
  The types a contact can be.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/identifier)*