# UIContextualAction.Handler

**Framework**: UIKit  
**Kind**: typealias

The handler block to call in response to the selection of an action.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
typealias Handler = (UIContextualAction, UIView, @escaping (Bool) -> Void) -> Void
```

## Parameters

- `action`: The object containing information about the selected action.
- `sourceView`: The view in which the action was displayed.
- `completionHandler`: The handler block for you to execute after you have performed the action. This block has no return value and takes the following parameter:

## See Also

- [var handler: UIContextualAction.Handler](uicontextualaction/handler-swift.property.md)
  The handler block to execute when the user selects the action.
- [var style: UIContextualAction.Style](uicontextualaction/style-swift.property.md)
  The style that applies to the action button.
- [UIContextualAction.Style](uicontextualaction/style-swift.enum.md)
  Constants indicating the style information that applies to the action button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextualaction/handler-swift.typealias)*