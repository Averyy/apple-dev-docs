# actionWithTitle:image:identifier:handler:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates an action with the specified title, image, identifier, and handler.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) actionWithTitle:(NSString *) title image:(UIImage *) image identifier:(UIActionIdentifier) identifier handler:(UIActionHandler) handler;
```

#### Return Value

A newly initialized action object.

## Parameters

- `title`: The title to display for the action.
- `image`: The image to display next to the action’s `title`. Only the [`context`](../uimenusystem/context.md) menu system supports the display of an image, and only when the app is running in iOS.
- `identifier`: The unique identifier for the action. Specify `nil` to let this method create a unique identifier for you.
- `handler`: The handler to invoke after a person selects the action. This handler has the following parameter:

  - **action**: The action that a person selects.

## See Also

### Creating an action
- [+ actionWithHandler:](./actionwithhandler_.md)
  Creates an action with the specified handler.
- [class func captureTextFromCamera(responder: any UIResponder & UIKeyInput, identifier: UIAction.Identifier?) -> Self](./capturetextfromcamera%28responder,identifier%29.md)
  Creates an action for capturing text using the device’s camera.
- [UIAction.Identifier](./identifier-swift.struct.md)
  A type that represents an action identifier.
- [typealias UIActionHandler](../uiactionhandler.md)
  A type that defines the closure for an action handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaction/actionwithtitle:image:identifier:handler:)*