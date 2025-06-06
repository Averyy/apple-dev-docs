# encodeRestorableState(with:backgroundQueue:)

**Framework**: AppKit  
**Kind**: method

Saves the interface-related state of the responder to a keyed archiver either synchronously or asynchronously on the given operation queue.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@MainActor
func encodeRestorableState(with coder: NSCoder, backgroundQueue queue: OperationQueue)
```

#### Discussion

Don’t call this method directly. The system calls this method on the main thread. The receiver may synchronously encode state to `coder` or may enqueue asynchronous work to encode additional restorable state using the provided serial background [`OperationQueue`](https://developer.apple.com/documentation/Foundation/OperationQueue), if it can safely access and encode that information. The encoding process finishes when the enqueued operations complete.

If you override this method, call the super implementation.

## Parameters

- `coder`: A thread-safe keyed archiver to write restorable state into.
- `queue`: A serial background operation queue to perform asynchronous encoding work on.

## See Also

- [class func allowedClasses(forRestorableStateKeyPath: String) -> [AnyClass]](nsresponder/allowedclasses(forrestorablestatekeypath:).md)
  Returns the classes that support secure coding.
- [func encodeRestorableState(with: NSCoder)](nsresponder/encoderestorablestate(with:).md)
  Saves the interface-related state of the responder.
- [func restoreState(with: NSCoder)](nsresponder/restorestate(with:).md)
  Restores the interface-related state of the responder.
- [class var restorableStateKeyPaths: [String]](nsresponder/restorablestatekeypaths.md)
  Returns an array of key paths representing the restorable attributes of the responder.
- [func invalidateRestorableState()](nsresponder/invalidaterestorablestate.md)
  Marks the responder’s interface-related state as dirty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/encoderestorablestate(with:backgroundqueue:))*