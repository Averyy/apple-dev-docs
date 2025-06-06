# unregisterUserInterfaceItemSearchHandler(_:)

**Framework**: AppKit  
**Kind**: method

Unregister an object that provides help data to your app.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func unregisterUserInterfaceItemSearchHandler(_ handler: any NSUserInterfaceItemSearching)
```

#### Discussion

If you unregister the same instance more than once the subsequent invocations are ignored. Unregistering an instance that was never registered is ignored.

## Parameters

- `handler`: The class instance that conforms to   and provides help content.

## See Also

- [func registerUserInterfaceItemSearchHandler(any NSUserInterfaceItemSearching)](nsapplication/registeruserinterfaceitemsearchhandler(_:).md)
  Register an object that provides help data to your app.
- [func searchString(String, inUserInterfaceItemString: String, range: NSRange, found: UnsafeMutablePointer<NSRange>?) -> Bool](nsapplication/searchstring(_:inuserinterfaceitemstring:range:found:).md)
  Searches for the string in the user interface.
- [func showHelp(Any?)](nsapplication/showhelp(_:).md)
  If your project is properly registered, and the necessary keys have been set in the property list, this method launches Help Viewer and displays the first page of your app’s help book.
- [func activateContextHelpMode(Any?)](nsapplication/activatecontexthelpmode(_:).md)
  Places the receiver in context-sensitive help mode.
- [var helpMenu: NSMenu?](nsapplication/helpmenu.md)
  The help menu used by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/unregisteruserinterfaceitemsearchhandler(_:))*