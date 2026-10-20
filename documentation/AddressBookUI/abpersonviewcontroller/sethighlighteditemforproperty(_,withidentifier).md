# setHighlightedItemForProperty(_:withIdentifier:)

**Framework**: Address Book UI  
**Kind**: method  
**Role**: Instance Method

Specifies whether to highlight a particular property of the displayed person.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNContactViewController`](../../ContactsUI/cncontactviewcontroller.md) instead.

## Declaration

```swift
func setHighlightedItemForProperty(_ property: ABPropertyID, withIdentifier identifier: ABMultiValueIdentifier)
```

```objc
- (void) setHighlightedItemForProperty:(ABPropertyID) property withIdentifier:(ABMultiValueIdentifier) identifier;
```

## Parameters

- `property`: The property to highlight.
- `identifier`: When `property` is a multi-value property, the value to highlight.

## See Also

### Configuring Person Views
- [var addressBook: ABAddressBook?](./addressbook.md)
  Optional. The address book from which to obtain the contact to display.
- [var allowsActions: Bool](./allowsactions.md)
  Specifies whether the to display buttons for actions such as sending a text message or initiating a FaceTime call.
- [var allowsEditing: Bool](./allowsediting.md)
  Specifies whether the user can edit the person’s information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/sethighlighteditemforproperty(_:withidentifier:))*