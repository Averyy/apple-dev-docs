# NSWritingToolsCoordinator.AnimationParameters

**Framework**: AppKit  
**Kind**: class

An object you use to configure additional tasks or animations to run alongside the Writing Tools animations.

**Availability**:
- macOS 15.2+

## Declaration

```swift
class AnimationParameters
```

#### Overview

When Writing Tools replaces text in one of your context objects, it provides an `NSWritingToolsCoordinator.AnimationParameters` object for you to use to configure any additional animations. During a Writing Tools session, you hide the text under evaluation and provide a targeted preview of your content. Writing Tools animations changes to that preview, but you might need to provide additional animations for other parts of your view’s content. For example, you might need to animate any layout changes caused by the insertion or removal of text in other parts of your view. Use this object to configure those animations.

You don’t create an `NSWritingToolsCoordinator.AnimationParameters` object directly. Instead, the system creates one and passes it to the `NSWritingToolsCoordinator/writingToolsCoordinator(_:replaceRange:inContext:proposedText:reason:animationParameters:completion:)` method of your [`NSWritingToolsCoordinator.Delegate`](nswritingtoolscoordinator/delegate-swift.protocol.md) object. Use that object to specify the blocks to run during and after the system animations.

## Topics

### Getting the animation values
- [var duration: CGFloat](nswritingtoolscoordinator/animationparameters/duration.md)
  The number of seconds it takes the system animations to run.
- [var delay: CGFloat](nswritingtoolscoordinator/animationparameters/delay.md)
  The number of seconds the system waits before starting its animations.
### Creating custom animations
- [var progressHandler: ((Float) -> Void)?](nswritingtoolscoordinator/animationparameters/progresshandler.md)
  A custom block that runs at the same time as the system animations.
- [var completionHandler: (() -> Void)?](nswritingtoolscoordinator/animationparameters/completionhandler.md)
  A custom block to run when the system animations finish.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Supporting Writing Tools via the pasteboard](supporting-writing-tools-via-the-pasteboard.md)
  Adopt a simplified version of the Writing Tools experience in a custom view using the pasteboard and macOS services.
- [Adding Writing Tools support to a custom AppKit view](adding-writing-tools-support-to-a-custom-nsview.md)
  Integrate Writing Tools support, including support for inline replacement animations, to your custom text views on macOS.
- [class NSWritingToolsCoordinator](nswritingtoolscoordinator.md)
  An object that manages interactions between Writing Tools and your custom text view.
- [NSWritingToolsCoordinator.Delegate](nswritingtoolscoordinator/delegate-swift.protocol.md)
  An interface that you use to manage interactions between Writing Tools and your custom text view.
- [NSWritingToolsCoordinator.Context](nswritingtoolscoordinator/context.md)
  A data object that you use to share your custom view’s text with Writing Tools.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/animationparameters)*