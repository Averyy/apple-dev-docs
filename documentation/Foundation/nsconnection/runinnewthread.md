# runInNewThread

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates and starts a new `NSThread` object and then runs the receiving connection in the new thread.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (void) runInNewThread;
```

#### Discussion

If the newly created thread is the first to be detached from the current thread, this method posts an [`NSWillBecomeMultiThreaded`](../nsnotification/name-swift.struct/nswillbecomemultithreaded.md) with `nil` to the default notification center.

## See Also

### Running the Connection in a New Thread
- [- enableMultipleThreads](./enablemultiplethreads.md)
  Configures the receiver to allow requests from multiple threads to the remote object, without requiring each thread to each maintain its own connection.
- [multipleThreadsEnabled](./multiplethreadsenabled.md)
  A Boolean value that indicates whether the receiver supports requests from multiple threads.
- [- addRunLoop:](./addrunloop_.md)
  Adds the specified run loop to the list of run loops the receiver monitors and from which it responds to requests.
- [- removeRunLoop:](./removerunloop_.md)
  Removes a given `NSRunLoop` object from the list of run loops the receiver monitors and from which it responds to requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/runinnewthread)*