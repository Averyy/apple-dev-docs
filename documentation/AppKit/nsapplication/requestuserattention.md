# requestUserAttention(_:)

**Framework**: AppKit  
**Kind**: method

Starts a user attention request.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func requestUserAttention(_ requestType: NSApplication.RequestUserAttentionType) -> Int
```

#### Return Value

The identifier for the request. You can use this value to cancel the request later using the [`cancelUserAttentionRequest(_:)`](nsapplication/canceluserattentionrequest(_:).md) method.

#### Discussion

Activating the app cancels the user attention request. A spoken notification will occur if spoken notifications are enabled. Sending [`requestUserAttention(_:)`](nsapplication/requestuserattention(_:).md) to an app that is already active has no effect.

If the inactive app presents a modal panel, this method will be invoked with `NSCriticalRequest` automatically. The modal panel is not brought to the front for an inactive app.

## Parameters

- `requestType`: The severity of the request. For a list of possible values, see  .

## See Also

- [NSApplication.RequestUserAttentionType](nsapplication/requestuserattentiontype.md)
  These constants specify the level of severity of a user attention request and are used by [`cancelUserAttentionRequest(_:)`](nsapplication/canceluserattentionrequest(_:).md) and [`requestUserAttention(_:)`](nsapplication/requestuserattention(_:).md).
- [func cancelUserAttentionRequest(Int)](nsapplication/canceluserattentionrequest(_:).md)
  Cancels a previous user attention request.
- [func reply(toOpenOrPrint: NSApplication.DelegateReply)](nsapplication/reply(toopenorprint:).md)
  Handles errors that might occur when the user attempts to open or print files.
- [NSApplication.DelegateReply](nsapplication/delegatereply.md)
  Constants that indicate whether a copy or print operation was successful, was canceled, or failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/requestuserattention(_:))*