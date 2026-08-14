# applicationShouldOpenUntitledFile(_:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates if the app can open an untitled file.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func applicationShouldOpenUntitledFile(_ sender: NSApplication) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the application should open a new untitled file or [`false`](https://developer.apple.com/documentation/swift/false) if it should not.

#### Discussion

Use this method to decide whether the application should open a new, untitled file. Note that [`applicationOpenUntitledFile(_:)`](nsapplicationdelegate/applicationopenuntitledfile(_:).md) is invoked if this method returns [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `sender`: The application object associated with the delegate.

## See Also

- [func application(NSApplication, open: [URL])](nsapplicationdelegate/application(_:open:).md)
  Tells the delegate to open the resource at the specified URL.
- [func application(NSApplication, openFile: String) -> Bool](nsapplicationdelegate/application(_:openfile:).md)
  Returns a Boolean value that indicates if the app opens the specified file.
- [func application(Any, openFileWithoutUI: String) -> Bool](nsapplicationdelegate/application(_:openfilewithoutui:).md)
  Returns a Boolean value that indicates if the app opens the specified file without showing its user interface.
- [func application(NSApplication, openTempFile: String) -> Bool](nsapplicationdelegate/application(_:opentempfile:).md)
  Returns a Boolean value that indicates if the app opens the specified temporary file.
- [func application(NSApplication, openFiles: [String])](nsapplicationdelegate/application(_:openfiles:).md)
  Tells the delegate to open the specified files.
- [func applicationOpenUntitledFile(NSApplication) -> Bool](nsapplicationdelegate/applicationopenuntitledfile(_:).md)
  Returns a Boolean value that indicates if the app opens an untitled file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationshouldopenuntitledfile(_:))*