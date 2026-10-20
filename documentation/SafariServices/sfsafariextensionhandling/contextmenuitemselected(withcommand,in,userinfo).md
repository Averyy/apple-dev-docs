# contextMenuItemSelected(withCommand:in:userInfo:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

A method the system calls when a user selects one of the app extension’s context menu items.

**Availability**:
- macOS 10.12+

## Declaration

```swift
optional func contextMenuItemSelected(withCommand command: String, in page: SFSafariPage, userInfo: [String : Any]? = nil)
```

```objc
- (void) contextMenuItemSelectedWithCommand:(NSString *) command inPage:(SFSafariPage *) page userInfo:(NSDictionary<NSString *,id> *) userInfo;
```

## Mentions

- [Adjusting settings for contextual menu items](../adjusting-settings-for-contextual-menu-items.md)

## Parameters

- `command`: The command that is associated with the selected context menu item specified in `Info.plist`.
- `page`: The page where the context menu item was selected.
- `userInfo`: Optional message content. If specified, the dictionary’s value objects conform to the W3C standard for safe passing of structured data, such as Boolean objects, numeric values, strings, and arrays.

## See Also

### Responding to Context Menu Selections
- [func validateContextMenuItem(withCommand: String, in: SFSafariPage, userInfo: [String : Any]?, validationHandler: (Bool, String?) -> Void)](./validatecontextmenuitem%28withcommand,in,userinfo,validationhandler%29.md)
  Validates whether a particular contextual menu item should be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/contextmenuitemselected(withcommand:in:userinfo:))*