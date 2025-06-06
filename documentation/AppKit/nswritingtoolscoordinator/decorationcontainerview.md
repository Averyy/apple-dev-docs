# decorationContainerView

**Framework**: AppKit  
**Kind**: property

The view that Writing Tools uses to display background decorations such as proofreading marks.

**Availability**:
- macOS 15.2+

## Declaration

```swift
@MainActor
weak var decorationContainerView: NSView? { get set }
```

#### Discussion

Writing Tools uses the view in this property to host proofreading marks and other visual elements that show any suggested changes. Set this property to a subview situated visibly below the text in your custom text view. It’s also satisfactory to place this view visually in front of the text. Make sure the size of the view is big enough to cover all of the affected text. If you don’t assign a value to this property, the coordinator places its own decoration view behind the subviews in your custom view. The default value of this property is `nil`.

If you display your view’s text using multiple text containers, implement the `NSWritingToolsCoordinator/Delegate/writingToolsCoordinator(_:singleContainerSubrangesOf:in:)` and `NSWritingToolsCoordinator/Delegate/writingToolsCoordinator(_:decorationContainerViewFor:in:)` methods to provide separate decoration views for each container.

## See Also

- [var effectContainerView: NSView?](nswritingtoolscoordinator/effectcontainerview.md)
  The view that Writing Tools uses to display visual effects during the text-rewriting process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/decorationcontainerview)*