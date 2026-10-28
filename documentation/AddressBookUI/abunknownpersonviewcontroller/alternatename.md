# alternateName

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

Provides a value that is displayed instead of the first and last name.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNContactViewController`](../../ContactsUI/cncontactviewcontroller.md) instead.

## Declaration

```swift
var alternateName: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * alternateName;
```

## Discussion

The alternate name is only for display. It is not saved if this contact is added to the address book database.

## See Also

### Displaying Person Properties
- [var message: String?](./message.md)
  Text displayed below [`alternateName`](./alternatename.md).
- [var displayedPerson: ABRecord](./displayedperson.md)
  Specifies a person record whose properties are displayed by the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/alternatename)*