# addressBook

**Framework**: Address Book UI  
**Kind**: property

Optional. The address book from which to obtain the contact to display.

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

- [var allowsActions: Bool](abpersonviewcontroller/allowsactions.md)
  Specifies whether the to display buttons for actions such as sending a text message or initiating a FaceTime call.
- [var allowsEditing: Bool](abpersonviewcontroller/allowsediting.md)
  Specifies whether the user can edit the person’s information.
- [func setHighlightedItemForProperty(ABPropertyID, withIdentifier: ABMultiValueIdentifier)](abpersonviewcontroller/sethighlighteditemforproperty(_:withidentifier:).md)
  Specifies whether to highlight a particular property of the displayed person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/addressbook)*