# cancelUserAttentionRequest(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Cancels a previous user attention request.

**Availability**:
- macOS

## Declaration

```swift
func cancelUserAttentionRequest(_ request: Int)
```

```objc
- (void) cancelUserAttentionRequest:(NSInteger) request;
```

## Discussion

A request is also canceled automatically by user activation of the app.

## Parameters

- `request`: The request identifier returned by the [`requestUserAttention(_:)`](./requestuserattention%28_%29.md) method.

## See Also

### Managing user attention requests
- [func requestUserAttention(NSApplication.RequestUserAttentionType) -> Int](./requestuserattention%28_%29.md)
  Starts a user attention request.
- [NSApplication.RequestUserAttentionType](./requestuserattentiontype.md)
  These constants specify the level of severity of a user attention request and are used by [`cancelUserAttentionRequest(_:)`](./canceluserattentionrequest%28_%29.md) and [`requestUserAttention(_:)`](./requestuserattention%28_%29.md).
- [func reply(toOpenOrPrint: NSApplication.DelegateReply)](./reply%28toopenorprint%29.md)
  Handles errors that might occur when the user attempts to open or print files.
- [NSApplication.DelegateReply](./delegatereply.md)
  Constants that indicate whether a copy or print operation was successful, was canceled, or failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/canceluserattentionrequest(_:))*