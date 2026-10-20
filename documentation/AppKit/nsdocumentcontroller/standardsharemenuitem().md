# standardShareMenuItem()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a menu item that your app uses for sharing the current document.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func standardShareMenuItem() -> NSMenuItem
```

```objc
- (NSMenuItem *) standardShareMenuItem;
```

#### Return Value

An [`NSMenuItem`](../nsmenuitem.md) for the Share menu.

#### Discussion

Use this method to perform custom placement of the Share menu if your [`NSDocument`](../nsdocument.md) subclass returns `false` for [`allowsAutomaticShareMenu`](./allowsautomaticsharemenu.md).

## See Also

### Sharing
- [var allowsAutomaticShareMenu: Bool](./allowsautomaticsharemenu.md)
  A Boolean value that the system uses to insert a Share menu in the File menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/standardsharemenuitem())*