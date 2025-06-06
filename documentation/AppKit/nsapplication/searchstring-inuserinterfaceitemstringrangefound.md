# searchString(_:inUserInterfaceItemString:range:found:)

**Framework**: AppKit  
**Kind**: method

Searches for the string in the user interface.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func searchString(_ searchString: String, inUserInterfaceItemString stringToSearch: String, range searchRange: NSRange, found foundRange: UnsafeMutablePointer<NSRange>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the searchString is matched, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The search uses the default matching rules for Spotlight for Help.

## Parameters

- `searchString`: The search string.
- `stringToSearch`: The string to search.
- `searchRange`: The subrange of the   to restrict the search to.
- `foundRange`: Returns, by-reference, the range of the   within  .

## See Also

- [func registerUserInterfaceItemSearchHandler(any NSUserInterfaceItemSearching)](nsapplication/registeruserinterfaceitemsearchhandler(_:).md)
  Register an object that provides help data to your app.
- [func unregisterUserInterfaceItemSearchHandler(any NSUserInterfaceItemSearching)](nsapplication/unregisteruserinterfaceitemsearchhandler(_:).md)
  Unregister an object that provides help data to your app.
- [func showHelp(Any?)](nsapplication/showhelp(_:).md)
  If your project is properly registered, and the necessary keys have been set in the property list, this method launches Help Viewer and displays the first page of your app’s help book.
- [func activateContextHelpMode(Any?)](nsapplication/activatecontexthelpmode(_:).md)
  Places the receiver in context-sensitive help mode.
- [var helpMenu: NSMenu?](nsapplication/helpmenu.md)
  The help menu used by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/searchstring(_:inuserinterfaceitemstring:range:found:))*