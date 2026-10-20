# delegate

**Framework**: Contacts UI  
**Kind**: property  
**Role**: Instance Property

The delegate to be notified.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any CNContactViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<CNContactViewControllerDelegate> delegate;
```

#### Discussion

The notification is sent when the user selects a property, or when the contact view controller is dismissed by its parent.

## See Also

### Handling Interactions with the Interface
- [protocol CNContactViewControllerDelegate](../cncontactviewcontrollerdelegate.md)
  Methods you use to respond to user interactions with a contact view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/delegate)*