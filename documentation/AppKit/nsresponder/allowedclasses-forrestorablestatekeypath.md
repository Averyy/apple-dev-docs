# allowedClasses(forRestorableStateKeyPath:)

**Framework**: AppKit  
**Kind**: method

Returns the classes that support secure coding.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
class func allowedClasses(forRestorableStateKeyPath keyPath: String) -> [AnyClass]
```

#### Return Value

An array of classes that support secure coding.

#### Discussion

The system calls the function during a secure state restoration and restores values only for the allowed classes your app returns in the array.

## Parameters

- `keyPath`: The key path of the restorable object.

## See Also

- [func encodeRestorableState(with: NSCoder)](nsresponder/encoderestorablestate(with:).md)
  Saves the interface-related state of the responder.
- [func encodeRestorableState(with: NSCoder, backgroundQueue: OperationQueue)](nsresponder/encoderestorablestate(with:backgroundqueue:).md)
  Saves the interface-related state of the responder to a keyed archiver either synchronously or asynchronously on the given operation queue.
- [func restoreState(with: NSCoder)](nsresponder/restorestate(with:).md)
  Restores the interface-related state of the responder.
- [class var restorableStateKeyPaths: [String]](nsresponder/restorablestatekeypaths.md)
  Returns an array of key paths representing the restorable attributes of the responder.
- [func invalidateRestorableState()](nsresponder/invalidaterestorablestate.md)
  Marks the responder’s interface-related state as dirty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/allowedclasses(forrestorablestatekeypath:))*