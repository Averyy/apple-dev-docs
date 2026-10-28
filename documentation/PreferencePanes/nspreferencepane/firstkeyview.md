# firstKeyView

**Framework**: Preference Panes  
**Kind**: property  
**Role**: Instance Property

The first view in the keyboard focus chain.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
var firstKeyView: NSView? { get set }
```

```objc
@property (strong, nullable) NSView * firstKeyView;
```

## Discussion

The first key view can be set in the nib file by connecting a view to the receiver’s `_firstKeyView` outlet.

## See Also

### Handling keyboard focus
- [var initialKeyView: NSView?](./initialkeyview.md)
  The view that should have keyboard focus when the pane is selected.
- [var lastKeyView: NSView?](./lastkeyview.md)
  The last view in the keyboard focus chain.
- [var autoSaveTextFields: Bool](./autosavetextfields.md)
  A Boolean value that indicates whether text fields save their values before changing preference panes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/firstkeyview)*