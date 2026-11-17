# CPContact

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A data object that contains information about a contact.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPContact
```

```objc
@interface CPContact : NSObject
```

## Overview

`CPContact` is an object that represents information about a person or a business, and can include a set of contextually relevant actions that a user can perform when CarPlay displays the contact, such as getting directions to its location.

You display a contact using [`CPContactTemplate`](./cpcontacttemplate.md). The template manages the appearance of the contact, and can display up to four action buttons. After displaying it, you can update the buttons for the template by assigning a new array to the contact’s [`actions`](./cpcontact/actions.md) property.

The framework provides specialized buttons for common actions, such as [`CPContactCallButton`](./cpcontactcallbutton.md) or [`CPContactMessageButton`](./cpcontactmessagebutton.md).

## Topics

### Creating a contact
- [init(name: String, image: UIImage)](./cpcontact/init%28name,image%29.md)
  Creates a contact with a name and an image.
### Configuring the contact’s attributes
- [var image: UIImage](./cpcontact/image.md)
  The contact’s image.
- [var name: String](./cpcontact/name.md)
  The contact’s name.
- [var subtitle: String?](./cpcontact/subtitle.md)
  A subtitle that the template displays in addition to the contact’s name.
- [var informativeText: String?](./cpcontact/informativetext.md)
  Additional text that the template displays.
### Managing interactions with the contact
- [var actions: [CPButton]?](./cpcontact/actions.md)
  The actions that the template displays for this contact.
- [class CPContactCallButton](./cpcontactcallbutton.md)
  A button for calling the contact.
- [class CPContactDirectionsButton](./cpcontactdirectionsbutton.md)
  A button for getting directions to the contact’s location.
- [class CPContactMessageButton](./cpcontactmessagebutton.md)
  A button that activates Siri and initiates the compose message flow.
### Initializers
- [init?(coder: NSCoder)](./cpcontact/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Configuring the contact
- [var contact: CPContact](./cpcontacttemplate/contact.md)
  The contact that the template displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontact)*