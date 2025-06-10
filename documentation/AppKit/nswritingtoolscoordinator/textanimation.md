# NSWritingToolsCoordinator.TextAnimation

**Framework**: AppKit  
**Kind**: enum

The types of animations that Writing Tools performs during an interactive update of your view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
enum TextAnimation
```

#### Overview

Use the `NSWritingToolsCoordinatorTextAnimation` constants to determine the type of animation that is occurring. During an interactive change to your view, Writing Tools creates animations to provide feedback about what’s happening. During the setup for each animation, Writing Tools reports the type of animation to the coordinator’s delegate, so you can perform additional actions related to that animation. For example, during an insertion animation, you might animate changes to other views in your interface.

## Topics

### Getting the animation types
- [NSWritingToolsCoordinator.TextAnimation.anticipate](nswritingtoolscoordinator/textanimation/anticipate.md)
  The animation that Writing Tools performs when waiting to receive results from the large language model.
- [NSWritingToolsCoordinator.TextAnimation.insert](nswritingtoolscoordinator/textanimation/insert.md)
  The animation that Writing Tools performs when inserting text into your view.
- [NSWritingToolsCoordinator.TextAnimation.remove](nswritingtoolscoordinator/textanimation/remove.md)
  The animation that Writing Tools performs when removing text from your view.
- [NSWritingToolsCoordinator.TextAnimation.anticipateInactive](nswritingtoolscoordinator/textanimation/anticipateinactive.md)
  The animation effect that Writing Tools performs when the view is waiting for results, but the system isn’t actively evaluating the text.
- [NSWritingToolsCoordinator.TextAnimation.translate](nswritingtoolscoordinator/textanimation/translate.md)
  The animation effect that Writing Tools performs on text situated after the insertion point.
### Initializers
- [init?(rawValue: Int)](nswritingtoolscoordinator/textanimation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSWritingToolsCoordinator.ContextScope](nswritingtoolscoordinator/contextscope.md)
  Options that indicate how much of your content Writing Tools requested.
- [NSWritingToolsCoordinator.TextReplacementReason](nswritingtoolscoordinator/textreplacementreason.md)
  Options that indicate whether Writing Tools is animating changes to your view’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/textanimation)*