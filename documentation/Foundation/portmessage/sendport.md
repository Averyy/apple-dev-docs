# sendPort

**Framework**: Foundation  
**Kind**: property

For an outgoing message, returns the port the receiver will send itself through. For an incoming message, returns the port replies to the receiver should be sent through.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var sendPort: Port? { get }
```

#### Return Value

For an outgoing message, the port the receiver will send itself through when it receives a [`send(before:)`](portmessage/send(before:).md) message. For an incoming message, the port replies to the receiver should be sent through.

## See Also

- [var receivePort: Port?](portmessage/receiveport.md)
  For an outgoing message, returns the port on which replies to the receiver will arrive. For an incoming message, returns the port the receiver did arrive on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/portmessage/sendport)*