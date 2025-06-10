# NSWritingToolsCoordinator.TextReplacementReason.interactive

**Framework**: AppKit  
**Kind**: case

An option to animate the replacement of text in your view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
case interactive
```

#### Discussion

When Writing Tools requests an interactive change in your delegate’s `NSWritingToolsCoordinator/writingToolsCoordinator(_:replaceRange:inContext:proposedText:reason:animationParameters:completion:)` method, it passes a valid set of animation parameters to that method. Update your view’s text storage and use the provided [`NSWritingToolsCoordinator.AnimationParameters`](nswritingtoolscoordinator/animationparameters.md) type to create any view-specific animations you need to support the animated replacement of the text.

## See Also

- [NSWritingToolsCoordinator.TextReplacementReason.noninteractive](nswritingtoolscoordinator/textreplacementreason/noninteractive.md)
  An option to replace the text in your view without animating the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/textreplacementreason/interactive)*