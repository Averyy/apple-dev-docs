# CPMessageComposeBarButton

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
class CPMessageComposeBarButton
```

```objc
@interface CPMessageComposeBarButton : CPBarButton
```

## Overview

> **Note**:  This button type does not use a handler. Instead, tapping this button activates Siri and initiates the compose message flow.

## Topics

### Creating a Message Compose Bar Button
- [init()](./cpmessagecomposebarbutton/init%28%29.md)
  Creates a message compose button with a system-provided image.
- [init(image: UIImage)](./cpmessagecomposebarbutton/init%28image%29.md)
  Creates a message compose button that displays a custom image.
- [+ new](./cpmessagecomposebarbutton/new.md)
  Creates a message compose button with a system-provided image.

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

### Providing Navigation Bar Buttons
- [var backButton: CPBarButton?](./cpbarbuttonproviding/backbutton.md)
  A button to display as the Back button on the navigation bar.
- [var leadingNavigationBarButtons: [CPBarButton]](./cpbarbuttonproviding/leadingnavigationbarbuttons.md)
  An array of bar buttons to display on the leading side of the navigation bar.
- [var trailingNavigationBarButtons: [CPBarButton]](./cpbarbuttonproviding/trailingnavigationbarbuttons.md)
  An array of bar buttons to display on the trailing side of the navigation bar.
- [class CPBarButton](./cpbarbutton.md)
  A button for placement in a navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagecomposebarbutton)*