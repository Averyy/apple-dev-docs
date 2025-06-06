# writingToolsCoordinator(_:select:in:completion:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Asks the delegate to update your view’s current text selection.

**Availability**:
- macOS 15.2+

## Declaration

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator, select ranges: [NSValue], in context: NSWritingToolsCoordinator.Context) async
```

## Mentions

- [Adding Writing Tools support to a custom AppKit view](adding-writing-tools-support-to-a-custom-nsview.md)

#### Discussion

As Writing Tools suggests changes to your view’s text, it calls this method to update the text selection accordingly. Use this method to update the current selection in your view’s text storage. When you finish making the changes, call the provided completion block to let Writing Tools know you’re finished.

## Parameters

- `writingToolsCoordinator`: The coordinator object making the change   to your view.
- `ranges`: One or more ranges of text to select. Each range is relative   to the text in your context object, and it’s your responsibility to   match each location to the correct location in your text storage. If   you initialized the context object with the entire contents of your   view’s text storage, you can use the ranges as-is to access that text   storage. However, if you initialized the context object with only a   portion of your view’s text, add the starting location of your context   object’s text to each value to get the correct range for that text storage.
- `context`: The context object you use to identify the associated text storage.
- `completion`: The completion handler to execute when your delegate finishes updating   the selection. The handler has no parameters or return value. You must   call this handler at some point during the implementation of your method.

## See Also

- [func writingToolsCoordinator(NSWritingToolsCoordinator, replace: NSRange, in: NSWritingToolsCoordinator.Context, proposedText: NSAttributedString, reason: NSWritingToolsCoordinator.TextReplacementReason, animationParameters: NSWritingToolsCoordinator.AnimationParameters?, completion: (NSAttributedString?) -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:replace:in:proposedtext:reason:animationparameters:completion:).md)
  Tells the delegate that there are text changes to incorporate into the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:select:in:completion:))*