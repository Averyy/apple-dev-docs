# startTextAnimation(_:for:in:writingDirection:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 27.0+

## Declaration

```swift
func startTextAnimation(_ textAnimation: NSWritingToolsCoordinator.TextAnimation, for range: NSRange, in context: NSWritingToolsCoordinator.Context, writingDirection: NSWritingDirection) -> UUID?
```

```objc
- (NSUUID *) startTextAnimation:(NSWritingToolsCoordinatorTextAnimation) textAnimation forRange:(NSRange) range inContext:(NSWritingToolsCoordinatorContext *) context writingDirection:(NSWritingDirection) writingDirection;
```

## See Also

### Managing grammar animations
- [func showGrammarPresentation(for: NSRange, in: NSWritingToolsCoordinator.Context) -> Bool](./showgrammarpresentation%28for,in%29.md)
  Used to support the presentation of grammar issues in text. When the user interacts with an issue, call this to bring up the relevant UI.
- [func cancelTextAnimations(identifiers: [UUID])](./canceltextanimations%28identifiers%29.md)
  Used to support the presentation of grammar issues in text. If it is necessary to cancel the animation of one or more issues, call this to cancel theanimations.
- [NSWritingToolsCoordinator.TextDecoration](./textdecoration.md)
  Use the `NSWritingToolsCoordinator.TextDecoration` constants to determine the type of decoration to be applied to a preview for grammar animation. The grammar animation needs previews of the text of the issue in two forms, without and with the grammar indication underline applied. If you use grammar animation, you must implement the delegate method [`writingToolsCoordinator(_:requestsPreviewFor:of:in:textDecoration:completion:)`](./delegate-swift.protocol/writingtoolscoordinator%28_,requestspreviewfor,of,in,textdecoration,completion%29.md) to provide both forms of previews, based on the specified decoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/starttextanimation(_:for:in:writingdirection:))*