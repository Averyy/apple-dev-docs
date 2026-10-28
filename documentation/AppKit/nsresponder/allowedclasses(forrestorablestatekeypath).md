# allowedClasses(forRestorableStateKeyPath:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the classes that support secure coding.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class func allowedClasses(forRestorableStateKeyPath keyPath: String) -> [AnyClass]
```

```objc
+ (NSArray<Class> *) allowedClassesForRestorableStateKeyPath:(NSString *) keyPath;
```

## Return Value

An array of classes that support secure coding.

## Discussion

The system calls the function during a secure state restoration and restores values only for the allowed classes your app returns in the array.

## Parameters

- `keyPath`: The key path of the restorable object.

## See Also

### Handling Window Restoration
- [func encodeRestorableState(with: NSCoder)](./encoderestorablestate%28with%29.md)
  Saves the interface-related state of the responder.
- [func encodeRestorableState(with: NSCoder, backgroundQueue: OperationQueue)](./encoderestorablestate%28with,backgroundqueue%29.md)
  Saves the interface-related state of the responder to a keyed archiver either synchronously or asynchronously on the given operation queue.
- [func restoreState(with: NSCoder)](./restorestate%28with%29.md)
  Restores the interface-related state of the responder.
- [class var restorableStateKeyPaths: [String]](./restorablestatekeypaths.md)
  Returns an array of key paths representing the restorable attributes of the responder.
- [func invalidateRestorableState()](./invalidaterestorablestate%28%29.md)
  Marks the responder’s interface-related state as dirty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/allowedclasses(forrestorablestatekeypath:))*