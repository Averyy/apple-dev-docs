# application(_:printFile:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates if the app prints the specified file in its entirety.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func application(_ sender: NSApplication, printFile filename: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the file was successfully printed or [`false`](https://developer.apple.com/documentation/Swift/false) if it was not.

#### Discussion

This message is sent directly by `theApplication` to the delegate. The application terminates (using the [`terminate(_:)`](nsapplication/terminate(_:).md) method) after this method returns.

If at all possible, this method should print the file without displaying the user interface. For example, if you pass the `-NSPrint` option to the TextEdit application, TextEdit assumes you want to print the entire contents of the specified file. However, if the application opens more complex documents, you may want to display a panel that lets the user choose exactly what they want to print.

## Parameters

- `sender`: The application object that is handling the printing.
- `filename`: The name of the file to print.

## See Also

- [func application(Any, openFileWithoutUI: String) -> Bool](nsapplicationdelegate/application(_:openfilewithoutui:).md)
  Returns a Boolean value that indicates if the app opens the specified file without showing its user interface.
- [func application(NSApplication, printFiles: [String], withSettings: [NSPrintInfo.AttributeKey : Any], showPrintPanels: Bool) -> NSApplication.PrintReply](nsapplicationdelegate/application(_:printfiles:withsettings:showprintpanels:).md)
  Returns a value that indicates if the app prints the specified files.
- [NSApplication.PrintReply](nsapplication/printreply.md)
  Constants that indicate the outcome of a print request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:printfile:))*