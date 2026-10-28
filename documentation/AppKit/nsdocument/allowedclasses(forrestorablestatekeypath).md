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
  Saves the interface-related state of the document.
- [func restoreState(with: NSCoder)](./restorestate%28with%29.md)
  Restores the interface-related state of the document.
- [class var restorableStateKeyPaths: [String]](./restorablestatekeypaths.md)
  Returns an array of key paths that represent the restorable attributes of the document.
- [func invalidateRestorableState()](./invalidaterestorablestate%28%29.md)
  Marks the document’s interface-related state as dirty.
- [func restoreWindow(withIdentifier: NSUserInterfaceItemIdentifier, state: NSCoder, completionHandler: (NSWindow?, (any Error)?) -> Void)](./restorewindow%28withidentifier,state,completionhandler%29.md)
  Restores a window that was associated with a document, after that document is reopened.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/allowedclasses(forrestorablestatekeypath:))*