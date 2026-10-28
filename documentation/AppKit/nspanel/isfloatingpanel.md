# isFloatingPanel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver is a floating panel.

**Availability**:
- macOS

## Declaration

```swift
var isFloatingPanel: Bool { get set }
```

```objc
@property (getter=isFloatingPanel) BOOL floatingPanel;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the receiver is a floating panel, [`false`](../../Swift/false.md) otherwise.

By default, panels do not float above other windows. It’s appropriate for a panel to float above other windows only if all of the following conditions are true:

- It’s small enough not to obscure whatever is behind it.
- It’s oriented more to the mouse than to the keyboard—that is, if it doesn’t become the key window or becomes so only when needed.
- It needs to remain visible while the user works in the app’s standard windows—for example, if the user must frequently move the pointer back and forth between a standard window and the panel (such as a tool palette), or if the panel gives information relevant to the user’s actions in a standard window.
- It hides when the app is deactivated (the default behavior for panels).

## See Also

### Related Documentation
- [var level: NSWindow.Level](../nswindow/level-swift.property.md)
  The window level of the window.
- [Window Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Introduction.html#//apple_ref/doc/uid/10000031i)
### Configuring Panels
- [var becomesKeyOnlyIfNeeded: Bool](./becomeskeyonlyifneeded.md)
  A Boolean value that indicates whether the receiver becomes the key window only when needed.
- [var worksWhenModal: Bool](./workswhenmodal.md)
  A Boolean value that indicates whether the panel receives keyboard and mouse events even when some other window is being run modally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspanel/isfloatingpanel)*