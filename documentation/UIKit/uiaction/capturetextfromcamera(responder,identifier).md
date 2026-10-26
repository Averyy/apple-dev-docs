# captureTextFromCamera(responder:identifier:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates an action for capturing text using the device’s camera.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class func captureTextFromCamera(responder: any UIResponder & UIKeyInput, identifier: UIAction.Identifier?) -> Self
```

```objc
+ (instancetype) captureTextFromCameraActionForResponder:(UIResponder<UIKeyInput> *) responder identifier:(UIActionIdentifier) identifier;
```

## Parameters

- `responder`: The [`UIKeyInput`](../uikeyinput.md) responder to send the [`captureTextFromCamera(_:)`](../uiresponder/capturetextfromcamera%28_%29.md) message to.
- `identifier`: The unique identifier for the action. Specify `nil` to let this method create a unique identifier for you.

## See Also

### Creating an action
- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIAction.Identifier?, discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State, handler: UIActionHandler)](./init%28title,subtitle,image,identifier,discoverabilitytitle,attributes,state,handler%29.md)
  Creates an action with the specified title, subtitle, image, identifier, discoverability title, attributes, state, and handler.
- [convenience init(title: String, image: UIImage?, identifier: UIAction.Identifier?, discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State, handler: UIActionHandler)](./init%28title,image,identifier,discoverabilitytitle,attributes,state,handler%29.md)
  Creates an action with the specified title, image, identifier, discoverability title, attributes, state, and handler.
- [UIAction.Identifier](./identifier-swift.struct.md)
  A type that represents an action identifier.
- [typealias UIActionHandler](../uiactionhandler.md)
  A type that defines the closure for an action handler.
- [+ actionWithTitle:image:identifier:handler:](./actionwithtitle_image_identifier_handler_.md)
  Creates an action with the specified title, image, identifier, and handler.
- [+ actionWithHandler:](./actionwithhandler_.md)
  Creates an action with the specified handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaction/capturetextfromcamera(responder:identifier:))*