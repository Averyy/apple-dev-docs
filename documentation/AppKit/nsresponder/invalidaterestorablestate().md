# invalidateRestorableState()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Marks the responder’s interface-related state as dirty.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func invalidateRestorableState()
```

```objc
- (void) invalidateRestorableState;
```

## Discussion

Call this method whenever the restorable state of your responder changes. This method marks the responder’s state as dirty, which writes the state to disk at some point in the future. Don’t override this method.

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
- [class var restorableStateKeyPaths: [String]](./restorablestatekeypaths.md)
  Returns an array of key paths representing the restorable attributes of the responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/invalidaterestorablestate())*