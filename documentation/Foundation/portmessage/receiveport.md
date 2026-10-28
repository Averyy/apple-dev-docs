# receivePort

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

For an outgoing message, returns the port on which replies to the receiver will arrive. For an incoming message, returns the port the receiver did arrive on.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var receivePort: Port? { get }
```

```objc
@property (retain, readonly, nullable) NSPort * receivePort;
```

## Return Value

For an outgoing message, the port on which replies to the receiver will arrive. For an incoming message, the port the receiver did arrive on.

## See Also

### Getting the Ports
- [var sendPort: Port?](./sendport.md)
  For an outgoing message, returns the port the receiver will send itself through. For an incoming message, returns the port replies to the receiver should be sent through.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/portmessage/receiveport)*