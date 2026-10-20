# NSWritingToolsCoordinator.TextReplacementReason.interactive

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

An option to animate the replacement of text in your view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
case interactive
```

```c
NSWritingToolsCoordinatorTextReplacementReasonInteractive
```

#### Discussion

When Writing Tools requests an interactive change in your delegate’s [`writingToolsCoordinator(_:replace:in:proposedText:reason:animationParameters:completion:)`](../delegate-swift.protocol/writingtoolscoordinator%28_,replace,in,proposedtext,reason,animationparameters,completion%29.md) method, it passes a valid set of animation parameters to that method. Update your view’s text storage and use the provided [`NSWritingToolsCoordinator.AnimationParameters`](../animationparameters.md) type to create any view-specific animations you need to support the animated replacement of the text.

## See Also

### Getting the reasons
- [NSWritingToolsCoordinator.TextReplacementReason.noninteractive](./noninteractive.md)
  An option to replace the text in your view without animating the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/textreplacementreason/interactive)*