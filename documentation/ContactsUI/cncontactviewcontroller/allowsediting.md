# allowsEditing

**Framework**: Contacts UI  
**Kind**: property  
**Role**: Instance Property

Determines whether the user can edit the contact’s information.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var allowsEditing: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsEditing;
```

## Discussion

By default, the value of this property is [`true`](../../Swift/true.md). All properties are visible when editing a contact.

## See Also

### Customizing Contact Card
- [var allowsActions: Bool](./allowsactions.md)
  Determines whether to display buttons for actions such as sending a text message or initiating a FaceTime call.
- [var shouldShowLinkedContacts: Bool](./shouldshowlinkedcontacts.md)
  Determines whether to display data from contacts that are linked to the contact being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/allowsediting)*