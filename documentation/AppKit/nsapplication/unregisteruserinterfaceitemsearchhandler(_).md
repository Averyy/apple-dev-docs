# unregisterUserInterfaceItemSearchHandler(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Unregister an object that provides help data to your app.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func unregisterUserInterfaceItemSearchHandler(_ handler: any NSUserInterfaceItemSearching)
```

```objc
- (void) unregisterUserInterfaceItemSearchHandler:(id<NSUserInterfaceItemSearching>) handler;
```

## Discussion

If you unregister the same instance more than once the subsequent invocations are ignored. Unregistering an instance that was never registered is ignored.

## Parameters

- `handler`: The class instance that conforms to `NSUserInterfaceItemSearching` and provides help content.

## See Also

### Providing help information
- [func registerUserInterfaceItemSearchHandler(any NSUserInterfaceItemSearching)](./registeruserinterfaceitemsearchhandler%28_%29.md)
  Register an object that provides help data to your app.
- [func searchString(String, inUserInterfaceItemString: String, range: NSRange, found: UnsafeMutablePointer<NSRange>?) -> Bool](./searchstring%28_,inuserinterfaceitemstring,range,found%29.md)
  Searches for the string in the user interface.
- [func showHelp(Any?)](./showhelp%28_%29.md)
  If your project is properly registered, and the necessary keys have been set in the property list, this method launches Help Viewer and displays the first page of your app’s help book.
- [func activateContextHelpMode(Any?)](./activatecontexthelpmode%28_%29.md)
  Places the receiver in context-sensitive help mode.
- [var helpMenu: NSMenu?](./helpmenu.md)
  The help menu used by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/unregisteruserinterfaceitemsearchhandler(_:))*