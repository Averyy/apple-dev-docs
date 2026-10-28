# performMnemonic:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Handle a mnemonic.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```objc
- (BOOL) performMnemonic:(NSString *) string;
```

## Discussion

Orverride to respond to mnemonics. If the character code or codes in s`tring` match the receiver’s mnemonic, the receiver should perform the mnemonic and return [`true`](../../Swift/true.md). The default implementation does nothing and returns [`false`](../../Swift/false.md). Mnemonics are not supported in macOS.

## Parameters

- `string`: A string containing mnemonic character code or codes.

## See Also

### Related Documentation
- [- performMnemonic:](../nsview/performmnemonic_.md)
  Implemented by subclasses to respond to mnemonics.
### Deprecated methods
- [- setInterfaceStyle:](./setinterfacestyle_.md)
  Sets the receiver’s style to the style specified by `interfaceStyle`, such as `NSMacintoshInterfaceStyle` or `NSWindows95InterfaceStyle`.
- [- interfaceStyle](./interfacestyle.md)
  Returns the receiver’s interface style.
- [func beginGesture(with: NSEvent)](./begingesture%28with%29.md)
  Informs the receiver that the user has begun a touch gesture.
- [func endGesture(with: NSEvent)](./endgesture%28with%29.md)
  Informs the receiver that the user has ended a touch gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/performmnemonic:)*