# interfaceStyle

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the receiver’s interface style.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```objc
- (NSInterfaceStyle) interfaceStyle;
```

## Discussion

[`interfaceStyle`](./interfacestyle.md) is an abstract method in `NSResponder` and just returns `NSNoInterfaceStyle`. It’s overridden in classes such as [`NSWindow`](../nswindow.md) and [`NSView`](../nsview.md) to return the interface style, such as `NSMacintoshInterfaceStyle`. A responder’s style (if other than `NSNoInterfaceStyle`) overrides all other settings, such as those established by the defaults system.

## See Also

### Deprecated methods
- [- performMnemonic:](./performmnemonic_.md)
  Handle a mnemonic.
- [- setInterfaceStyle:](./setinterfacestyle_.md)
  Sets the receiver’s style to the style specified by `interfaceStyle`, such as `NSMacintoshInterfaceStyle` or `NSWindows95InterfaceStyle`.
- [func beginGesture(with: NSEvent)](./begingesture%28with%29.md)
  Informs the receiver that the user has begun a touch gesture.
- [func endGesture(with: NSEvent)](./endgesture%28with%29.md)
  Informs the receiver that the user has ended a touch gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/interfacestyle)*