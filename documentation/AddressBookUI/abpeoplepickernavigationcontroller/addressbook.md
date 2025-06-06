# addressBook

**Framework**: Address Book UI  
**Kind**: property

Optional; the address book from which to obtain the list of contacts.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var addressBook: ABAddressBook? { get set }
```

#### Discussion

When unset, an address book is created and assigned to this property when needed. This property is only used when the app has access to the user’s contacts—otherwise it remains `NULL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller/addressbook)*