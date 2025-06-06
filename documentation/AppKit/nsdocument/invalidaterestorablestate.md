# invalidateRestorableState()

**Framework**: AppKit  
**Kind**: method

Marks the document’s interface-related state as dirty.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func invalidateRestorableState()
```

#### Discussion

Call this method whenever the restorable state of your document changes. This method marks the document’s state as dirty, which causes that state to be written to disk at some point in the future. Do not override this method.

## See Also

- [class func allowedClasses(forRestorableStateKeyPath: String) -> [AnyClass]](nsdocument/allowedclasses(forrestorablestatekeypath:).md)
  Returns the classes that support secure coding.
- [func encodeRestorableState(with: NSCoder)](nsdocument/encoderestorablestate(with:).md)
  Saves the interface-related state of the document.
- [func restoreState(with: NSCoder)](nsdocument/restorestate(with:).md)
  Restores the interface-related state of the document.
- [class var restorableStateKeyPaths: [String]](nsdocument/restorablestatekeypaths.md)
  Returns an array of key paths that represent the restorable attributes of the document.
- [func restoreWindow(withIdentifier: NSUserInterfaceItemIdentifier, state: NSCoder, completionHandler: (NSWindow?, (any Error)?) -> Void)](nsdocument/restorewindow(withidentifier:state:completionhandler:).md)
  Restores a window that was associated with a document, after that document is reopened.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/invalidaterestorablestate())*