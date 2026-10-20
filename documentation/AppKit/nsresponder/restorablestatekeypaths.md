# restorableStateKeyPaths

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns an array of key paths representing the restorable attributes of the responder.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class var restorableStateKeyPaths: [String] { get }
```

```objc
@property (class, copy, readonly) NSArray<NSString *> * restorableStateKeyPaths;
```

#### Return Value

An array of [`NSString`](../../Foundation/nsstring.md) objects, each of which contains a key path to one of the responder’s attributes.

#### Discussion

You can use this method instead of, or in addition to, the [`encodeRestorableState(with:)`](./encoderestorablestate%28with%29.md) and [`restoreState(with:)`](./restorestate%28with%29.md) methods to save and restore the state of your responder. The key paths you return must refer to attributes that are key-value coding and key-value observing compliant. To learn more about these mechanisms, see [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i) and [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

When changes are detected, the specified attributes are automatically written to disk with the rest of the application’s interface-related state. At launch time, the attributes are automatically restored to their previous values.

## See Also

### Handling Window Restoration
- [class func allowedClasses(forRestorableStateKeyPath: String) -> [AnyClass]](./allowedclasses%28forrestorablestatekeypath%29.md)
  Returns the classes that support secure coding.
- [func encodeRestorableState(with: NSCoder)](./encoderestorablestate%28with%29.md)
  Saves the interface-related state of the responder.
- [func encodeRestorableState(with: NSCoder, backgroundQueue: OperationQueue)](./encoderestorablestate%28with,backgroundqueue%29.md)
  Saves the interface-related state of the responder to a keyed archiver either synchronously or asynchronously on the given operation queue.
- [func restoreState(with: NSCoder)](./restorestate%28with%29.md)
  Restores the interface-related state of the responder.
- [func invalidateRestorableState()](./invalidaterestorablestate%28%29.md)
  Marks the responder’s interface-related state as dirty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/restorablestatekeypaths)*