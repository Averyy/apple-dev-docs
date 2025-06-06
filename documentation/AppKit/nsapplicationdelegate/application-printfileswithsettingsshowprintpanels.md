# application(_:printFiles:withSettings:showPrintPanels:)

**Framework**: AppKit  
**Kind**: method

Returns a value that indicates if the app prints the specified files.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func application(_ application: NSApplication, printFiles fileNames: [String], withSettings printSettings: [NSPrintInfo.AttributeKey : Any], showPrintPanels: Bool) -> NSApplication.PrintReply
```

#### Return Value

A constant indicating whether printing was successful. For a list of possible values, see [`NSApplication.PrintReply`](nsapplication/printreply.md).

#### Discussion

Return `NSPrintingReplyLater` if the result of printing cannot be returned immediately, for example, if printing will cause the presentation of a sheet. If your method returns `NSPrintingReplyLater` it must always invoke the `NSApplication` method [`reply(toOpenOrPrint:)`](nsapplication/reply(toopenorprint:).md)] when the entire print operation has been completed, successfully or not.

This delegate method replaces `application:printFiles:`, which is now deprecated. If your application delegate only implements the deprecated method, it is still invoked, and `NSApplication` uses private functionality to arrange for the print settings to take effect.

## Parameters

- `application`: The application object that is handling the printing.
- `fileNames`: An array of   objects, each of which contains the name of a file to print.
- `printSettings`: A dictionary containing  -compatible print job attributes.
- `showPrintPanels`: A Boolean that specifies whether the print panel should be displayed for each file printed. Print progress indicators will be presented even if this value is  .

## See Also

- [func application(NSApplication, printFile: String) -> Bool](nsapplicationdelegate/application(_:printfile:).md)
  Returns a Boolean value that indicates if the app prints the specified file in its entirety.
- [NSApplication.PrintReply](nsapplication/printreply.md)
  Constants that indicate the outcome of a print request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:printfiles:withsettings:showprintpanels:))*