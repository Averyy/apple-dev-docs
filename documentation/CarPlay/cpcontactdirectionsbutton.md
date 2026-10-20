# CPContactDirectionsButton

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A button for getting directions to the contact’s location.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPContactDirectionsButton
```

```objc
@interface CPContactDirectionsButton : CPButton
```

#### Overview

Use this button to get directions to the location of the template’s contact.

If your app doesn’t provide turn-by-turn navigation, use the `maps` URL scheme to launch the most recent navigation app. Call your template application scene’s [`open(_:options:completionHandler:)`](../UIKit/uiscene/open%28_,options,completionhandler%29.md) method and pass a URL that embeds the contact’s location. CarPlay provides this scene to your [`CPTemplateApplicationSceneDelegate`](./cptemplateapplicationscenedelegate.md) when the scene connects.

## Topics

### Creating a Contact Directions Button
- [init(handler: ((CPButton) -> Void)?)](./cpcontactdirectionsbutton/init%28handler%29.md)
  Creates a button that invokes a handler when the user taps it.

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

### Managing Interactions with the Contact
- [var actions: [CPButton]?](./cpcontact/actions.md)
  The actions that the template displays for this contact.
- [class CPContactCallButton](./cpcontactcallbutton.md)
  A button for calling the contact.
- [class CPContactMessageButton](./cpcontactmessagebutton.md)
  A button that activates Siri and initiates the compose message flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontactdirectionsbutton)*