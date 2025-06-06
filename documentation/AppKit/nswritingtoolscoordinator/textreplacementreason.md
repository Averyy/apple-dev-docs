# NSWritingToolsCoordinator.TextReplacementReason

**Framework**: AppKit  
**Kind**: enum

Options that indicate whether Writing Tools is animating changes to your view’s text.

**Availability**:
- macOS 15.2+

## Declaration

```swift
enum TextReplacementReason
```

#### Overview

During an operation, Writing Tools delivers replacement text to the delegate of the active [`NSWritingToolsCoordinator`](nswritingtoolscoordinator.md) object. Depending on the configured experience for your view, it delivers these changes as either interactive or noninteractive replacements. For interactive replacements, Writing Tools animates the change automatically and provides you with the information you need to perform any related animations.

## Topics

### Getting the reasons
- [NSWritingToolsCoordinator.TextReplacementReason.interactive](nswritingtoolscoordinator/textreplacementreason/interactive.md)
  An option to animate the replacement of text in your view.
- [NSWritingToolsCoordinator.TextReplacementReason.noninteractive](nswritingtoolscoordinator/textreplacementreason/noninteractive.md)
  An option to replace the text in your view without animating the change.
### Initializers
- [init?(rawValue: Int)](nswritingtoolscoordinator/textreplacementreason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSWritingToolsCoordinator.ContextScope](nswritingtoolscoordinator/contextscope.md)
  Options that indicate how much of your content Writing Tools requested.
- [NSWritingToolsCoordinator.TextAnimation](nswritingtoolscoordinator/textanimation.md)
  The types of animations that Writing Tools performs during an interactive update of your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/textreplacementreason)*