# ILClassificationAction.reportNotJunk

**Framework**: SMS and Call Reporting  
**Kind**: case

The system should report that the communication is not junk.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
case reportNotJunk
```

#### Discussion

The extension creates an SMS message based on the response, and displays the message to the user. The user can then send or cancel the report. Finally, the extension dismisses the [`ILClassificationUIExtensionViewController`](https://developer.apple.com/documentation/identitylookupui/ilclassificationuiextensionviewcontroller).

## See Also

- [ILClassificationAction.none](ilclassificationaction/none.md)
  No action is required.
- [ILClassificationAction.reportJunk](ilclassificationaction/reportjunk.md)
  The system should report the communication as junk.
- [ILClassificationAction.reportJunkAndBlockSender](ilclassificationaction/reportjunkandblocksender.md)
  The system should report the communication as junk and add the number to the system’s block list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilclassificationaction/reportnotjunk)*