# NSWritingToolsCoordinator.TextAnimation.anticipate

**Framework**: AppKit  
**Kind**: case

The animation that Writing Tools performs when waiting to receive results from the large language model.

**Availability**:
- macOS 15.2+

## Declaration

```swift
case anticipate
```

#### Discussion

This type of animation applies a visual effect to the text that Writing Tools is evaluating. When preparing for this animation, hide the text that Writing Tools is about to evaluate. In the same space where that text appears, Writing Tools displays a preview image that you provide and animates changes to that image.

## See Also

- [NSWritingToolsCoordinator.TextAnimation.insert](nswritingtoolscoordinator/textanimation/insert.md)
  The animation that Writing Tools performs when inserting text into your view.
- [NSWritingToolsCoordinator.TextAnimation.remove](nswritingtoolscoordinator/textanimation/remove.md)
  The animation that Writing Tools performs when removing text from your view.
- [NSWritingToolsCoordinator.TextAnimation.anticipateInactive](nswritingtoolscoordinator/textanimation/anticipateinactive.md)
  The animation effect that Writing Tools performs when the view is waiting for results, but the system isn’t actively evaluating the text.
- [NSWritingToolsCoordinator.TextAnimation.translate](nswritingtoolscoordinator/textanimation/translate.md)
  The animation effect that Writing Tools performs on text situated after the insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/textanimation/anticipate)*