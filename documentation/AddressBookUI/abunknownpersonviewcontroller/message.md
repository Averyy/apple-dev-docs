# message

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

Text displayed below [`alternateName`](./alternatename.md).

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNContactViewController`](../../ContactsUI/cncontactviewcontroller.md) instead.

## Declaration

```swift
var message: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * message;
```

## See Also

### Displaying Person Properties
- [var alternateName: String?](./alternatename.md)
  Provides a value that is displayed instead of the first and last name.
- [var displayedPerson: ABRecord](./displayedperson.md)
  Specifies a person record whose properties are displayed by the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/message)*