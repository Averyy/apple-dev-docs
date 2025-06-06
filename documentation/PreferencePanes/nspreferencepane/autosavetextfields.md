# autoSaveTextFields

**Framework**: Preference Panes  
**Kind**: property

A Boolean value that indicates whether text fields save their values before changing preference panes.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.1+

## Declaration

```swift
var autoSaveTextFields: Bool { get }
```

#### Discussion

If this property is [`true`](https://developer.apple.com/documentation/swift/true), text fields are forced to give up their responder status before [`shouldUnselect`](nspreferencepane/shouldunselect.md) is called on the preference pane. If it is [`false`](https://developer.apple.com/documentation/swift/false), the preference pane is responsible for forcing text fields to give up their responder status before saving them. The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var firstKeyView: NSView?](nspreferencepane/firstkeyview.md)
  The first view in the keyboard focus chain.
- [var initialKeyView: NSView?](nspreferencepane/initialkeyview.md)
  The view that should have keyboard focus when the pane is selected.
- [var lastKeyView: NSView?](nspreferencepane/lastkeyview.md)
  The last view in the keyboard focus chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/preferencepanes/nspreferencepane/autosavetextfields)*