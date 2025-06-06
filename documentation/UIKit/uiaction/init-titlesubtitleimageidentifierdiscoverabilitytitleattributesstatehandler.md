# init(title:subtitle:image:identifier:discoverabilityTitle:attributes:state:handler:)

**Framework**: UIKit  
**Kind**: init

Creates an action with the specified title, subtitle, image, identifier, discoverability title, attributes, state, and handler.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(title: String = "", subtitle: String? = nil, image: UIImage? = nil, identifier: UIAction.Identifier? = nil, discoverabilityTitle: String? = nil, attributes: UIMenuElement.Attributes = [], state: UIMenuElement.State = .off, handler: @escaping UIActionHandler)
```

## Parameters

- `title`: The title to display for the action.
- `subtitle`: The subtitle to display alongside the action’s title.
- `image`: The image to display next to the action’s  . Only the   menu system supports the display of an image, and only when the app is running in iOS.
- `identifier`: The unique identifier for the action. Specify   to let this method create a unique identifier for you.
- `discoverabilityTitle`: An elaborated title that explains the purpose of the action.
- `attributes`: The attributes indicating the style of the action.
- `state`: The initial state of the action.
- `handler`: The handler to invoke after a person selects the action. This handler has the following parameter:

## See Also

- [convenience init(title: String, image: UIImage?, identifier: UIAction.Identifier?, discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State, handler: UIActionHandler)](uiaction/init(title:image:identifier:discoverabilitytitle:attributes:state:handler:).md)
  Creates an action with the specified title, image, identifier, discoverability title, attributes, state, and handler.
- [class func captureTextFromCamera(responder: any UIResponder & UIKeyInput, identifier: UIAction.Identifier?) -> Self](uiaction/capturetextfromcamera(responder:identifier:).md)
  Creates an action for capturing text using the device’s camera.
- [UIAction.Identifier](uiaction/identifier-swift.struct.md)
  A type that represents an action identifier.
- [typealias UIActionHandler](uiactionhandler.md)
  A type that defines the closure for an action handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaction/init(title:subtitle:image:identifier:discoverabilitytitle:attributes:state:handler:))*