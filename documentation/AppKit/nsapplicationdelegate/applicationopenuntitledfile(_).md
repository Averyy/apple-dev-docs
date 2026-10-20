# applicationOpenUntitledFile(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates if the app opens an untitled file.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func applicationOpenUntitledFile(_ sender: NSApplication) -> Bool
```

```objc
- (BOOL) applicationOpenUntitledFile:(NSApplication *) sender;
```

#### Return Value

[`true`](../../Swift/true.md) if the file was successfully opened or [`false`](../../Swift/false.md) if it was not.

#### Discussion

Sent directly by `theApplication` to the delegate to request that a new, untitled file be opened.

## Parameters

- `sender`: The application object associated with the delegate.

## See Also

### Opening Files
- [func application(NSApplication, open: [URL])](./application%28_,open%29.md)
  Tells the delegate to open the resource at the specified URL.
- [func application(NSApplication, openFile: String) -> Bool](./application%28_,openfile%29.md)
  Returns a Boolean value that indicates if the app opens the specified file.
- [func application(Any, openFileWithoutUI: String) -> Bool](./application%28_,openfilewithoutui%29.md)
  Returns a Boolean value that indicates if the app opens the specified file without showing its user interface.
- [func application(NSApplication, openTempFile: String) -> Bool](./application%28_,opentempfile%29.md)
  Returns a Boolean value that indicates if the app opens the specified temporary file.
- [func application(NSApplication, openFiles: [String])](./application%28_,openfiles%29.md)
  Tells the delegate to open the specified files.
- [func applicationShouldOpenUntitledFile(NSApplication) -> Bool](./applicationshouldopenuntitledfile%28_%29.md)
  Returns a Boolean value that indicates if the app can open an untitled file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationopenuntitledfile(_:))*