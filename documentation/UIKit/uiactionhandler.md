# UIActionHandler

**Framework**: UIKit  
**Kind**: typealias

A type that defines the closure for an action handler.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias UIActionHandler = (UIAction) -> Void
```

## Parameters

- `action`: The action selected by the user.

## See Also

- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIAction.Identifier?, discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State, handler: UIActionHandler)](uiaction/init(title:subtitle:image:identifier:discoverabilitytitle:attributes:state:handler:).md)
  Creates an action with the specified title, subtitle, image, identifier, discoverability title, attributes, state, and handler.
- [convenience init(title: String, image: UIImage?, identifier: UIAction.Identifier?, discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State, handler: UIActionHandler)](uiaction/init(title:image:identifier:discoverabilitytitle:attributes:state:handler:).md)
  Creates an action with the specified title, image, identifier, discoverability title, attributes, state, and handler.
- [class func captureTextFromCamera(responder: any UIResponder & UIKeyInput, identifier: UIAction.Identifier?) -> Self](uiaction/capturetextfromcamera(responder:identifier:).md)
  Creates an action for capturing text using the device’s camera.
- [UIAction.Identifier](uiaction/identifier-swift.struct.md)
  A type that represents an action identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionhandler)*