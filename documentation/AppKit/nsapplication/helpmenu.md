# helpMenu

**Framework**: AppKit  
**Kind**: property

The help menu used by the app.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var helpMenu: NSMenu? { get set }
```

#### Discussion

Use this property to specify your app’s Help menu. When this property contains a valid menu, the system installs its Spotlight-related menu items on that menu. When the value is `nil`, AppKit installs Spotlight menu items on the menu of its choosing. To suppress Spotlight help items altogether, specify a menu that doesn’t appear on the menu bar.

## See Also

- [func registerUserInterfaceItemSearchHandler(any NSUserInterfaceItemSearching)](nsapplication/registeruserinterfaceitemsearchhandler(_:).md)
  Register an object that provides help data to your app.
- [func searchString(String, inUserInterfaceItemString: String, range: NSRange, found: UnsafeMutablePointer<NSRange>?) -> Bool](nsapplication/searchstring(_:inuserinterfaceitemstring:range:found:).md)
  Searches for the string in the user interface.
- [func unregisterUserInterfaceItemSearchHandler(any NSUserInterfaceItemSearching)](nsapplication/unregisteruserinterfaceitemsearchhandler(_:).md)
  Unregister an object that provides help data to your app.
- [func showHelp(Any?)](nsapplication/showhelp(_:).md)
  If your project is properly registered, and the necessary keys have been set in the property list, this method launches Help Viewer and displays the first page of your app’s help book.
- [func activateContextHelpMode(Any?)](nsapplication/activatecontexthelpmode(_:).md)
  Places the receiver in context-sensitive help mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/helpmenu)*