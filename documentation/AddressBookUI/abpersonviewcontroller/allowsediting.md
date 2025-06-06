# allowsEditing

**Framework**: Address Book UI  
**Kind**: property

Specifies whether the user can edit the person’s information.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var allowsEditing: Bool { get set }
```

#### Discussion

When editing a person’s information, all person properties are visible.

## See Also

- [var addressBook: ABAddressBook?](abpersonviewcontroller/addressbook.md)
  Optional. The address book from which to obtain the contact to display.
- [var allowsActions: Bool](abpersonviewcontroller/allowsactions.md)
  Specifies whether the to display buttons for actions such as sending a text message or initiating a FaceTime call.
- [func setHighlightedItemForProperty(ABPropertyID, withIdentifier: ABMultiValueIdentifier)](abpersonviewcontroller/sethighlighteditemforproperty(_:withidentifier:).md)
  Specifies whether to highlight a particular property of the displayed person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/allowsediting)*