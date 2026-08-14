# application(_:openFile:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates if the app opens the specified file.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func application(_ sender: NSApplication, openFile filename: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the file was successfully opened or [`false`](https://developer.apple.com/documentation/swift/false) if it was not.

#### Discussion

Sent directly by `theApplication` to the delegate. The method should open the file `filename`, returning [`true`](https://developer.apple.com/documentation/swift/true) if the file is successfully opened, and [`false`](https://developer.apple.com/documentation/swift/false) otherwise. If the user started up the application by double-clicking a file, the delegate receives the [`application(_:openFile:)`](nsapplicationdelegate/application(_:openfile:).md) message before receiving [`applicationDidFinishLaunching(_:)`](nsapplicationdelegate/applicationdidfinishlaunching(_:).md). ([`applicationWillFinishLaunching(_:)`](nsapplicationdelegate/applicationwillfinishlaunching(_:).md) is sent before [`application(_:openFile:)`](nsapplicationdelegate/application(_:openfile:).md).)

## Parameters

- `sender`: The application object associated with the delegate.
- `filename`: The name of the file to open.

## See Also

- [func application(NSApplication, open: [URL])](nsapplicationdelegate/application(_:open:).md)
  Tells the delegate to open the resource at the specified URL.
- [func application(Any, openFileWithoutUI: String) -> Bool](nsapplicationdelegate/application(_:openfilewithoutui:).md)
  Returns a Boolean value that indicates if the app opens the specified file without showing its user interface.
- [func application(NSApplication, openTempFile: String) -> Bool](nsapplicationdelegate/application(_:opentempfile:).md)
  Returns a Boolean value that indicates if the app opens the specified temporary file.
- [func application(NSApplication, openFiles: [String])](nsapplicationdelegate/application(_:openfiles:).md)
  Tells the delegate to open the specified files.
- [func applicationShouldOpenUntitledFile(NSApplication) -> Bool](nsapplicationdelegate/applicationshouldopenuntitledfile(_:).md)
  Returns a Boolean value that indicates if the app can open an untitled file.
- [func applicationOpenUntitledFile(NSApplication) -> Bool](nsapplicationdelegate/applicationopenuntitledfile(_:).md)
  Returns a Boolean value that indicates if the app opens an untitled file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:openfile:))*