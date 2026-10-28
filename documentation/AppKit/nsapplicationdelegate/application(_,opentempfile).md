# application(_:openTempFile:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates if the app opens the specified temporary file.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func application(_ sender: NSApplication, openTempFile filename: String) -> Bool
```

```objc
- (BOOL) application:(NSApplication *) sender openTempFile:(NSString *) filename;
```

## Return Value

[`true`](../../Swift/true.md) if the file was successfully opened or [`false`](../../Swift/false.md) if it was not.

## Discussion

Sent directly by `theApplication` to the delegate. The method should attempt to open the file `filename`, returning [`true`](../../Swift/true.md) if the file is successfully opened, and [`false`](../../Swift/false.md) otherwise.

By design, a file opened through this method is assumed to be temporary—it’s the application’s responsibility to remove the file at the appropriate time.

## Parameters

- `sender`: The application object associated with the delegate.
- `filename`: The name of the temporary file to open.

## See Also

### Opening Files
- [func application(NSApplication, open: [URL])](./application%28_,open%29.md)
  Tells the delegate to open the resource at the specified URL.
- [func application(NSApplication, openFile: String) -> Bool](./application%28_,openfile%29.md)
  Returns a Boolean value that indicates if the app opens the specified file.
- [func application(Any, openFileWithoutUI: String) -> Bool](./application%28_,openfilewithoutui%29.md)
  Returns a Boolean value that indicates if the app opens the specified file without showing its user interface.
- [func application(NSApplication, openFiles: [String])](./application%28_,openfiles%29.md)
  Tells the delegate to open the specified files.
- [func applicationShouldOpenUntitledFile(NSApplication) -> Bool](./applicationshouldopenuntitledfile%28_%29.md)
  Returns a Boolean value that indicates if the app can open an untitled file.
- [func applicationOpenUntitledFile(NSApplication) -> Bool](./applicationopenuntitledfile%28_%29.md)
  Returns a Boolean value that indicates if the app opens an untitled file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:opentempfile:))*