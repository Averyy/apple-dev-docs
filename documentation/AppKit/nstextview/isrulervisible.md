# isRulerVisible

**Framework**: AppKit  
**Kind**: property

A Boolean value that controls whether the scroll view enclosing text views sharing the receiver’s layout manager displays the ruler.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isRulerVisible: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) to show the ruler, [`false`](https://developer.apple.com/documentation/swift/false) to hide the ruler. By default, the ruler is hidden.

## See Also

- [func toggleRuler(Any?)](nstext/toggleruler(_:).md)
  This action method shows or hides the ruler, if the receiver is enclosed in a scroll view.
- [var usesRuler: Bool](nstextview/usesruler.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager use a ruler.
- [var usesInspectorBar: Bool](nstextview/usesinspectorbar.md)
  A Boolean value that indicates whether this text view uses the inspector bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/isrulervisible)*