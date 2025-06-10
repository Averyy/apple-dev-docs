# NSWritingToolsCoordinator.TextAnimation.anticipateInactive

**Framework**: AppKit  
**Kind**: case

The animation effect that Writing Tools performs when the view is waiting for results, but the system isn’t actively evaluating the text.

**Availability**:
- macOS 15.2+

## Declaration

```swift
case anticipateInactive
```

#### Discussion

When Writing Tools isn’t actively evaluating your text, it creates this animation. When preparing for this animation, display the text in the specified range with a foreground color of 50% grey.

## See Also

- [NSWritingToolsCoordinator.TextAnimation.anticipate](nswritingtoolscoordinator/textanimation/anticipate.md)
  The animation that Writing Tools performs when waiting to receive results from the large language model.
- [NSWritingToolsCoordinator.TextAnimation.insert](nswritingtoolscoordinator/textanimation/insert.md)
  The animation that Writing Tools performs when inserting text into your view.
- [NSWritingToolsCoordinator.TextAnimation.remove](nswritingtoolscoordinator/textanimation/remove.md)
  The animation that Writing Tools performs when removing text from your view.
- [NSWritingToolsCoordinator.TextAnimation.translate](nswritingtoolscoordinator/textanimation/translate.md)
  The animation effect that Writing Tools performs on text situated after the insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/textanimation/anticipateinactive)*