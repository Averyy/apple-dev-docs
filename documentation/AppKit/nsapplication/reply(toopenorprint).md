# reply(toOpenOrPrint:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Handles errors that might occur when the user attempts to open or print files.

**Availability**:
- macOS

## Declaration

```swift
func reply(toOpenOrPrint reply: NSApplication.DelegateReply)
```

```objc
- (void) replyToOpenOrPrint:(NSApplicationDelegateReply) reply;
```

#### Discussion

Delegates should invoke this method if an error is encountered in the [`application(_:openFiles:)`](../nsapplicationdelegate/application%28_,openfiles%29.md) or [`application(_:printFiles:withSettings:showPrintPanels:)`](../nsapplicationdelegate/application%28_,printfiles,withsettings,showprintpanels%29.md) delegate methods.

## Parameters

- `reply`: The error that occurred. For a list of possible values, see [`NSApplication.DelegateReply`](./delegatereply.md).

## See Also

### Managing user attention requests
- [func requestUserAttention(NSApplication.RequestUserAttentionType) -> Int](./requestuserattention%28_%29.md)
  Starts a user attention request.
- [NSApplication.RequestUserAttentionType](./requestuserattentiontype.md)
  These constants specify the level of severity of a user attention request and are used by [`cancelUserAttentionRequest(_:)`](./canceluserattentionrequest%28_%29.md) and [`requestUserAttention(_:)`](./requestuserattention%28_%29.md).
- [func cancelUserAttentionRequest(Int)](./canceluserattentionrequest%28_%29.md)
  Cancels a previous user attention request.
- [NSApplication.DelegateReply](./delegatereply.md)
  Constants that indicate whether a copy or print operation was successful, was canceled, or failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/reply(toopenorprint:))*