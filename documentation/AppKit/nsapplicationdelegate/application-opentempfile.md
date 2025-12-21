# application(_:openTempFile:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates if the app opens the specified temporary file.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func application(_ sender: NSApplication, openTempFile filename: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the file was successfully opened or [`false`](https://developer.apple.com/documentation/Swift/false) if it was not.

#### Discussion

Sent directly by `theApplication` to the delegate. The method should attempt to open the file `filename`, returning [`true`](https://developer.apple.com/documentation/Swift/true) if the file is successfully opened, and [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

By design, a file opened through this method is assumed to be temporary—it’s the application’s responsibility to remove the file at the appropriate time.

## Parameters

- `sender`: The application object associated with the delegate.
- `filename`: The name of the temporary file to open.

## See Also

- [func application(NSApplication, open: [URL])](nsapplicationdelegate/application(_:open:).md)
  Tells the delegate to open the resource at the specified URL.
- [func application(NSApplication, openFile: String) -> Bool](nsapplicationdelegate/application(_:openfile:).md)
  Returns a Boolean value that indicates if the app opens the specified file.
- [func application(Any, openFileWithoutUI: String) -> Bool](nsapplicationdelegate/application(_:openfilewithoutui:).md)
  Returns a Boolean value that indicates if the app opens the specified file without showing its user interface.
- [func application(NSApplication, openFiles: [String])](nsapplicationdelegate/application(_:openfiles:).md)
  Tells the delegate to open the specified files.
- [func applicationShouldOpenUntitledFile(NSApplication) -> Bool](nsapplicationdelegate/applicationshouldopenuntitledfile(_:).md)
  Returns a Boolean value that indicates if the app can open an untitled file.
- [func applicationOpenUntitledFile(NSApplication) -> Bool](nsapplicationdelegate/applicationopenuntitledfile(_:).md)
  Returns a Boolean value that indicates if the app opens an untitled file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:opentempfile:))*