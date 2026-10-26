# INObject

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A representation of a custom intent parameter or response property.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class INObject
```

```objc
@interface INObject : NSObject
```

#### Overview

Use [`INObject`](./inobject.md) to create custom parameters and response properties for intent data that doesn’t fit into one of the System Types, such as Boolean, Duration, or Location. Define custom types and associate them with your custom intents and responses in the Intent Definition file.

Xcode uses the type defined in the Intent Definition file to generate a subclass of `INObject`. Create an instance of this subclass to structure data in intents and intent responses.

> 💡 **Tip**:  If your app supports intents on iOS 12, use the Custom parameter type in your Intent Definition file and create instances of [`INObject`](./inobject.md) (not a subclass) for custom parameters of those intents.

## Topics

### Creating a Custom Object
- [convenience init(identifier: String?, display: String, subtitle: String?, image: INImage?)](./inobject/init%28identifier,display,subtitle,image%29.md)
  Creates a custom intent object with full display information.
- [convenience init(identifier: String?, display: String)](./inobject/init%28identifier,display%29.md)
  Creates a custom intent object with the specified identifier and display string.
- [convenience init(identifier: String?, display: String, pronunciationHint: String?, subtitle: String?, image: INImage?)](./inobject/init%28identifier,display,pronunciationhint,subtitle,image%29.md)
  Creates a custom intent object with the specified attributes.
- [init(identifier: String?, display: String, pronunciationHint: String?)](./inobject/init%28identifier,display,pronunciationhint%29.md)
  Creates a custom intent object with the specified attributes.
### Displaying the Object
- [var displayString: String](./inobject/displaystring.md)
  A name or description for the custom intent object.
- [var subtitleString: String?](./inobject/subtitlestring.md)
  Additional details about the custom intent object.
- [var displayImage: INImage?](./inobject/displayimage.md)
  An image to display alongside the custom intent object’s text.
### Describing the Object for the System
- [var identifier: String?](./inobject/identifier.md)
  A string that identifies the custom intent object within your app.
- [var pronunciationHint: String?](./inobject/pronunciationhint.md)
  A hint that describes how to pronounce the custom intent object.
- [var alternativeSpeakableMatches: [INSpeakableString]?](./inobject/alternativespeakablematches.md)
  An array of alternative speakable strings that identify the object.
### Initializers
- [init?(coder: NSCoder)](./inobject/init%28coder%29.md)
- [convenience init(identifier: String?, displayString: String)](./inobject/init%28identifier,displaystring%29.md)
- [init(identifier: String?, displayString: String, pronunciationHint: String?)](./inobject/init%28identifier,displaystring,pronunciationhint%29.md)
- [convenience init(identifier: String?, displayString: String, pronunciationHint: String?, subtitleString: String?, displayImage: INImage?)](./inobject/init%28identifier,displaystring,pronunciationhint,subtitlestring,displayimage%29.md)
- [convenience init(identifier: String?, displayString: String, subtitleString: String?, displayImage: INImage?)](./inobject/init%28identifier,displaystring,subtitlestring,displayimage%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INSpeakable](./inspeakable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Custom Objects
- [class INObjectCollection](./inobjectcollection.md)
- [class INObjectSection](./inobjectsection.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inobject)*