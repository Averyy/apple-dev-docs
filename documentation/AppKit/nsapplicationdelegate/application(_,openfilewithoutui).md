# application(_:openFileWithoutUI:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates if the app opens the specified file without showing its user interface.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func application(_ sender: Any, openFileWithoutUI filename: String) -> Bool
```

```objc
- (BOOL) application:(id) sender openFileWithoutUI:(NSString *) filename;
```

#### Return Value

[`true`](../../Swift/true.md) if the file was successfully opened or [`false`](../../Swift/false.md) if it was not.

#### Discussion

Sent directly by `sender` to the delegate to request that the file `filename` be opened as a linked file. The method should open the file without bringing up its application’s user interface—that is, work with the file is under programmatic control of `sender`, rather than under keyboard control of the user.

## Parameters

- `sender`: The object that sent the command.
- `filename`: The name of the file to open.

## See Also

### Related Documentation
- [func application(NSApplication, printFile: String) -> Bool](./application%28_,printfile%29.md)
  Returns a Boolean value that indicates if the app prints the specified file in its entirety.
### Opening Files
- [func application(NSApplication, open: [URL])](./application%28_,open%29.md)
  Tells the delegate to open the resource at the specified URL.
- [func application(NSApplication, openFile: String) -> Bool](./application%28_,openfile%29.md)
  Returns a Boolean value that indicates if the app opens the specified file.
- [func application(NSApplication, openTempFile: String) -> Bool](./application%28_,opentempfile%29.md)
  Returns a Boolean value that indicates if the app opens the specified temporary file.
- [func application(NSApplication, openFiles: [String])](./application%28_,openfiles%29.md)
  Tells the delegate to open the specified files.
- [func applicationShouldOpenUntitledFile(NSApplication) -> Bool](./applicationshouldopenuntitledfile%28_%29.md)
  Returns a Boolean value that indicates if the app can open an untitled file.
- [func applicationOpenUntitledFile(NSApplication) -> Bool](./applicationopenuntitledfile%28_%29.md)
  Returns a Boolean value that indicates if the app opens an untitled file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:openfilewithoutui:))*