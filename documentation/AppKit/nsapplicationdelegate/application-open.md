# application(_:open:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate to open the resource at the specified URL.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@MainActor
optional func application(_ application: NSApplication, open urls: [URL])
```

#### Discussion

AppKit calls this method when your app is asked to open one or more URL-based resources. You must declare the URL types that your app supports in your `Info.plist` file using the `CFBundleURLTypes` key. The list can also include URLs for documents for which your app does not have an associated [`NSDocument`](nsdocument.md) class. You configure document types using Xcode, or by adding the `CFBundleDocumentTypes` key to your `Info.plist` file.

If your delegate implements this method, AppKit does not call the [`application(_:openFile:)`](nsapplicationdelegate/application(_:openfile:).md) or [`application(_:openFiles:)`](nsapplicationdelegate/application(_:openfiles:).md) methods.

## Parameters

- `application`: Your singleton app object.
- `urls`: An array of URLs to open. The list does not include URLs for which your app has a defined document type.

## See Also

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
- [func applicationOpenUntitledFile(NSApplication) -> Bool](nsapplicationdelegate/applicationopenuntitledfile(_:).md)
  Returns a Boolean value that indicates if the app opens an untitled file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:open:))*