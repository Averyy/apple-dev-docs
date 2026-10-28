# restorableStateKeyPaths

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns an array of key paths that represent the restorable attributes of the document.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class var restorableStateKeyPaths: [String] { get }
```

```objc
@property (class, copy, readonly) NSArray<NSString *> * restorableStateKeyPaths;
```

## Return Value

An array of [`NSString`](../../Foundation/nsstring.md) objects, each of which contains a key path to one of the document’s attributes.

## Discussion

You can use this method instead of, or in addition to, the [`encodeRestorableState(with:)`](./encoderestorablestate%28with%29.md) and [`restoreState(with:)`](./restorestate%28with%29.md) methods to save and restore the state of your document. The key paths must refer to attributes that are [Key-value coding](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25) and [Key-value observing](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16) compliant.

When changes are detected, the specified attributes are automatically written to disk with the rest of the app’s interface-related state. At launch time, the attributes are automatically restored to their previous values.

## See Also

### Handling Window Restoration
- [class func allowedClasses(forRestorableStateKeyPath: String) -> [AnyClass]](./allowedclasses%28forrestorablestatekeypath%29.md)
  Returns the classes that support secure coding.
- [func encodeRestorableState(with: NSCoder)](./encoderestorablestate%28with%29.md)
  Saves the interface-related state of the document.
- [func restoreState(with: NSCoder)](./restorestate%28with%29.md)
  Restores the interface-related state of the document.
- [func invalidateRestorableState()](./invalidaterestorablestate%28%29.md)
  Marks the document’s interface-related state as dirty.
- [func restoreWindow(withIdentifier: NSUserInterfaceItemIdentifier, state: NSCoder, completionHandler: (NSWindow?, (any Error)?) -> Void)](./restorewindow%28withidentifier,state,completionhandler%29.md)
  Restores a window that was associated with a document, after that document is reopened.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/restorablestatekeypaths)*