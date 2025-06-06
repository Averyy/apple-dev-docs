# CNContactViewControllerDelegate

**Framework**: Contacts UI  
**Kind**: protocol

Methods you use to respond to user interactions with a contact view controller.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
protocol CNContactViewControllerDelegate : NSObjectProtocol
```

#### Overview

Implement the methods of this protocol and assign the resulting object to the [`delegate`](cncontactviewcontroller/delegate.md) property of a `CNContactViewController` object.

## Topics

### Responding to User Events
- [func contactViewController(CNContactViewController, shouldPerformDefaultActionFor: CNContactProperty) -> Bool](cncontactviewcontrollerdelegate/contactviewcontroller(_:shouldperformdefaultactionfor:).md)
  Called when the user selects a property.
- [func contactViewController(CNContactViewController, didCompleteWith: CNContact?)](cncontactviewcontrollerdelegate/contactviewcontroller(_:didcompletewith:).md)
  Called when the view has been presented.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any CNContactViewControllerDelegate)?](cncontactviewcontroller/delegate.md)
  The delegate to be notified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontrollerdelegate)*