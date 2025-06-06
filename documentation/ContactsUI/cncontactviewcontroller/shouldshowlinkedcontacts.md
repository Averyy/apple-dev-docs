# shouldShowLinkedContacts

**Framework**: Contacts UI  
**Kind**: property

Determines whether to display data from contacts that are linked to the contact being displayed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var shouldShowLinkedContacts: Bool { get set }
```

#### Discussion

By default, the value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var allowsEditing: Bool](cncontactviewcontroller/allowsediting.md)
  Determines whether the user can edit the contact’s information.
- [var allowsActions: Bool](cncontactviewcontroller/allowsactions.md)
  Determines whether to display buttons for actions such as sending a text message or initiating a FaceTime call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/shouldshowlinkedcontacts)*