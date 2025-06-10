# NSWritingToolsCoordinator.TextAnimation.insert

**Framework**: AppKit  
**Kind**: case

The animation that Writing Tools performs when inserting text into your view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
case insert
```

#### Discussion

This type of animation shows the insertion of text to your view. When preparing for this animation, hide the text in the provided range if you haven’t already. If you support animating the reflow of your view’s text, you can also prepare any other animations you need. Writing Tools uses a preview object you provide to animate the insertion of the text.

## See Also

- [NSWritingToolsCoordinator.TextAnimation.anticipate](nswritingtoolscoordinator/textanimation/anticipate.md)
  The animation that Writing Tools performs when waiting to receive results from the large language model.
- [NSWritingToolsCoordinator.TextAnimation.remove](nswritingtoolscoordinator/textanimation/remove.md)
  The animation that Writing Tools performs when removing text from your view.
- [NSWritingToolsCoordinator.TextAnimation.anticipateInactive](nswritingtoolscoordinator/textanimation/anticipateinactive.md)
  The animation effect that Writing Tools performs when the view is waiting for results, but the system isn’t actively evaluating the text.
- [NSWritingToolsCoordinator.TextAnimation.translate](nswritingtoolscoordinator/textanimation/translate.md)
  The animation effect that Writing Tools performs on text situated after the insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/textanimation/insert)*