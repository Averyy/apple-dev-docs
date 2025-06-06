# NSApplication.RequestUserAttentionType

**Framework**: AppKit  
**Kind**: enum

These constants specify the level of severity of a user attention request and are used by [`cancelUserAttentionRequest(_:)`](nsapplication/canceluserattentionrequest(_:).md) and [`requestUserAttention(_:)`](nsapplication/requestuserattention(_:).md).

**Availability**:
- macOS ?+

## Declaration

```swift
enum RequestUserAttentionType
```

## Topics

### Constants
- [NSApplication.RequestUserAttentionType.criticalRequest](nsapplication/requestuserattentiontype/criticalrequest.md)
  The user attention request is a critical request.
- [NSApplication.RequestUserAttentionType.informationalRequest](nsapplication/requestuserattentiontype/informationalrequest.md)
  The user attention request is an informational request.
### Initializers
- [init?(rawValue: UInt)](nsapplication/requestuserattentiontype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func requestUserAttention(NSApplication.RequestUserAttentionType) -> Int](nsapplication/requestuserattention(_:).md)
  Starts a user attention request.
- [func cancelUserAttentionRequest(Int)](nsapplication/canceluserattentionrequest(_:).md)
  Cancels a previous user attention request.
- [func reply(toOpenOrPrint: NSApplication.DelegateReply)](nsapplication/reply(toopenorprint:).md)
  Handles errors that might occur when the user attempts to open or print files.
- [NSApplication.DelegateReply](nsapplication/delegatereply.md)
  Constants that indicate whether a copy or print operation was successful, was canceled, or failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/requestuserattentiontype)*