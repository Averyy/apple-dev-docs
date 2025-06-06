# restorableStateKeyPaths

**Framework**: AppKit  
**Kind**: property

Returns an array of key paths representing the restorable attributes of the responder.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
class var restorableStateKeyPaths: [String] { get }
```

#### Return Value

An array of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects, each of which contains a key path to one of the responder’s attributes.

#### Discussion

You can use this method instead of, or in addition to, the [`encodeRestorableState(with:)`](nsresponder/encoderestorablestate(with:).md) and [`restoreState(with:)`](nsresponder/restorestate(with:).md) methods to save and restore the state of your responder. The key paths you return must refer to attributes that are key-value coding and key-value observing compliant. To learn more about these mechanisms, see [`Key-Value Coding Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i) and [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

When changes are detected, the specified attributes are automatically written to disk with the rest of the application’s interface-related state. At launch time, the attributes are automatically restored to their previous values.

## See Also

- [class func allowedClasses(forRestorableStateKeyPath: String) -> [AnyClass]](nsresponder/allowedclasses(forrestorablestatekeypath:).md)
  Returns the classes that support secure coding.
- [func encodeRestorableState(with: NSCoder)](nsresponder/encoderestorablestate(with:).md)
  Saves the interface-related state of the responder.
- [func encodeRestorableState(with: NSCoder, backgroundQueue: OperationQueue)](nsresponder/encoderestorablestate(with:backgroundqueue:).md)
  Saves the interface-related state of the responder to a keyed archiver either synchronously or asynchronously on the given operation queue.
- [func restoreState(with: NSCoder)](nsresponder/restorestate(with:).md)
  Restores the interface-related state of the responder.
- [func invalidateRestorableState()](nsresponder/invalidaterestorablestate.md)
  Marks the responder’s interface-related state as dirty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/restorablestatekeypaths)*