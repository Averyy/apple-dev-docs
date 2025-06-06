# parentGroup

**Framework**: Address Book UI  
**Kind**: property

Optional. Specifies the group to which to add the new contact on save.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var parentGroup: ABRecord? { get set }
```

#### Discussion

You must set [`addressBook`](abnewpersonviewcontroller/addressbook.md) before you can set this property.

## See Also

- [var addressBook: ABAddressBook?](abnewpersonviewcontroller/addressbook.md)
  Optional. The address book to which the new contact is added.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller/parentgroup)*