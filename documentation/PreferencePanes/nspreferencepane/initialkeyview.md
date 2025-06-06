# initialKeyView

**Framework**: Preference Panes  
**Kind**: property

The view that should have keyboard focus when the pane is selected.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
var initialKeyView: NSView? { get set }
```

#### Discussion

The initial view can be set in the nib file by connecting a view to the receiver’s `_initialKeyView` outlet.

## See Also

- [var firstKeyView: NSView?](nspreferencepane/firstkeyview.md)
  The first view in the keyboard focus chain.
- [var lastKeyView: NSView?](nspreferencepane/lastkeyview.md)
  The last view in the keyboard focus chain.
- [var autoSaveTextFields: Bool](nspreferencepane/autosavetextfields.md)
  A Boolean value that indicates whether text fields save their values before changing preference panes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/initialkeyview)*