# NSWritingToolsCoordinator.ContextScope

**Framework**: AppKit  
**Kind**: enum

Options that indicate how much of your content Writing Tools requested.

**Availability**:
- macOS 15.2+

## Declaration

```swift
enum ContextScope
```

#### Overview

At the start of any Writing Tools interaction, you provide the text for the system to evaluate from your `NS/UIWritingToolsCoordinator/Delegate` object. The request for your content comes with a scope constant that indicates how much of your view’s text to provide.

## Topics

### Getting the scope
- [NSWritingToolsCoordinator.ContextScope.userSelection](nswritingtoolscoordinator/contextscope/userselection.md)
  An option to provide only the view’s currently selected text.
- [NSWritingToolsCoordinator.ContextScope.fullDocument](nswritingtoolscoordinator/contextscope/fulldocument.md)
  An option to provide all of your view’s text.
- [NSWritingToolsCoordinator.ContextScope.visibleArea](nswritingtoolscoordinator/contextscope/visiblearea.md)
  An option to provide only the text in the currently visible portion of your view.
### Initializers
- [init?(rawValue: Int)](nswritingtoolscoordinator/contextscope/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSWritingToolsCoordinator.TextReplacementReason](nswritingtoolscoordinator/textreplacementreason.md)
  Options that indicate whether Writing Tools is animating changes to your view’s text.
- [NSWritingToolsCoordinator.TextAnimation](nswritingtoolscoordinator/textanimation.md)
  The types of animations that Writing Tools performs during an interactive update of your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/contextscope)*