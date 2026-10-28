# application(_:openFiles:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate to open the specified files.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func application(_ sender: NSApplication, openFiles filenames: [String])
```

```objc
- (void) application:(NSApplication *) sender openFiles:(NSArray<NSString *> *) filenames;
```

## Discussion

Identical to [`application(_:openFile:)`](./application%28_,openfile%29.md) except that the receiver opens multiple files corresponding to the file names in the `filenames` array. Delegates should invoke the [`reply(toOpenOrPrint:)`](../nsapplication/reply%28toopenorprint%29.md) method upon success or failure, or when the user cancels the operation.

## Parameters

- `sender`: The application object associated with the delegate.
- `filenames`: An array of `NSString` objects containing the names of the files to open..

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
- [func applicationShouldOpenUntitledFile(NSApplication) -> Bool](./applicationshouldopenuntitledfile%28_%29.md)
  Returns a Boolean value that indicates if the app can open an untitled file.
- [func applicationOpenUntitledFile(NSApplication) -> Bool](./applicationopenuntitledfile%28_%29.md)
  Returns a Boolean value that indicates if the app opens an untitled file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:openfiles:))*