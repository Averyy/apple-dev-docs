# isRulerVisible

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls whether the scroll view enclosing text views sharing the receiver’s layout manager displays the ruler.

**Availability**:
- macOS

## Declaration

```swift
var isRulerVisible: Bool { get set }
```

```objc
@property (getter=isRulerVisible) BOOL rulerVisible;
```

#### Discussion

[`true`](../../Swift/true.md) to show the ruler, [`false`](../../Swift/false.md) to hide the ruler. By default, the ruler is hidden.

## See Also

### Related Documentation
- [func toggleRuler(Any?)](../nstext/toggleruler%28_%29.md)
  This action method shows or hides the ruler, if the receiver is enclosed in a scroll view.
### Using text formatting controls
- [var usesRuler: Bool](./usesruler.md)
  A Boolean value that controls whether the text views sharing the receiver’s layout manager use a ruler.
- [var usesInspectorBar: Bool](./usesinspectorbar.md)
  A Boolean value that indicates whether this text view uses the inspector bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/isrulervisible)*