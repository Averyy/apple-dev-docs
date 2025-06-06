# registerUserInterfaceItemSearchHandler(_:)

**Framework**: AppKit  
**Kind**: method

Register an object that provides help data to your app.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func registerUserInterfaceItemSearchHandler(_ handler: any NSUserInterfaceItemSearching)
```

#### Discussion

You can register as many search handlers as you like. If you register the same instance more than once the subsequent registrations are ignored.

## Parameters

- `handler`: The class instance that conforms to   and provides help content.

## See Also

- [func searchString(String, inUserInterfaceItemString: String, range: NSRange, found: UnsafeMutablePointer<NSRange>?) -> Bool](nsapplication/searchstring(_:inuserinterfaceitemstring:range:found:).md)
  Searches for the string in the user interface.
- [func unregisterUserInterfaceItemSearchHandler(any NSUserInterfaceItemSearching)](nsapplication/unregisteruserinterfaceitemsearchhandler(_:).md)
  Unregister an object that provides help data to your app.
- [func showHelp(Any?)](nsapplication/showhelp(_:).md)
  If your project is properly registered, and the necessary keys have been set in the property list, this method launches Help Viewer and displays the first page of your app’s help book.
- [func activateContextHelpMode(Any?)](nsapplication/activatecontexthelpmode(_:).md)
  Places the receiver in context-sensitive help mode.
- [var helpMenu: NSMenu?](nsapplication/helpmenu.md)
  The help menu used by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/registeruserinterfaceitemsearchhandler(_:))*