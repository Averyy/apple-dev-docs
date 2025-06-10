# restoreState(with:)

**Framework**: AppKit  
**Kind**: method

Restores the interface-related state of the responder.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func restoreState(with coder: NSCoder)
```

#### Discussion

This method is part of the window restoration system and is called at launch time to restore the visual state of your responder object. The default implementation does nothing but specific subclasses (such as [`NSView`](nsview.md) and [`NSWindow`](nswindow.md)) override it and save important state information. Therefore, if you override this method, you should always call `super` at some point in your implementation.

Subclasses can override this method and use it to restore any information that was saved in the [`encodeRestorableState(with:)`](nsresponder/encoderestorablestate(with:).md) method. You can also use this method to reconfigure the responder to its previous appearance.

> **Note**:  If the user’s computer is configured to close all windows when an app quits, the system automatically removes any preserved state as part of that process. As a result, the system doesn’t call `restoreState(with:)` the next time your app launches.

For information about using a coder object to read data from an archive, see [`Encoding and Decoding Custom Types`](https://developer.apple.com/documentation/Foundation/encoding-and-decoding-custom-types).

## Parameters

- `coder`: The coder object to use to restore the responder’s interface-related state.

## See Also

- [class func allowedClasses(forRestorableStateKeyPath: String) -> [AnyClass]](nsresponder/allowedclasses(forrestorablestatekeypath:).md)
  Returns the classes that support secure coding.
- [func encodeRestorableState(with: NSCoder)](nsresponder/encoderestorablestate(with:).md)
  Saves the interface-related state of the responder.
- [func encodeRestorableState(with: NSCoder, backgroundQueue: OperationQueue)](nsresponder/encoderestorablestate(with:backgroundqueue:).md)
  Saves the interface-related state of the responder to a keyed archiver either synchronously or asynchronously on the given operation queue.
- [class var restorableStateKeyPaths: [String]](nsresponder/restorablestatekeypaths.md)
  Returns an array of key paths representing the restorable attributes of the responder.
- [func invalidateRestorableState()](nsresponder/invalidaterestorablestate.md)
  Marks the responder’s interface-related state as dirty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/restorestate(with:))*