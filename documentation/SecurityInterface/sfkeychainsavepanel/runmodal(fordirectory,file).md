# runModal(forDirectory:file:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Displays a panel that allows a user to create a new keychain.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func runModal(forDirectory path: String!, file name: String!) -> Int
```

```objc
- (NSInteger) runModalForDirectory:(NSString *) path file:(NSString *) name;
```

## Discussion

This method returns a result code from the [`runModalForDirectory:file:types:`](../../AppKit/nsopenpanel/runmodalfordirectory_file_types_.md) method of the [`NSSavePanel`](../../AppKit/nssavepanel.md) class: [`NSFileHandlingPanelOKButton`](../../AppKit/nsfilehandlingpanelokbutton.md) if the user clicks the OK button or [`NSFileHandlingPanelCancelButton`](../../AppKit/nsfilehandlingpanelcancelbutton.md) if the user clicks the Cancel button.

Use the [`keychain()`](./keychain%28%29.md) method to obtain the keychain created by the user.

## Parameters

- `path`: The path to the folder where the keychain is created. Specify `nil` for `~/Library/Keychains`.
- `name`: The keychain name to be automatically displayed in the Save As field of the panel.

## See Also

### Displaying a Sheet or Panel
- [func setPassword(String!)](./setpassword%28_%29.md)
  Specifies the password for the keychain that will be created.
- [func beginSheet(forDirectory: String!, file: String!, modalFor: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](./beginsheet%28fordirectory,file,modalfor,modaldelegate,didend,contextinfo%29.md)
  Displays a sheet that allows a user to create a new keychain.
### Related Documentation
- [- runModalForDirectory:file:types:](../../AppKit/nsopenpanel/runmodalfordirectory_file_types_.md)
  Displays the panel and begins a modal event loop that is terminated when the user clicks either OK or Cancel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfkeychainsavepanel/runmodal(fordirectory:file:))*