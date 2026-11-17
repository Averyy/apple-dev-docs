# CPContactMessageButton

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A button that activates Siri and initiates the compose message flow.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPContactMessageButton
```

```objc
@interface CPContactMessageButton : CPButton
```

## Overview

> ❗ **Important**:  This subclass of [`CPButton`](./cpbutton.md) doesn’t use a handler. Instead, tapping this button activates Siri and launches the compose message flow using the contact information in the [`phoneOrEmail`](./cpcontactmessagebutton/phoneoremail.md) property.

## Topics

### Creating a contact message button
- [init(phoneOrEmail: String)](./cpcontactmessagebutton/init%28phoneoremail%29.md)
  Creates a contact message button with the provided contact information.
### Getting the contact information
- [var phoneOrEmail: String](./cpcontactmessagebutton/phoneoremail.md)
  The contact’s phone number or email address.

## Relationships

### Inherits From
- [CPButton](./cpbutton.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Contacts
- [class CPContactTemplate](./cpcontacttemplate.md)
  A template that displays information about a person or a business.
- [class CPContact](./cpcontact.md)
  A data object that contains information about a contact.
- [class CPContactCallButton](./cpcontactcallbutton.md)
  A button for calling the contact.
- [class CPContactDirectionsButton](./cpcontactdirectionsbutton.md)
  A button for getting directions to the contact’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontactmessagebutton)*