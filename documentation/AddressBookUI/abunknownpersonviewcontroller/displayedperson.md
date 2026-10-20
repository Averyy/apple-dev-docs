# displayedPerson

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

Specifies a person record whose properties are displayed by the view controller.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNContactViewController`](../../ContactsUI/cncontactviewcontroller.md) instead.

## Declaration

```swift
var displayedPerson: ABRecord { get set }
```

```objc
@property (nonatomic, readwrite) ABRecordRef displayedPerson;
```

#### Discussion

All the properties of `displayedPerson` are displayed by the view controller.

## See Also

### Displaying Person Properties
- [var alternateName: String?](./alternatename.md)
  Provides a value that is displayed instead of the first and last name.
- [var message: String?](./message.md)
  Text displayed below [`alternateName`](./alternatename.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/displayedperson)*