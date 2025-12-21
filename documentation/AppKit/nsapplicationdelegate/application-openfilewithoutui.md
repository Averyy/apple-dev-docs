# application(_:openFileWithoutUI:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates if the app opens the specified file without showing its user interface.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func application(_ sender: Any, openFileWithoutUI filename: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the file was successfully opened or [`false`](https://developer.apple.com/documentation/Swift/false) if it was not.

#### Discussion

Sent directly by `sender` to the delegate to request that the file `filename` be opened as a linked file. The method should open the file without bringing up its application’s user interface—that is, work with the file is under programmatic control of `sender`, rather than under keyboard control of the user.

## Parameters

- `sender`: The object that sent the command.
- `filename`: The name of the file to open.

## See Also

- [func application(NSApplication, printFile: String) -> Bool](nsapplicationdelegate/application(_:printfile:).md)
  Returns a Boolean value that indicates if the app prints the specified file in its entirety.
- [func application(NSApplication, open: [URL])](nsapplicationdelegate/application(_:open:).md)
  Tells the delegate to open the resource at the specified URL.
- [func application(NSApplication, openFile: String) -> Bool](nsapplicationdelegate/application(_:openfile:).md)
  Returns a Boolean value that indicates if the app opens the specified file.
- [func application(NSApplication, openTempFile: String) -> Bool](nsapplicationdelegate/application(_:opentempfile:).md)
  Returns a Boolean value that indicates if the app opens the specified temporary file.
- [func application(NSApplication, openFiles: [String])](nsapplicationdelegate/application(_:openfiles:).md)
  Tells the delegate to open the specified files.
- [func applicationShouldOpenUntitledFile(NSApplication) -> Bool](nsapplicationdelegate/applicationshouldopenuntitledfile(_:).md)
  Returns a Boolean value that indicates if the app can open an untitled file.
- [func applicationOpenUntitledFile(NSApplication) -> Bool](nsapplicationdelegate/applicationopenuntitledfile(_:).md)
  Returns a Boolean value that indicates if the app opens an untitled file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:openfilewithoutui:))*