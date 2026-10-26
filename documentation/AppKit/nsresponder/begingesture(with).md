# beginGesture(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the receiver that the user has begun a touch gesture.

**Availability**:
- macOS 10.5+ - Deprecated in 27.0

> **Deprecated**: Begin/end gesture events are no longer delivered. Use the phase property on NSEvent or NSGestureRecognizer instead.

## Declaration

```swift
func beginGesture(with event: NSEvent)
```

```objc
- (void) beginGestureWithEvent:(NSEvent *) event;
```

#### Discussion

The event will be sent to the view under the touch in the key window.

Note that this method is no longer called on apps that link against macOS 10.11 and later. If you need to access the phases of a specific gesture, you can implement the responder for that gesture and examine its [`phase`](../nsevent/phase-swift.property.md) property instead.

## Parameters

- `event`: An event object representing the gesture beginning.

## See Also

### Deprecated methods
- [func endGesture(with: NSEvent)](./endgesture%28with%29.md)
  Informs the receiver that the user has ended a touch gesture.
- [- performMnemonic:](./performmnemonic_.md)
  Handle a mnemonic.
- [- setInterfaceStyle:](./setinterfacestyle_.md)
  Sets the receiver’s style to the style specified by `interfaceStyle`, such as `NSMacintoshInterfaceStyle` or `NSWindows95InterfaceStyle`.
- [- interfaceStyle](./interfacestyle.md)
  Returns the receiver’s interface style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/begingesture(with:))*