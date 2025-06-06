# activateContextHelpMode(_:)

**Framework**: AppKit  
**Kind**: method

Places the receiver in context-sensitive help mode.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func activateContextHelpMode(_ sender: Any?)
```

#### Discussion

In this mode, the cursor becomes a question mark, and help appears for any user interface item the user clicks.

Most apps don’t use this method. Instead, apps enter context-sensitive mode when the user presses the Help key. Apps exit context-sensitive help mode upon the first event after a help window is displayed.

## Parameters

- `sender`: The object that sent the command.

## See Also

- [func registerUserInterfaceItemSearchHandler(any NSUserInterfaceItemSearching)](nsapplication/registeruserinterfaceitemsearchhandler(_:).md)
  Register an object that provides help data to your app.
- [func searchString(String, inUserInterfaceItemString: String, range: NSRange, found: UnsafeMutablePointer<NSRange>?) -> Bool](nsapplication/searchstring(_:inuserinterfaceitemstring:range:found:).md)
  Searches for the string in the user interface.
- [func unregisterUserInterfaceItemSearchHandler(any NSUserInterfaceItemSearching)](nsapplication/unregisteruserinterfaceitemsearchhandler(_:).md)
  Unregister an object that provides help data to your app.
- [func showHelp(Any?)](nsapplication/showhelp(_:).md)
  If your project is properly registered, and the necessary keys have been set in the property list, this method launches Help Viewer and displays the first page of your app’s help book.
- [var helpMenu: NSMenu?](nsapplication/helpmenu.md)
  The help menu used by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/activatecontexthelpmode(_:))*