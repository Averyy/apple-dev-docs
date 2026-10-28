# removeConnection:fromRunLoop:forMode:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes the receiver from the list of ports monitored by `runLoop` in the given input mode, `mode`.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use [`NSXPCConnection`](../nsxpcconnection.md) instead.

## Declaration

```objc
- (void) removeConnection:(NSConnection *) conn fromRunLoop:(NSRunLoop *) runLoop forMode:(NSRunLoopMode) mode;
```

## Discussion

You should not call this method directly. The method is provided for subclassers who wish to provide their own custom types of `NSPort`. The `NSConnection` object, `conn`, calls this method at the appropriate times.

## Parameters

- `conn`: The connection object that invoked this method.
- `runLoop`: The run loop to which to add the receiver.
- `mode`: The run loop mode in which to add the receiver.

## See Also

### Creating connections
- [- addConnection:toRunLoop:forMode:](./addconnection_torunloop_formode_.md)
  Adds the receiver to the list of ports monitored by a given run loop for the given input mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsport/removeconnection:fromrunloop:formode:)*