# showGrammarPresentation(for:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Used to support the presentation of grammar issues in text. When the user interacts with an issue, call this to bring up the relevant UI.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func showGrammarPresentation(for range: NSRange, in context: NSWritingToolsCoordinator.Context) -> Bool
```

```objc
- (BOOL) showGrammarPresentationForRange:(NSRange) range inContext:(NSWritingToolsCoordinatorContext *) context;
```

## Discussion

Pass in context and range to identify the issue the user selected. The context must match one of the contexts returned from [`writingToolsCoordinator(_:requestsContextsFor:completion:)`](./delegate-swift.protocol/writingtoolscoordinator%28_,requestscontextsfor,completion%29.md) and the range must match the range in the context of one of the grammar details returned for that context from [`writingToolsCoordinator(_:requestsGrammarResultsFor:completion:)`](./delegate-swift.protocol/writingtoolscoordinator%28_,requestsgrammarresultsfor,completion%29.md) Returns NO if the UI cannot be brought up.

## See Also

### Managing grammar animations
- [func startTextAnimation(NSWritingToolsCoordinator.TextAnimation, for: NSRange, in: NSWritingToolsCoordinator.Context, writingDirection: NSWritingDirection) -> UUID?](./starttextanimation%28_,for,in,writingdirection%29.md)
- [func cancelTextAnimations(identifiers: [UUID])](./canceltextanimations%28identifiers%29.md)
  Used to support the presentation of grammar issues in text. If it is necessary to cancel the animation of one or more issues, call this to cancel theanimations.
- [NSWritingToolsCoordinator.TextDecoration](./textdecoration.md)
  Use the `NSWritingToolsCoordinator.TextDecoration` constants to determine the type of decoration to be applied to a preview for grammar animation. The grammar animation needs previews of the text of the issue in two forms, without and with the grammar indication underline applied. If you use grammar animation, you must implement the delegate method [`writingToolsCoordinator(_:requestsPreviewFor:of:in:textDecoration:completion:)`](./delegate-swift.protocol/writingtoolscoordinator%28_,requestspreviewfor,of,in,textdecoration,completion%29.md) to provide both forms of previews, based on the specified decoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/showgrammarpresentation(for:in:))*