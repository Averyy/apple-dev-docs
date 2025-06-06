# delegate

**Framework**: Contacts UI  
**Kind**: property

The delegate to be notified.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any CNContactViewControllerDelegate)? { get set }
```

#### Discussion

The notification is sent when the user selects a property, or when the contact view controller is dismissed by its parent.

## See Also

- [protocol CNContactViewControllerDelegate](cncontactviewcontrollerdelegate.md)
  Methods you use to respond to user interactions with a contact view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/delegate)*