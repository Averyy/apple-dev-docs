# usesRuler

**Framework**: AppKit  
**Kind**: property

A Boolean value that controls whether the text views sharing the receiver’s layout manager use a ruler.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var usesRuler: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) to cause text views sharing the receiver’s layout manager to respond to [`NSRulerView`](nsrulerview.md) client messages and to paragraph-related menu actions, and update the ruler (when visible) as the selection changes with its paragraph and tab attributes, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var rangeForUserParagraphAttributeChange: NSRange](nstextview/rangeforuserparagraphattributechange.md)
  The range of characters affected by an action method that changes paragraph (not character) attributes.
- [var isRulerVisible: Bool](nstextview/isrulervisible.md)
  A Boolean value that controls whether the scroll view enclosing text views sharing the receiver’s layout manager displays the ruler.
- [var usesInspectorBar: Bool](nstextview/usesinspectorbar.md)
  A Boolean value that indicates whether this text view uses the inspector bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/usesruler)*