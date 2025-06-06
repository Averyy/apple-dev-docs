# application(_:openFiles:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate to open the specified files.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func application(_ sender: NSApplication, openFiles filenames: [String])
```

#### Discussion

Identical to [`application(_:openFile:)`](nsapplicationdelegate/application(_:openfile:).md) except that the receiver opens multiple files corresponding to the file names in the `filenames` array. Delegates should invoke the [`reply(toOpenOrPrint:)`](nsapplication/reply(toopenorprint:).md) method upon success or failure, or when the user cancels the operation.

## Parameters

- `sender`: The application object associated with the delegate.
- `filenames`: An array of   objects containing the names of the files to open..

## See Also

- [func application(NSApplication, open: [URL])](nsapplicationdelegate/application(_:open:).md)
  Tells the delegate to open the resource at the specified URL.
- [func application(NSApplication, openFile: String) -> Bool](nsapplicationdelegate/application(_:openfile:).md)
  Returns a Boolean value that indicates if the app opens the specified file.
- [func application(Any, openFileWithoutUI: String) -> Bool](nsapplicationdelegate/application(_:openfilewithoutui:).md)
  Returns a Boolean value that indicates if the app opens the specified file without showing its user interface.
- [func application(NSApplication, openTempFile: String) -> Bool](nsapplicationdelegate/application(_:opentempfile:).md)
  Returns a Boolean value that indicates if the app opens the specified temporary file.
- [func applicationShouldOpenUntitledFile(NSApplication) -> Bool](nsapplicationdelegate/applicationshouldopenuntitledfile(_:).md)
  Returns a Boolean value that indicates if the app can open an untitled file.
- [func applicationOpenUntitledFile(NSApplication) -> Bool](nsapplicationdelegate/applicationopenuntitledfile(_:).md)
  Returns a Boolean value that indicates if the app opens an untitled file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:openfiles:))*