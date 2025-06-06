# firstKeyView

**Framework**: Preference Panes  
**Kind**: property

The first view in the keyboard focus chain.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
var firstKeyView: NSView? { get set }
```

#### Discussion

The first key view can be set in the nib file by connecting a view to the receiver’s `_firstKeyView` outlet.

## See Also

- [var initialKeyView: NSView?](nspreferencepane/initialkeyview.md)
  The view that should have keyboard focus when the pane is selected.
- [var lastKeyView: NSView?](nspreferencepane/lastkeyview.md)
  The last view in the keyboard focus chain.
- [var autoSaveTextFields: Bool](nspreferencepane/autosavetextfields.md)
  A Boolean value that indicates whether text fields save their values before changing preference panes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/firstkeyview)*