# CPContact

**Framework**: CarPlay  
**Kind**: class

A data object that contains information about a contact.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPContact
```

#### Overview

`CPContact` is an object that represents information about a person or a business, and can include a set of contextually relevant actions that a user can perform when CarPlay displays the contact, such as getting directions to its location.

You display a contact using [`CPContactTemplate`](cpcontacttemplate.md). The template manages the appearance of the contact, and can display up to four action buttons. After displaying it, you can update the buttons for the template by assigning a new array to the contact’s [`actions`](cpcontact/actions.md) property.

The framework provides specialized buttons for common actions, such as [`CPContactCallButton`](cpcontactcallbutton.md) or [`CPContactMessageButton`](cpcontactmessagebutton.md).

## Topics

### Creating a Contact
- [init(name: String, image: UIImage)](cpcontact/init(name:image:).md)
  Creates a contact with a name and an image.
### Configuring the Contact’s Attributes
- [var image: UIImage](cpcontact/image.md)
  The contact’s image.
- [var name: String](cpcontact/name.md)
  The contact’s name.
- [var subtitle: String?](cpcontact/subtitle.md)
  A subtitle that the template displays in addition to the contact’s name.
- [var informativeText: String?](cpcontact/informativetext.md)
  Additional text that the template displays.
### Managing Interactions with the Contact
- [var actions: [CPButton]?](cpcontact/actions.md)
  The actions that the template displays for this contact.
- [class CPContactCallButton](cpcontactcallbutton.md)
  A button for calling the contact.
- [class CPContactDirectionsButton](cpcontactdirectionsbutton.md)
  A button for getting directions to the contact’s location.
- [class CPContactMessageButton](cpcontactmessagebutton.md)
  A button that activates Siri and initiates the compose message flow.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var contact: CPContact](cpcontacttemplate/contact.md)
  The contact that the template displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontact)*