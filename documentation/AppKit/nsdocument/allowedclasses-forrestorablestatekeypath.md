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

- [func encodeRestorableState(with: NSCoder)](nsdocument/encoderestorablestate(with:).md)
  Saves the interface-related state of the document.
- [func restoreState(with: NSCoder)](nsdocument/restorestate(with:).md)
  Restores the interface-related state of the document.
- [class var restorableStateKeyPaths: [String]](nsdocument/restorablestatekeypaths.md)
  Returns an array of key paths that represent the restorable attributes of the document.
- [func invalidateRestorableState()](nsdocument/invalidaterestorablestate.md)
  Marks the document’s interface-related state as dirty.
- [func restoreWindow(withIdentifier: NSUserInterfaceItemIdentifier, state: NSCoder, completionHandler: (NSWindow?, (any Error)?) -> Void)](nsdocument/restorewindow(withidentifier:state:completionhandler:).md)
  Restores a window that was associated with a document, after that document is reopened.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/allowedclasses(forrestorablestatekeypath:))*