# reply(toOpenOrPrint:)

**Framework**: AppKit  
**Kind**: method

Handles errors that might occur when the user attempts to open or print files.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func reply(toOpenOrPrint reply: NSApplication.DelegateReply)
```

#### Discussion

Delegates should invoke this method if an error is encountered in the [`application(_:openFiles:)`](nsapplicationdelegate/application(_:openfiles:).md) or [`application(_:printFiles:withSettings:showPrintPanels:)`](nsapplicationdelegate/application(_:printfiles:withsettings:showprintpanels:).md) delegate methods.

## Parameters

- `reply`: The error that occurred. For a list of possible values, see  .

## See Also

- [func requestUserAttention(NSApplication.RequestUserAttentionType) -> Int](nsapplication/requestuserattention(_:).md)
  Starts a user attention request.
- [NSApplication.RequestUserAttentionType](nsapplication/requestuserattentiontype.md)
  These constants specify the level of severity of a user attention request and are used by [`cancelUserAttentionRequest(_:)`](nsapplication/canceluserattentionrequest(_:).md) and [`requestUserAttention(_:)`](nsapplication/requestuserattention(_:).md).
- [func cancelUserAttentionRequest(Int)](nsapplication/canceluserattentionrequest(_:).md)
  Cancels a previous user attention request.
- [NSApplication.DelegateReply](nsapplication/delegatereply.md)
  Constants that indicate whether a copy or print operation was successful, was canceled, or failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/reply(toopenorprint:))*