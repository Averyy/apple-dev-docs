# cancelUserAttentionRequest(_:)

**Framework**: AppKit  
**Kind**: method

Cancels a previous user attention request.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func cancelUserAttentionRequest(_ request: Int)
```

#### Discussion

A request is also canceled automatically by user activation of the app.

## Parameters

- `request`: The request identifier returned by the   method.

## See Also

- [func requestUserAttention(NSApplication.RequestUserAttentionType) -> Int](nsapplication/requestuserattention(_:).md)
  Starts a user attention request.
- [NSApplication.RequestUserAttentionType](nsapplication/requestuserattentiontype.md)
  These constants specify the level of severity of a user attention request and are used by [`cancelUserAttentionRequest(_:)`](nsapplication/canceluserattentionrequest(_:).md) and [`requestUserAttention(_:)`](nsapplication/requestuserattention(_:).md).
- [func reply(toOpenOrPrint: NSApplication.DelegateReply)](nsapplication/reply(toopenorprint:).md)
  Handles errors that might occur when the user attempts to open or print files.
- [NSApplication.DelegateReply](nsapplication/delegatereply.md)
  Constants that indicate whether a copy or print operation was successful, was canceled, or failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/canceluserattentionrequest(_:))*