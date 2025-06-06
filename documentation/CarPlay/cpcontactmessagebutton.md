# CPContactMessageButton

**Framework**: CarPlay  
**Kind**: class

A button that activates Siri and initiates the compose message flow.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPContactMessageButton
```

#### Overview

> ❗ **Important**:  This subclass of [`CPButton`](cpbutton.md) doesn’t use a handler. Instead, tapping this button activates Siri and launches the compose message flow using the contact information in the [`phoneOrEmail`](cpcontactmessagebutton/phoneoremail.md) property.

 This subclass of [`CPButton`](cpbutton.md) doesn’t use a handler. Instead, tapping this button activates Siri and launches the compose message flow using the contact information in the [`phoneOrEmail`](cpcontactmessagebutton/phoneoremail.md) property.

## Topics

### Creating a Contact Message Button
- [init(phoneOrEmail: String)](cpcontactmessagebutton/init(phoneoremail:).md)
  Creates a contact message button with the provided contact information.
### Getting the Contact Information
- [var phoneOrEmail: String](cpcontactmessagebutton/phoneoremail.md)
  The contact’s phone number or email address.

## Relationships

### Inherits From
- [CPButton](cpbutton.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var actions: [CPButton]?](cpcontact/actions.md)
  The actions that the template displays for this contact.
- [class CPContactCallButton](cpcontactcallbutton.md)
  A button for calling the contact.
- [class CPContactDirectionsButton](cpcontactdirectionsbutton.md)
  A button for getting directions to the contact’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontactmessagebutton)*