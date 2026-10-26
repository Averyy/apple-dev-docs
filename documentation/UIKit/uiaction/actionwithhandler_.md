# actionWithHandler:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates an action with the specified handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) actionWithHandler:(UIActionHandler) handler;
```

## Parameters

- `handler`: The handler to invoke after a person selects the action. This handler has the following parameter:

  - **action**: The action that a person selects.

## See Also

### Creating an action
- [+ actionWithTitle:image:identifier:handler:](./actionwithtitle_image_identifier_handler_.md)
  Creates an action with the specified title, image, identifier, and handler.
- [class func captureTextFromCamera(responder: any UIResponder & UIKeyInput, identifier: UIAction.Identifier?) -> Self](./capturetextfromcamera%28responder,identifier%29.md)
  Creates an action for capturing text using the device’s camera.
- [UIAction.Identifier](./identifier-swift.struct.md)
  A type that represents an action identifier.
- [typealias UIActionHandler](../uiactionhandler.md)
  A type that defines the closure for an action handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaction/actionwithhandler:)*