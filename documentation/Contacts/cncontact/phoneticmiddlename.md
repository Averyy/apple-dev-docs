# phoneticMiddleName

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The phonetic middle name of the contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var phoneticMiddleName: String { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * phoneticMiddleName;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * phoneticMiddleName;
```

#### Discussion

This property contains a string that specifies the pronunciation of the contact’s middle name.

## See Also

### Getting Name Information
- [var namePrefix: String](./nameprefix.md)
  The name prefix of the contact.
- [var givenName: String](./givenname.md)
  The given name of the contact.
- [var middleName: String](./middlename.md)
  The middle name of the contact.
- [var familyName: String](./familyname.md)
  The family name of the contact.
- [var previousFamilyName: String](./previousfamilyname.md)
  A string for the previous family name of the contact.
- [var nameSuffix: String](./namesuffix.md)
  The name suffix of the contact.
- [var nickname: String](./nickname.md)
  The nickname of the contact.
- [var phoneticGivenName: String](./phoneticgivenname.md)
  The phonetic given name of the contact.
- [var phoneticFamilyName: String](./phoneticfamilyname.md)
  A string for the phonetic family name of the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/phoneticmiddlename)*