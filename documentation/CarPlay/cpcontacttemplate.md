# CPContactTemplate

**Framework**: Carplay  
**Kind**: class

A template that displays information about a person or a business.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPContactTemplate
```

#### Overview

The contact template can provide up to four contextual actions a user can invoke. For example, you might have an action that provides directions to the contact’s address.

When creating a contact template, you provide an instance of [`CPContact`](cpcontact.md) that contains a contact’s name and image, and optional subtitle. The object also contains any actions relevant to the contact. CarPlay provides specialized buttons for common actions, such as [`CPContactCallButton`](cpcontactcallbutton.md) or [`CPContactMessageButton`](cpcontactmessagebutton.md).

To display a contact template, call your interface controller’s [`pushTemplate(_:animated:completion:)`](cpinterfacecontroller/pushtemplate(_:animated:completion:).md) method to push it onto the navigation hierarchy, or [`presentTemplate(_:animated:completion:)`](cpinterfacecontroller/presenttemplate(_:animated:completion:).md) to present it modally.

> **Note**:  `CPContactTemplate` is only available in apps that have the communication or navigation entitlements.

## Topics

### Creating a Contact Template
- [init(contact: CPContact)](cpcontacttemplate/init(contact:).md)
  Creates a contact template that displays the provided contact.
### Configuring the Contact
- [var contact: CPContact](cpcontacttemplate/contact.md)
  The contact that the template displays.
- [class CPContact](cpcontact.md)
  A data object that contains information about a contact.

## Relationships

### Inherits From
- [CPTemplate](cptemplate.md)
### Conforms To
- [CPBarButtonProviding](cpbarbuttonproviding.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CarPlay/cpcontacttemplate)*