# isTornOff

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Indicates whether the menu is offscreen or attached to another menu (or if it’s the main menu).

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

## Declaration

```swift
var isTornOff: Bool { get }
```

```objc
@property (readonly, getter=isTornOff) BOOL tornOff;
```

#### Discussion

This property has a value of [`false`](../../Swift/false.md) if the menu is offscreen, is attached to another menu, or is the main menu. Otherwise, this property has a value of [`true`](../../Swift/true.md).

##### Special Considerations

This property has no effect in macOS 10.6 and later.

## See Also

### Deprecated properties
- [var menuChangedMessagesEnabled: Bool](./menuchangedmessagesenabled.md)
  Indicates whether messages are sent to the application’s windows each time the menu changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/istornoff)*