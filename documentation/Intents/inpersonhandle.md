# INPersonHandle

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The identifying information for a user of your app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INPersonHandle
```

```objc
@interface INPersonHandle : NSObject
```

#### Overview

An [`INPersonHandle`](./inpersonhandle.md) object contains information that you use to uniquely identify a user of your app. When resolving a person associated with an intent, you might create instances of this class and add them to an [`INPerson`](./inperson.md) object when resolving an intent involving that person. Handles contain unique information such as an email address or phone number.

## Topics

### Initializing a Person Handle
- [init(value: String?, type: INPersonHandleType, label: INPersonHandleLabel?)](./inpersonhandle/init%28value,type,label%29.md)
  Initializes and returns a person handle with the specified data.
- [convenience init(value: String?, type: INPersonHandleType)](./inpersonhandle/init%28value,type%29.md)
  Initializes and returns a person handle with the specified data.
### Getting the Handle Information
- [var type: INPersonHandleType](./inpersonhandle/type.md)
  The type of information contained in the handle.
- [var value: String?](./inpersonhandle/value.md)
  The data for the handle.
- [var label: INPersonHandleLabel?](./inpersonhandle/label.md)
  A standard label that describes the meaning of the information.
### Constants
- [enum INPersonHandleType](./inpersonhandletype.md)
  Constants indicating the types of data that can be associated with a person handle.
### Initializers
- [init?(coder: NSCoder)](./inpersonhandle/init%28coder%29.md)

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
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Contacts
- [class INPerson](./inperson.md)
  Information about a person participating in a SiriKit interaction.
- [struct INPersonHandleLabel](./inpersonhandlelabel.md)
  Constants describing how the person handle relates to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpersonhandle)*