# allowsEditing

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

Specifies whether the user can edit the person’s information.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNContactViewController`](../../ContactsUI/cncontactviewcontroller.md) instead.

## Declaration

```swift
var allowsEditing: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsEditing;
```

#### Discussion

When editing a person’s information, all person properties are visible.

## See Also

### Configuring Person Views
- [var addressBook: ABAddressBook?](./addressbook.md)
  Optional. The address book from which to obtain the contact to display.
- [var allowsActions: Bool](./allowsactions.md)
  Specifies whether the to display buttons for actions such as sending a text message or initiating a FaceTime call.
- [func setHighlightedItemForProperty(ABPropertyID, withIdentifier: ABMultiValueIdentifier)](./sethighlighteditemforproperty%28_,withidentifier%29.md)
  Specifies whether to highlight a particular property of the displayed person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/allowsediting)*