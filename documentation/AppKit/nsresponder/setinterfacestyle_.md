# setInterfaceStyle:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the receiver’s style to the style specified by `interfaceStyle`, such as `NSMacintoshInterfaceStyle` or `NSWindows95InterfaceStyle`.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```objc
- (void) setInterfaceStyle:(NSInterfaceStyle) interfaceStyle;
```

#### Discussion

[`setInterfaceStyle:`](./setinterfacestyle_.md) is an abstract method in `NSResponder`, but is overridden in classes such as [`NSWindow`](../nswindow.md) and [`NSView`](../nsview.md) to actually set the interface style. You should almost never need to invoke or override this method, but if you do override it, your version should always invoke the implementation in `super`.

## Parameters

- `interfaceStyle`: An `enum` constant identifying an interface style.

## See Also

### Deprecated methods
- [- performMnemonic:](./performmnemonic_.md)
  Handle a mnemonic.
- [- interfaceStyle](./interfacestyle.md)
  Returns the receiver’s interface style.
- [func beginGesture(with: NSEvent)](./begingesture%28with%29.md)
  Informs the receiver that the user has begun a touch gesture.
- [func endGesture(with: NSEvent)](./endgesture%28with%29.md)
  Informs the receiver that the user has ended a touch gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/setinterfacestyle:)*