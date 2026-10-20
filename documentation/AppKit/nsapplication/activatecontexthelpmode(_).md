# activateContextHelpMode(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Places the receiver in context-sensitive help mode.

**Availability**:
- macOS

## Declaration

```swift
func activateContextHelpMode(_ sender: Any?)
```

```objc
- (void) activateContextHelpMode:(id) sender;
```

#### Discussion

In this mode, the cursor becomes a question mark, and help appears for any user interface item the user clicks.

Most apps don’t use this method. Instead, apps enter context-sensitive mode when the user presses the Help key. Apps exit context-sensitive help mode upon the first event after a help window is displayed.

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
- [func showHelp(Any?)](./showhelp%28_%29.md)
  If your project is properly registered, and the necessary keys have been set in the property list, this method launches Help Viewer and displays the first page of your app’s help book.
- [var helpMenu: NSMenu?](./helpmenu.md)
  The help menu used by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/activatecontexthelpmode(_:))*