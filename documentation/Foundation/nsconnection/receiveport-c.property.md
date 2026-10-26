# receivePort

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The port on which the receiver receives incoming network messages.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
@property (retain, readonly) NSPort * receivePort;
```

#### Discussion

You can inspect this object for debugging purposes or use it to create another `NSConnection` object, but shouldn’t use it to send or receive messages explicitly. Don’t set the delegate of the receive port; it already has a delegate established by the `NSConnection` object.

## See Also

### Related Documentation
- [- initWithReceivePort:sendPort:](./initwithreceiveport_sendport_.md)
  Returns an `NSConnection` object initialized with given send and receive ports.
### Getting Ports
- [sendPort](./sendport-c.property.md)
  The port that the connection sends outgoing network messages through.
- [- dispatchWithComponents:](./dispatchwithcomponents_.md)
  Allows subclasses to ask a connection object to dispatch component data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/receiveport-c.property)*