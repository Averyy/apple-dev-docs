# CPMessageGridItemConfiguration

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A type that associates message-related information with a grid button.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class CPMessageGridItemConfiguration
```

```objc
@interface CPMessageGridItemConfiguration : NSObject
```

## Overview

Add a `CPMessageGridItemConfiguration` object to a [`CPGridButton`](./cpgridbutton.md) that represents one of your app’s conversations. This type stores an app-specific conversation identifier, which you can use to look up the conversation in your app’s data structures. It also contains a Boolean value to indicate whether the conversation contains unread messages.

## Topics

### Creating a configuration object
- [init(conversationIdentifier: String, unread: Bool)](./cpmessagegriditemconfiguration/init%28conversationidentifier,unread%29.md)
  Creates the configuration object with a conversation identifier and Boolean value.
### Getting the conversation identifier
- [var conversationIdentifier: String](./cpmessagegriditemconfiguration/conversationidentifier.md)
  The string you use to uniquely identify the conversation in your app.
### Updating the message’s unread status
- [var isUnread: Bool](./cpmessagegriditemconfiguration/isunread.md)
  A Boolean value that indicates whether the conversation contains unread messages.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Grids
- [class CPGridTemplate](./cpgridtemplate.md)
  A template that displays and manages a grid of items.
- [class CPGridButton](./cpgridbutton.md)
  A menu item button displayed on a grid template.
- [let CPGridTemplateMaximumItems: Int](./cpgridtemplatemaximumitems.md)
  The maximum number of buttons that a grid template displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagegriditemconfiguration)*