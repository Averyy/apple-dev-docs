# NSWritingToolsCoordinator.TextReplacementReason.noninteractive

**Framework**: AppKit  
**Kind**: case

An option to replace the text in your view without animating the change.

**Availability**:
- macOS 15.2+

## Declaration

```swift
case noninteractive
```

#### Discussion

When Writing Tools requests a noninteractive change in your delegate’s [`writingToolsCoordinator(_:replace:in:proposedText:reason:animationParameters:completion:)`](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:replace:in:proposedtext:reason:animationparameters:completion:).md) method, update your view’s text storage without animating the change.

## See Also

- [NSWritingToolsCoordinator.TextReplacementReason.interactive](nswritingtoolscoordinator/textreplacementreason/interactive.md)
  An option to animate the replacement of text in your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/textreplacementreason/noninteractive)*