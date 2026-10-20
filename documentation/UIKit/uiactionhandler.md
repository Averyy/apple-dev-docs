# UIActionHandler

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

A type that defines the closure for an action handler.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
typealias UIActionHandler = (UIAction) -> Void
```

```c
typedef void (^)(__kindof UIAction *) UIActionHandler;
```

## Parameters

- `action`: The action selected by the user.

## See Also

### Creating an action
- [convenience init(title: String, subtitle: String?, image: UIImage?, identifier: UIAction.Identifier?, discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State, handler: UIActionHandler)](./uiaction/init%28title,subtitle,image,identifier,discoverabilitytitle,attributes,state,handler%29.md)
  Creates an action with the specified title, subtitle, image, identifier, discoverability title, attributes, state, and handler.
- [convenience init(title: String, image: UIImage?, identifier: UIAction.Identifier?, discoverabilityTitle: String?, attributes: UIMenuElement.Attributes, state: UIMenuElement.State, handler: UIActionHandler)](./uiaction/init%28title,image,identifier,discoverabilitytitle,attributes,state,handler%29.md)
  Creates an action with the specified title, image, identifier, discoverability title, attributes, state, and handler.
- [class func captureTextFromCamera(responder: any UIResponder & UIKeyInput, identifier: UIAction.Identifier?) -> Self](./uiaction/capturetextfromcamera%28responder,identifier%29.md)
  Creates an action for capturing text using the device’s camera.
- [UIAction.Identifier](./uiaction/identifier-swift.struct.md)
  A type that represents an action identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionhandler)*