# menuChangedMessagesEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Indicates whether messages are sent to the application’s windows each time the menu changes.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

## Declaration

```swift
var menuChangedMessagesEnabled: Bool { get set }
```

```objc
@property BOOL menuChangedMessagesEnabled;
```

## Discussion

This property indicates whether messages are sent to the application’s windows each time the menu changes.

To avoid the “flickering” effect of many successive menu changes, set the value of this property to [`false`](../../Swift/false.md), make changes to the menu, and then set the value of this property to [`true`](../../Swift/true.md). This approach has the effect of batching changes and applying them all at once.

### Special Considerations

In macOS 10.6 and later this property has no effect.

## See Also

### Deprecated properties
- [var isTornOff: Bool](./istornoff.md)
  Indicates whether the menu is offscreen or attached to another menu (or if it’s the main menu).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/menuchangedmessagesenabled)*