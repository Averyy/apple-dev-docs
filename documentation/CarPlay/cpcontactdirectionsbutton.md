# CPContactDirectionsButton

**Framework**: CarPlay  
**Kind**: class

A button for getting directions to the contact’s location.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class CPContactDirectionsButton
```

#### Overview

Use this button to get directions to the location of the template’s contact.

If your app doesn’t provide turn-by-turn navigation, use the `maps` URL scheme to launch the most recent navigation app. Call your template application scene’s [`open(_:options:completionHandler:)`](https://developer.apple.com/documentation/UIKit/UIScene/open(_:options:completionHandler:)) method and pass a URL that embeds the contact’s location. CarPlay provides this scene to your [`CPTemplateApplicationSceneDelegate`](cptemplateapplicationscenedelegate.md) when the scene connects.

## Topics

### Creating a Contact Directions Button
- [init(handler: ((CPButton) -> Void)?)](cpcontactdirectionsbutton/init(handler:).md)
  Creates a button that invokes a handler when the user taps it.

## Relationships

### Inherits From
- [CPButton](cpbutton.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var actions: [CPButton]?](cpcontact/actions.md)
  The actions that the template displays for this contact.
- [class CPContactCallButton](cpcontactcallbutton.md)
  A button for calling the contact.
- [class CPContactMessageButton](cpcontactmessagebutton.md)
  A button that activates Siri and initiates the compose message flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontactdirectionsbutton)*