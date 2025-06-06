# restorableStateKeyPaths

**Framework**: AppKit  
**Kind**: property

Returns an array of key paths that represent the restorable attributes of the document.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
class var restorableStateKeyPaths: [String] { get }
```

#### Return Value

An array of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects, each of which contains a key path to one of the document’s attributes.

#### Discussion

You can use this method instead of, or in addition to, the [`encodeRestorableState(with:)`](nsdocument/encoderestorablestate(with:).md) and [`restoreState(with:)`](nsdocument/restorestate(with:).md) methods to save and restore the state of your document. The key paths must refer to attributes that are [`Key-value coding`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25) and [`Key-value observing`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16) compliant.

When changes are detected, the specified attributes are automatically written to disk with the rest of the app’s interface-related state. At launch time, the attributes are automatically restored to their previous values.

## See Also

- [class func allowedClasses(forRestorableStateKeyPath: String) -> [AnyClass]](nsdocument/allowedclasses(forrestorablestatekeypath:).md)
  Returns the classes that support secure coding.
- [func encodeRestorableState(with: NSCoder)](nsdocument/encoderestorablestate(with:).md)
  Saves the interface-related state of the document.
- [func restoreState(with: NSCoder)](nsdocument/restorestate(with:).md)
  Restores the interface-related state of the document.
- [func invalidateRestorableState()](nsdocument/invalidaterestorablestate.md)
  Marks the document’s interface-related state as dirty.
- [func restoreWindow(withIdentifier: NSUserInterfaceItemIdentifier, state: NSCoder, completionHandler: (NSWindow?, (any Error)?) -> Void)](nsdocument/restorewindow(withidentifier:state:completionhandler:).md)
  Restores a window that was associated with a document, after that document is reopened.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/restorablestatekeypaths)*