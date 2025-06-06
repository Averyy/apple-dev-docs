# restoreWindow(withIdentifier:state:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Restores a window that was associated with a document, after that document is reopened.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func restoreWindow(withIdentifier identifier: NSUserInterfaceItemIdentifier, state: NSCoder) async throws -> NSWindow
```

#### Discussion

This method is called by the default `NSDocumentController` implementation of [`restoreWindow(withIdentifier:state:completionHandler:)`](nswindowrestoration/restorewindow(withidentifier:state:completionhandler:).md).

The default implementation of this method first checks if the document has window controllers, and if not, it calls [`makeWindowControllers()`](nsdocument/makewindowcontrollers().md). If there is then exactly one window controller, it invokes the completion handler with its window. If there is more than one, it searches the receiver’s window controllers for a window that matches the given identifier, and then calls the completion handler with it. If no window could be found, it invokes the completion handler with a `nil` window.

If your document has variable or optional windows, you may override this to create the requested window, and then call the completion handler with it. This allows you to use the default document reopening behavior, but intervene at the point of creating the windows. The parameters are the same as in the class method [`restoreWindow(withIdentifier:state:completionHandler:)`](nswindowrestoration/restorewindow(withidentifier:state:completionhandler:).md).

## Parameters

- `identifier`: The unique interface item identifier string that was previously associated with the window. Use this string to determine which window to create.
- `state`: A coder object containing the window state information. This coder object contains the combined restorable state of the window, which can include the state of the window, its delegate, window controller, and document object. You can use this state to determine which window to create.
- `completionHandler`: A block object to execute with the results of creating the window. You must execute this block at some point but may do so after the method returns if needed. This block takes the following parameters:

## See Also

- [static func restoreWindow(withIdentifier: NSUserInterfaceItemIdentifier, state: NSCoder, completionHandler: (NSWindow?, (any Error)?) -> Void)](nswindowrestoration/restorewindow(withidentifier:state:completionhandler:).md)
  Asks the class to provide a new window for the specified identifier.
- [class func allowedClasses(forRestorableStateKeyPath: String) -> [AnyClass]](nsdocument/allowedclasses(forrestorablestatekeypath:).md)
  Returns the classes that support secure coding.
- [func encodeRestorableState(with: NSCoder)](nsdocument/encoderestorablestate(with:).md)
  Saves the interface-related state of the document.
- [func restoreState(with: NSCoder)](nsdocument/restorestate(with:).md)
  Restores the interface-related state of the document.
- [class var restorableStateKeyPaths: [String]](nsdocument/restorablestatekeypaths.md)
  Returns an array of key paths that represent the restorable attributes of the document.
- [func invalidateRestorableState()](nsdocument/invalidaterestorablestate.md)
  Marks the document’s interface-related state as dirty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/restorewindow(withidentifier:state:completionhandler:))*