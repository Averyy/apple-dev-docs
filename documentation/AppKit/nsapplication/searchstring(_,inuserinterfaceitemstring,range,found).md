# searchString(_:inUserInterfaceItemString:range:found:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Searches for the string in the user interface.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func searchString(_ searchString: String, inUserInterfaceItemString stringToSearch: String, range searchRange: NSRange, found foundRange: UnsafeMutablePointer<NSRange>?) -> Bool
```

```objc
- (BOOL) searchString:(NSString *) searchString inUserInterfaceItemString:(NSString *) stringToSearch searchRange:(NSRange) searchRange foundRange:(NSRange *) foundRange;
```

#### Return Value

[`true`](../../Swift/true.md) if the searchString is matched, otherwise [`false`](../../Swift/false.md).

#### Discussion

The search uses the default matching rules for Spotlight for Help.

## Parameters

- `searchString`: The search string.
- `stringToSearch`: The string to search.
- `searchRange`: The subrange of the `stringToSearch` to restrict the search to.
- `foundRange`: Returns, by-reference, the range of the `searchString` within `stringToSearch`.

## See Also

### Providing help information
- [func registerUserInterfaceItemSearchHandler(any NSUserInterfaceItemSearching)](./registeruserinterfaceitemsearchhandler%28_%29.md)
  Register an object that provides help data to your app.
- [func unregisterUserInterfaceItemSearchHandler(any NSUserInterfaceItemSearching)](./unregisteruserinterfaceitemsearchhandler%28_%29.md)
  Unregister an object that provides help data to your app.
- [func showHelp(Any?)](./showhelp%28_%29.md)
  If your project is properly registered, and the necessary keys have been set in the property list, this method launches Help Viewer and displays the first page of your app’s help book.
- [func activateContextHelpMode(Any?)](./activatecontexthelpmode%28_%29.md)
  Places the receiver in context-sensitive help mode.
- [var helpMenu: NSMenu?](./helpmenu.md)
  The help menu used by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/searchstring(_:inuserinterfaceitemstring:range:found:))*