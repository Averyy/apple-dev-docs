# givenName

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The given name of the contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var givenName: String { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * givenName;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * givenName;
```

#### Discussion

The given name is often known as the first name of the contact.

## See Also

### Getting Name Information
- [var namePrefix: String](./nameprefix.md)
  The name prefix of the contact.
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
- [var phoneticMiddleName: String](./phoneticmiddlename.md)
  The phonetic middle name of the contact.
- [var phoneticFamilyName: String](./phoneticfamilyname.md)
  A string for the phonetic family name of the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/givenname)*