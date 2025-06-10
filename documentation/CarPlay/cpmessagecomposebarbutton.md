# CPMessageComposeBarButton

**Framework**: CarPlay  
**Kind**: class

A button that activates Siri and initiates the compose message flow.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPMessageComposeBarButton
```

#### Overview

> **Note**:  This button type does not use a handler. Instead, tapping this button activates Siri and initiates the compose message flow.

## Topics

### Creating a Message Compose Bar Button
- [init()](cpmessagecomposebarbutton/init.md)
  Creates a message compose button with a system-provided image.
- [init(image: UIImage)](cpmessagecomposebarbutton/init(image:).md)
  Creates a message compose button that displays a custom image.

## Relationships

### Inherits From
- [CPBarButton](cpbarbutton.md)
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

- [var backButton: CPBarButton?](cpbarbuttonproviding/backbutton.md)
  A button to display as the Back button on the navigation bar.
- [var leadingNavigationBarButtons: [CPBarButton]](cpbarbuttonproviding/leadingnavigationbarbuttons.md)
  An array of bar buttons to display on the leading side of the navigation bar.
- [var trailingNavigationBarButtons: [CPBarButton]](cpbarbuttonproviding/trailingnavigationbarbuttons.md)
  An array of bar buttons to display on the trailing side of the navigation bar.
- [class CPBarButton](cpbarbutton.md)
  A button for placement in a navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagecomposebarbutton)*