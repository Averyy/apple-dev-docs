# addressBook

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

Optional; the address book from which to obtain the list of contacts.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNContactPickerViewController`](../../ContactsUI/cncontactpickerviewcontroller.md) instead.

## Declaration

```swift
var addressBook: ABAddressBook? { get set }
```

```objc
@property (nonatomic, readwrite, nullable) ABAddressBookRef addressBook;
```

## Discussion

When unset, an address book is created and assigned to this property when needed. This property is only used when the app has access to the user’s contacts—otherwise it remains `NULL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/addressbook)*