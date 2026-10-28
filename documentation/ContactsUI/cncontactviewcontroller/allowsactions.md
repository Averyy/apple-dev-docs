# allowsActions

**Framework**: Contacts UI  
**Kind**: property  
**Role**: Instance Property

Determines whether to display buttons for actions such as sending a text message or initiating a FaceTime call.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var allowsActions: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsActions;
```

## Discussion

By default the value of this property is [`true`](../../Swift/true.md).

## See Also

### Customizing Contact Card
- [var allowsEditing: Bool](./allowsediting.md)
  Determines whether the user can edit the contact’s information.
- [var shouldShowLinkedContacts: Bool](./shouldshowlinkedcontacts.md)
  Determines whether to display data from contacts that are linked to the contact being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/allowsactions)*