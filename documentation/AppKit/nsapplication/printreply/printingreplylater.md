# NSApplication.PrintReply.printingReplyLater

**Framework**: AppKit  
**Kind**: case

**Availability**:
- macOS ?+

## Declaration

```swift
case printingReplyLater
```

#### Discussion

The result of printing cannot be returned immediately, for example, if printing will cause the presentation of a sheet. If your method returns `NSPrintingReplyLater` it must always invoke [`reply(toOpenOrPrint:)`](nsapplication/reply(toopenorprint:).md) when the entire print operation has been completed, successfully or not.

## See Also

- [NSApplication.PrintReply.printingCancelled](nsapplication/printreply/printingcancelled.md)
  Printing was cancelled.
- [NSApplication.PrintReply.printingSuccess](nsapplication/printreply/printingsuccess.md)
  Printing was successful.
- [NSApplication.PrintReply.printingFailure](nsapplication/printreply/printingfailure.md)
  Printing failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/printreply/printingreplylater)*