# applicationShouldOpenUntitledFile(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates if the app can open an untitled file.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func applicationShouldOpenUntitledFile(_ sender: NSApplication) -> Bool
```

```objc
- (BOOL) applicationShouldOpenUntitledFile:(NSApplication *) sender;
```

## Return Value

[`true`](../../Swift/true.md) if the application should open a new untitled file or [`false`](../../Swift/false.md) if it should not.

## Discussion

Use this method to decide whether the application should open a new, untitled file. Note that [`applicationOpenUntitledFile(_:)`](./applicationopenuntitledfile%28_%29.md) is invoked if this method returns [`true`](../../Swift/true.md).

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
- [func applicationOpenUntitledFile(NSApplication) -> Bool](./applicationopenuntitledfile%28_%29.md)
  Returns a Boolean value that indicates if the app opens an untitled file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationshouldopenuntitledfile(_:))*