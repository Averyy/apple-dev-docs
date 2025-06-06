# addressBook

**Framework**: Address Book UI  
**Kind**: property

Optional. The address book to which the new contact is added.

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

When unset, an address book is created and assigned to this property when needed.

## See Also

- [var parentGroup: ABRecord?](abnewpersonviewcontroller/parentgroup.md)
  Optional. Specifies the group to which to add the new contact on save.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller/addressbook)*