# allowsActions

**Framework**: Address Book UI  
**Kind**: property

Specifies whether the to display buttons for actions such as sending a text message or initiating a FaceTime call.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var allowsActions: Bool { get set }
```

## See Also

- [var addressBook: ABAddressBook?](abpersonviewcontroller/addressbook.md)
  Optional. The address book from which to obtain the contact to display.
- [var allowsEditing: Bool](abpersonviewcontroller/allowsediting.md)
  Specifies whether the user can edit the person’s information.
- [func setHighlightedItemForProperty(ABPropertyID, withIdentifier: ABMultiValueIdentifier)](abpersonviewcontroller/sethighlighteditemforproperty(_:withidentifier:).md)
  Specifies whether to highlight a particular property of the displayed person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/allowsactions)*