# cancelTextAnimations(identifiers:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Used to support the presentation of grammar issues in text. If it is necessary to cancel the animation of one or more issues, call this to cancel theanimations.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func cancelTextAnimations(identifiers: [UUID])
```

```objc
- (void) cancelTextAnimationsWithIdentifiers:(NSArray<NSUUID *> *) identifiers;
```

## Discussion

The UUIDs passed in should be those returned when starting the animations. To cancel all ahimations, use [`stopWritingTools()`](./stopwritingtools%28%29.md) instead.

## See Also

### Managing grammar animations
- [func startTextAnimation(NSWritingToolsCoordinator.TextAnimation, for: NSRange, in: NSWritingToolsCoordinator.Context, writingDirection: NSWritingDirection) -> UUID?](./starttextanimation%28_,for,in,writingdirection%29.md)
- [func showGrammarPresentation(for: NSRange, in: NSWritingToolsCoordinator.Context) -> Bool](./showgrammarpresentation%28for,in%29.md)
  Used to support the presentation of grammar issues in text. When the user interacts with an issue, call this to bring up the relevant UI.
- [NSWritingToolsCoordinator.TextDecoration](./textdecoration.md)
  Use the `NSWritingToolsCoordinator.TextDecoration` constants to determine the type of decoration to be applied to a preview for grammar animation. The grammar animation needs previews of the text of the issue in two forms, without and with the grammar indication underline applied. If you use grammar animation, you must implement the delegate method [`writingToolsCoordinator(_:requestsPreviewFor:of:in:textDecoration:completion:)`](./delegate-swift.protocol/writingtoolscoordinator%28_,requestspreviewfor,of,in,textdecoration,completion%29.md) to provide both forms of previews, based on the specified decoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/canceltextanimations(identifiers:))*