# connectionWithReceivePort:sendPort:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns an `NSConnection` object that communicates using given send and receive ports.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
+ (instancetype) connectionWithReceivePort:(NSPort *) receivePort sendPort:(NSPort *) sendPort;
```

#### Return Value

An `NSConnection` object that communicates using `receivePort` and `sendPort`.

#### Discussion

See [`initWithReceivePort:sendPort:`](./initwithreceiveport_sendport_.md) for more information.

## Parameters

- `receivePort`: A receive port.
- `sendPort`: A send port.

## See Also

### Related Documentation
- [+ defaultConnection](./defaultconnection.md)
  Returns the default `NSConnection` object for the current thread.
### Creating Instances
- [- initWithReceivePort:sendPort:](./initwithreceiveport_sendport_.md)
  Returns an `NSConnection` object initialized with given send and receive ports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/connectionwithreceiveport:sendport:)*