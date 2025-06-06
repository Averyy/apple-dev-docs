# standardShareMenuItem()

**Framework**: AppKit  
**Kind**: method

Returns a menu item that your app uses for sharing the current document.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@MainActor
func standardShareMenuItem() -> NSMenuItem
```

#### Return Value

An [`NSMenuItem`](nsmenuitem.md) for the Share menu.

#### Discussion

Use this method to perform custom placement of the Share menu if your [`NSDocument`](nsdocument.md) subclass returns `false` for [`allowsAutomaticShareMenu`](nsdocumentcontroller/allowsautomaticsharemenu.md).

## See Also

- [var allowsAutomaticShareMenu: Bool](nsdocumentcontroller/allowsautomaticsharemenu.md)
  A Boolean value that the system uses to insert a Share menu in the File menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/standardsharemenuitem())*