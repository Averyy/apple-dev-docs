# showHelp(_:)

**Framework**: AppKit  
**Kind**: method

If your project is properly registered, and the necessary keys have been set in the property list, this method launches Help Viewer and displays the first page of your app’s help book.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func showHelp(_ sender: Any?)
```

#### Discussion

For information on how to set up your project to take advantage of having Help Viewer display your help book, see [`Specifying the Comprehensive Help File`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OnlineHelp/Tasks/SpecifyHelpFile.html#//apple_ref/doc/uid/20000020).

## Parameters

- `sender`: The object that sent the command.

## See Also

- [func registerUserInterfaceItemSearchHandler(any NSUserInterfaceItemSearching)](nsapplication/registeruserinterfaceitemsearchhandler(_:).md)
  Register an object that provides help data to your app.
- [func searchString(String, inUserInterfaceItemString: String, range: NSRange, found: UnsafeMutablePointer<NSRange>?) -> Bool](nsapplication/searchstring(_:inuserinterfaceitemstring:range:found:).md)
  Searches for the string in the user interface.
- [func unregisterUserInterfaceItemSearchHandler(any NSUserInterfaceItemSearching)](nsapplication/unregisteruserinterfaceitemsearchhandler(_:).md)
  Unregister an object that provides help data to your app.
- [func activateContextHelpMode(Any?)](nsapplication/activatecontexthelpmode(_:).md)
  Places the receiver in context-sensitive help mode.
- [var helpMenu: NSMenu?](nsapplication/helpmenu.md)
  The help menu used by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/showhelp(_:))*