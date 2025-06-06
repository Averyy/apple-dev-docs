# applicationOpenUntitledFile(_:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates if the app opens an untitled file.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func applicationOpenUntitledFile(_ sender: NSApplication) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the file was successfully opened or [`false`](https://developer.apple.com/documentation/swift/false) if it was not.

#### Discussion

Sent directly by `theApplication` to the delegate to request that a new, untitled file be opened.

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
- [func applicationShouldOpenUntitledFile(NSApplication) -> Bool](nsapplicationdelegate/applicationshouldopenuntitledfile(_:).md)
  Returns a Boolean value that indicates if the app can open an untitled file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationopenuntitledfile(_:))*