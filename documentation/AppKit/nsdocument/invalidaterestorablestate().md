# invalidateRestorableState()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Marks the document’s interface-related state as dirty.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func invalidateRestorableState()
```

```objc
- (void) invalidateRestorableState;
```

#### Discussion

Call this method whenever the restorable state of your document changes. This method marks the document’s state as dirty, which causes that state to be written to disk at some point in the future. Do not override this method.

## See Also

### Handling Window Restoration
- [class func allowedClasses(forRestorableStateKeyPath: String) -> [AnyClass]](./allowedclasses%28forrestorablestatekeypath%29.md)
  Returns the classes that support secure coding.
- [func encodeRestorableState(with: NSCoder)](./encoderestorablestate%28with%29.md)
  Saves the interface-related state of the document.
- [func restoreState(with: NSCoder)](./restorestate%28with%29.md)
  Restores the interface-related state of the document.
- [class var restorableStateKeyPaths: [String]](./restorablestatekeypaths.md)
  Returns an array of key paths that represent the restorable attributes of the document.
- [func restoreWindow(withIdentifier: NSUserInterfaceItemIdentifier, state: NSCoder, completionHandler: (NSWindow?, (any Error)?) -> Void)](./restorewindow%28withidentifier,state,completionhandler%29.md)
  Restores a window that was associated with a document, after that document is reopened.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/invalidaterestorablestate())*