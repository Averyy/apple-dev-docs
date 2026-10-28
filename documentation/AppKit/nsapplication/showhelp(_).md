# showHelp(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

If your project is properly registered, and the necessary keys have been set in the property list, this method launches Help Viewer and displays the first page of your app’s help book.

**Availability**:
- macOS

## Declaration

```swift
func showHelp(_ sender: Any?)
```

```objc
- (void) showHelp:(id) sender;
```

## Discussion

For information on how to set up your project to take advantage of having Help Viewer display your help book, see [Specifying the Comprehensive Help File](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OnlineHelp/Tasks/SpecifyHelpFile.html#//apple_ref/doc/uid/20000020).

## Parameters

- `sender`: The object that sent the command.

## See Also

### Providing help information
- [func registerUserInterfaceItemSearchHandler(any NSUserInterfaceItemSearching)](./registeruserinterfaceitemsearchhandler%28_%29.md)
  Register an object that provides help data to your app.
- [func searchString(String, inUserInterfaceItemString: String, range: NSRange, found: UnsafeMutablePointer<NSRange>?) -> Bool](./searchstring%28_,inuserinterfaceitemstring,range,found%29.md)
  Searches for the string in the user interface.
- [func unregisterUserInterfaceItemSearchHandler(any NSUserInterfaceItemSearching)](./unregisteruserinterfaceitemsearchhandler%28_%29.md)
  Unregister an object that provides help data to your app.
- [func activateContextHelpMode(Any?)](./activatecontexthelpmode%28_%29.md)
  Places the receiver in context-sensitive help mode.
- [var helpMenu: NSMenu?](./helpmenu.md)
  The help menu used by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/showhelp(_:))*