# addRunLoop:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds the specified run loop to the list of run loops the receiver monitors and from which it responds to requests.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (void) addRunLoop:(NSRunLoop *) runloop;
```

#### Discussion

This method is invoked automatically when a request comes in from a new run loop if [`enableMultipleThreads`](./enablemultiplethreads.md) has been set.

## Parameters

- `runloop`: The run loop to add to the receiver.

## See Also

### Running the Connection in a New Thread
- [- runInNewThread](./runinnewthread.md)
  Creates and starts a new `NSThread` object and then runs the receiving connection in the new thread.
- [- enableMultipleThreads](./enablemultiplethreads.md)
  Configures the receiver to allow requests from multiple threads to the remote object, without requiring each thread to each maintain its own connection.
- [multipleThreadsEnabled](./multiplethreadsenabled.md)
  A Boolean value that indicates whether the receiver supports requests from multiple threads.
- [- removeRunLoop:](./removerunloop_.md)
  Removes a given `NSRunLoop` object from the list of run loops the receiver monitors and from which it responds to requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/addrunloop:)*