# shouldShowLinkedContacts

**Framework**: Contacts UI  
**Kind**: property  
**Role**: Instance Property

Determines whether to display data from contacts that are linked to the contact being displayed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var shouldShowLinkedContacts: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL shouldShowLinkedContacts;
```

#### Discussion

By default, the value of this property is [`false`](../../Swift/false.md).

## See Also

### Customizing Contact Card
- [var allowsEditing: Bool](./allowsediting.md)
  Determines whether the user can edit the contact’s information.
- [var allowsActions: Bool](./allowsactions.md)
  Determines whether to display buttons for actions such as sending a text message or initiating a FaceTime call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/shouldshowlinkedcontacts)*