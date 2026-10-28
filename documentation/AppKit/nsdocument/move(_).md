# move(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves the document to a new location in response to the user choosing the Move To… menu item.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@IBAction
func move(_ sender: Any?)
```

```objc
- (void) moveDocument:(id) sender;
```

## Discussion

This is the action method of the Move To… menu item in a document-based app. By default, this method invokes the [`move(completionHandler:)`](./move%28completionhandler%29.md) method, passing `nil` as a parameter value.

## Parameters

- `sender`: The control sending the message.

## See Also

### Moving the Document
- [func move(completionHandler: ((Bool) -> Void)?)](./move%28completionhandler%29.md)
  Moves the document to a user-selected location.
- [func move(to: URL, completionHandler: (((any Error)?) -> Void)?)](./move%28to,completionhandler%29.md)
  Moves the document’s file to the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/move(_:))*