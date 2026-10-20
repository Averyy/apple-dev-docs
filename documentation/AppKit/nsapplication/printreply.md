# NSApplication.PrintReply

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the outcome of a print request.

**Availability**:
- macOS

## Declaration

```swift
enum PrintReply
```

```c
enum NSApplicationPrintReply : NSUInteger;
```

## Topics

### Constants
- [NSApplication.PrintReply.printingCancelled](./printreply/printingcancelled.md)
  Printing was cancelled.
- [NSApplication.PrintReply.printingSuccess](./printreply/printingsuccess.md)
  Printing was successful.
- [NSApplication.PrintReply.printingFailure](./printreply/printingfailure.md)
  Printing failed.
- [NSApplication.PrintReply.printingReplyLater](./printreply/printingreplylater.md)
### Initializers
- [init?(rawValue: UInt)](./printreply/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Printing
- [func application(NSApplication, printFile: String) -> Bool](../nsapplicationdelegate/application%28_,printfile%29.md)
  Returns a Boolean value that indicates if the app prints the specified file in its entirety.
- [func application(NSApplication, printFiles: [String], withSettings: [NSPrintInfo.AttributeKey : Any], showPrintPanels: Bool) -> NSApplication.PrintReply](../nsapplicationdelegate/application%28_,printfiles,withsettings,showprintpanels%29.md)
  Returns a value that indicates if the app prints the specified files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/printreply)*