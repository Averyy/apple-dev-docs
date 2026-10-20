# encodeRestorableState(with:backgroundQueue:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Saves the interface-related state of the responder to a keyed archiver either synchronously or asynchronously on the given operation queue.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func encodeRestorableState(with coder: NSCoder, backgroundQueue queue: OperationQueue)
```

```objc
- (void) encodeRestorableStateWithCoder:(NSCoder *) coder backgroundQueue:(NSOperationQueue *) queue;
```

#### Discussion

Don’t call this method directly. The system calls this method on the main thread. The receiver may synchronously encode state to `coder` or may enqueue asynchronous work to encode additional restorable state using the provided serial background [`OperationQueue`](../../Foundation/operationqueue.md), if it can safely access and encode that information. The encoding process finishes when the enqueued operations complete.

If you override this method, call the super implementation.

## Parameters

- `coder`: A thread-safe keyed archiver to write restorable state into.
- `queue`: A serial background operation queue to perform asynchronous encoding work on.

## See Also

### Handling Window Restoration
- [class func allowedClasses(forRestorableStateKeyPath: String) -> [AnyClass]](./allowedclasses%28forrestorablestatekeypath%29.md)
  Returns the classes that support secure coding.
- [func encodeRestorableState(with: NSCoder)](./encoderestorablestate%28with%29.md)
  Saves the interface-related state of the responder.
- [func restoreState(with: NSCoder)](./restorestate%28with%29.md)
  Restores the interface-related state of the responder.
- [class var restorableStateKeyPaths: [String]](./restorablestatekeypaths.md)
  Returns an array of key paths representing the restorable attributes of the responder.
- [func invalidateRestorableState()](./invalidaterestorablestate%28%29.md)
  Marks the responder’s interface-related state as dirty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/encoderestorablestate(with:backgroundqueue:))*