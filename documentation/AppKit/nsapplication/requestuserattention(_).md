# requestUserAttention(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Starts a user attention request.

**Availability**:
- macOS

## Declaration

```swift
func requestUserAttention(_ requestType: NSApplication.RequestUserAttentionType) -> Int
```

```objc
- (NSInteger) requestUserAttention:(NSRequestUserAttentionType) requestType;
```

#### Return Value

The identifier for the request. You can use this value to cancel the request later using the [`cancelUserAttentionRequest(_:)`](./canceluserattentionrequest%28_%29.md) method.

#### Discussion

Activating the app cancels the user attention request. A spoken notification will occur if spoken notifications are enabled. Sending [`requestUserAttention(_:)`](./requestuserattention%28_%29.md) to an app that is already active has no effect.

If the inactive app presents a modal panel, this method will be invoked with `NSCriticalRequest` automatically. The modal panel is not brought to the front for an inactive app.

## Parameters

- `requestType`: The severity of the request. For a list of possible values, see [`NSApplication.RequestUserAttentionType`](./requestuserattentiontype.md).

## See Also

### Managing user attention requests
- [NSApplication.RequestUserAttentionType](./requestuserattentiontype.md)
  These constants specify the level of severity of a user attention request and are used by [`cancelUserAttentionRequest(_:)`](./canceluserattentionrequest%28_%29.md) and [`requestUserAttention(_:)`](./requestuserattention%28_%29.md).
- [func cancelUserAttentionRequest(Int)](./canceluserattentionrequest%28_%29.md)
  Cancels a previous user attention request.
- [func reply(toOpenOrPrint: NSApplication.DelegateReply)](./reply%28toopenorprint%29.md)
  Handles errors that might occur when the user attempts to open or print files.
- [NSApplication.DelegateReply](./delegatereply.md)
  Constants that indicate whether a copy or print operation was successful, was canceled, or failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/requestuserattention(_:))*