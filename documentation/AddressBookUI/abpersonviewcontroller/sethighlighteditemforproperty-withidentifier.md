# setHighlightedItemForProperty(_:withIdentifier:)

**Framework**: Address Book UI  
**Kind**: method

Specifies whether to highlight a particular property of the displayed person.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func setHighlightedItemForProperty(_ property: ABPropertyID, withIdentifier identifier: ABMultiValueIdentifier)
```

## Parameters

- `property`: The property to highlight.
- `identifier`: When   is a multi-value property, the value to highlight.

## See Also

- [var addressBook: ABAddressBook?](abpersonviewcontroller/addressbook.md)
  Optional. The address book from which to obtain the contact to display.
- [var allowsActions: Bool](abpersonviewcontroller/allowsactions.md)
  Specifies whether the to display buttons for actions such as sending a text message or initiating a FaceTime call.
- [var allowsEditing: Bool](abpersonviewcontroller/allowsediting.md)
  Specifies whether the user can edit the person’s information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/sethighlighteditemforproperty(_:withidentifier:))*