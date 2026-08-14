# NSApplication.PrintReply

**Framework**: AppKit  
**Kind**: enum

Constants that indicate the outcome of a print request.

**Availability**:
- macOS ?+

## Declaration

```swift
enum PrintReply
```

## Topics

### Constants
- [NSApplication.PrintReply.printingCancelled](nsapplication/printreply/printingcancelled.md)
  Printing was cancelled.
- [NSApplication.PrintReply.printingSuccess](nsapplication/printreply/printingsuccess.md)
  Printing was successful.
- [NSApplication.PrintReply.printingFailure](nsapplication/printreply/printingfailure.md)
  Printing failed.
- [NSApplication.PrintReply.printingReplyLater](nsapplication/printreply/printingreplylater.md)
### Initializers
- [init?(rawValue: UInt)](nsapplication/printreply/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func application(NSApplication, printFile: String) -> Bool](nsapplicationdelegate/application(_:printfile:).md)
  Returns a Boolean value that indicates if the app prints the specified file in its entirety.
- [func application(NSApplication, printFiles: [String], withSettings: [NSPrintInfo.AttributeKey : Any], showPrintPanels: Bool) -> NSApplication.PrintReply](nsapplicationdelegate/application(_:printfiles:withsettings:showprintpanels:).md)
  Returns a value that indicates if the app prints the specified files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/printreply)*