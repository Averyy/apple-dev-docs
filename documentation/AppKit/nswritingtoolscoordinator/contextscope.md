# NSWritingToolsCoordinator.ContextScope

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Options that indicate how much of your content Writing Tools requested.

**Availability**:
- macOS 15.2+

## Declaration

```swift
enum ContextScope
```

```c
enum NSWritingToolsCoordinatorContextScope : NSInteger;
```

## Overview

At the start of any Writing Tools interaction, you provide the text for the system to evaluate from your [`NSWritingToolsCoordinator.Delegate`](./delegate-swift.protocol.md) object. The request for your content comes with a scope constant that indicates how much of your view’s text to provide.

## Topics

### Getting the scope
- [NSWritingToolsCoordinator.ContextScope.userSelection](./contextscope/userselection.md)
  An option to provide only the view’s currently selected text.
- [NSWritingToolsCoordinator.ContextScope.fullDocument](./contextscope/fulldocument.md)
  An option to provide all of your view’s text.
- [NSWritingToolsCoordinator.ContextScope.visibleArea](./contextscope/visiblearea.md)
  An option to provide only the text in the currently visible portion of your view.
### Initializers
- [init?(rawValue: Int)](./contextscope/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the supporting types
- [NSWritingToolsCoordinator.TextReplacementReason](./textreplacementreason.md)
  Options that indicate whether Writing Tools is animating changes to your view’s text.
- [NSWritingToolsCoordinator.TextAnimation](./textanimation.md)
  The types of animations that Writing Tools performs during an interactive update of your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/contextscope)*