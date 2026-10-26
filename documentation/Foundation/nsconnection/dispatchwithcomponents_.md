# dispatchWithComponents:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Allows subclasses to ask a connection object to dispatch component data.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+ - Deprecated in 10.13

## Declaration

```objc
- (void) dispatchWithComponents:(NSArray *) components;
```

#### Discussion

[`Port`](../port.md) subclasses should use this method to ask a connection object to dispatch Distributed Objects component data received over the wire. This will decode the data, authenticate, and send the message.

## Parameters

- `components`: Distributed Objects component data.

## See Also

### Getting Ports
- [receivePort](./receiveport-c.property.md)
  The port on which the receiver receives incoming network messages.
- [sendPort](./sendport-c.property.md)
  The port that the connection sends outgoing network messages through.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/dispatchwithcomponents:)*