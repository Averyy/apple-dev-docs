# UIContextualAction.Handler

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

The handler block to call in response to the selection of an action.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
@MainActor
typealias Handler = (UIContextualAction, UIView, @escaping (Bool) -> Void) -> Void
```

```c
typedef void (^)(UIContextualAction *, __kindof UIView *, void (^)(_Bool)) UIContextualActionHandler;
```

## Parameters

- `action`: The object containing information about the selected action.
- `sourceView`: The view in which the action was displayed.
- `completionHandler`: The handler block for you to execute after you have performed the action. This block has no return value and takes the following parameter:

  - **actionPerformed**: A Boolean value indicating whether you performed the action. Specify [`true`](../../Swift/true.md) if you performed the action or [`false`](../../Swift/false.md) if you were unable to perform the action for some reason.

## See Also

### Getting the configuration details
- [var handler: UIContextualAction.Handler](./handler-swift.property.md)
  The handler block to execute when the user selects the action.
- [var style: UIContextualAction.Style](./style-swift.property.md)
  The style that applies to the action button.
- [UIContextualAction.Style](./style-swift.enum.md)
  Constants indicating the style information that applies to the action button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextualaction/handler-swift.typealias)*