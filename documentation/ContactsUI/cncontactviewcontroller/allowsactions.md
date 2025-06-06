# allowsActions

**Framework**: Contacts UI  
**Kind**: property

Determines whether to display buttons for actions such as sending a text message or initiating a FaceTime call.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsActions: Bool { get set }
```

#### Discussion

By default the value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var allowsEditing: Bool](cncontactviewcontroller/allowsediting.md)
  Determines whether the user can edit the contact’s information.
- [var shouldShowLinkedContacts: Bool](cncontactviewcontroller/shouldshowlinkedcontacts.md)
  Determines whether to display data from contacts that are linked to the contact being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/allowsactions)*