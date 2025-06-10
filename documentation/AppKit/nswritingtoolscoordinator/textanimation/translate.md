# NSWritingToolsCoordinator.TextAnimation.translate

**Framework**: AppKit  
**Kind**: case

The animation effect that Writing Tools performs on text situated after the insertion point.

**Availability**:
- macOS 15.2+

## Declaration

```swift
case translate
```

#### Discussion

When Writing Tools inserts text at a given location, it creates an animation to make room for the new text. When preparing for this animation, hide the text between the insertion point and the end of your text storage. When finishing the animation, show the text again.

## See Also

- [NSWritingToolsCoordinator.TextAnimation.anticipate](nswritingtoolscoordinator/textanimation/anticipate.md)
  The animation that Writing Tools performs when waiting to receive results from the large language model.
- [NSWritingToolsCoordinator.TextAnimation.insert](nswritingtoolscoordinator/textanimation/insert.md)
  The animation that Writing Tools performs when inserting text into your view.
- [NSWritingToolsCoordinator.TextAnimation.remove](nswritingtoolscoordinator/textanimation/remove.md)
  The animation that Writing Tools performs when removing text from your view.
- [NSWritingToolsCoordinator.TextAnimation.anticipateInactive](nswritingtoolscoordinator/textanimation/anticipateinactive.md)
  The animation effect that Writing Tools performs when the view is waiting for results, but the system isn’t actively evaluating the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/textanimation/translate)*