# autoSaveTextFields

**Framework**: Preference Panes  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether text fields save their values before changing preference panes.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
var autoSaveTextFields: Bool { get }
```

```objc
@property (readonly) BOOL autoSaveTextFields;
```

#### Discussion

If this property is [`true`](../../Swift/true.md), text fields are forced to give up their responder status before [`shouldUnselect`](./shouldunselect.md) is called on the preference pane. If it is [`false`](../../Swift/false.md), the preference pane is responsible for forcing text fields to give up their responder status before saving them. The default value is [`true`](../../Swift/true.md).

## See Also

### Handling keyboard focus
- [var firstKeyView: NSView?](./firstkeyview.md)
  The first view in the keyboard focus chain.
- [var initialKeyView: NSView?](./initialkeyview.md)
  The view that should have keyboard focus when the pane is selected.
- [var lastKeyView: NSView?](./lastkeyview.md)
  The last view in the keyboard focus chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/autosavetextfields)*