# captureTextFromCamera(responder:identifier:)

**Framework**: UIKit  
**Kind**: method

Creates an action for capturing text using the device’s camera.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func captureTextFromCamera(responder: any UIResponder & UIKeyInput, identifier: UIAction.Identifier?) -> Self
```

## Parameters

- `responder`: The   responder to send the   message to.
- `identifier`: The unique identifier for the action. Specify   to let this method create a unique identifier for you.

## See Also

- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIAction.Identifier?, discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State, handler: UIActionHandler)](uiaction/init(title:subtitle:image:identifier:discoverabilitytitle:attributes:state:handler:).md)
  Creates an action with the specified title, subtitle, image, identifier, discoverability title, attributes, state, and handler.
- [convenience init(title: String, image: UIImage?, identifier: UIAction.Identifier?, discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State, handler: UIActionHandler)](uiaction/init(title:image:identifier:discoverabilitytitle:attributes:state:handler:).md)
  Creates an action with the specified title, image, identifier, discoverability title, attributes, state, and handler.
- [UIAction.Identifier](uiaction/identifier-swift.struct.md)
  A type that represents an action identifier.
- [typealias UIActionHandler](uiactionhandler.md)
  A type that defines the closure for an action handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaction/capturetextfromcamera(responder:identifier:))*