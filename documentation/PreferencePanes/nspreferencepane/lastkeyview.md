# lastKeyView

**Framework**: Preference Panes  
**Kind**: property

The last view in the keyboard focus chain.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
var lastKeyView: NSView? { get set }
```

#### Discussion

The last view can be set in the nib file by connecting a view to the receiver’s `_lastKeyView` outlet.

## See Also

- [var firstKeyView: NSView?](nspreferencepane/firstkeyview.md)
  The first view in the keyboard focus chain.
- [var initialKeyView: NSView?](nspreferencepane/initialkeyview.md)
  The view that should have keyboard focus when the pane is selected.
- [var autoSaveTextFields: Bool](nspreferencepane/autosavetextfields.md)
  A Boolean value that indicates whether text fields save their values before changing preference panes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/lastkeyview)*