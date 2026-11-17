# CPMessageComposeBarButton

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A button that activates Siri and initiates the process for composing a message.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPMessageComposeBarButton
```

```objc
@interface CPMessageComposeBarButton : CPBarButton
```

## Overview

Include a `CPMessageComposeBarButton` in your template’s navigation bar to support the creation of new messages in your communication app. When someone taps the button, CarPlay launches Siri to compose the message. The message composition workflow relies on your app’s SiriKit support for messages to build and send the message.

> **Note**: This button works only in communication apps.

## Topics

### Creating a message compose bar button
- [init()](./cpmessagecomposebarbutton/init%28%29.md)
  Creates a button for composing messages that uses the system-provided image.
- [init(image: UIImage)](./cpmessagecomposebarbutton/init%28image%29.md)
  Creates a button for composing messages that uses a custom image you provide.
- [+ new](./cpmessagecomposebarbutton/new.md)

## Relationships

### Inherits From
- [CPBarButton](./cpbarbutton.md)
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

### Navigation bar
- [protocol CPBarButtonProviding](./cpbarbuttonproviding.md)
  The interface templates you use to manage buttons in the navigation bar.
- [class CPBarButton](./cpbarbutton.md)
  A button that appears in a navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagecomposebarbutton)*