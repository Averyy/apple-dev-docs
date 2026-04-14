# selectionContainerViewBelowText

**Framework**: BrowserEngineKit  
**Kind**: property

An optional view you supply to draw text selection below the text.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
optional var selectionContainerViewBelowText: UIView? { get }
```

#### Discussion

The default value is `nil`. If you supply a view to this property, the framework layers the supplied view below [`textInputView`](betextinput/textinputview.md) to render text selection below the text, and includes text-selection handles in the rendering.

If you implement text selection using a [`textInputView`](betextinput/textinputview.md) subview instead, leave the value `nil`.

## See Also

- [var selectionContainerViewAboveText: UIView?](betextinput/selectioncontainerviewabovetext.md)
  An optional view you supply to draw text selection above the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/selectioncontainerviewbelowtext)*