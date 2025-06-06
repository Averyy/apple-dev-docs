# NSApplication.DelegateReply

**Framework**: AppKit  
**Kind**: enum

Constants that indicate whether a copy or print operation was successful, was canceled, or failed.

**Availability**:
- macOS ?+

## Declaration

```swift
enum DelegateReply
```

#### Overview

These constants are used by the [`reply(toOpenOrPrint:)`](nsapplication/reply(toopenorprint:).md) method.

## Topics

### Constants
- [NSApplication.DelegateReply.success](nsapplication/delegatereply/success.md)
  Indicates the operation succeeded.
- [NSApplication.DelegateReply.cancel](nsapplication/delegatereply/cancel.md)
  Indicates the user cancelled the operation.
- [NSApplication.DelegateReply.failure](nsapplication/delegatereply/failure.md)
  Indicates an error occurred processing the operation.
### Initializers
- [init?(rawValue: UInt)](nsapplication/delegatereply/init(rawvalue:).md)

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
- [NSApplication.RequestUserAttentionType](nsapplication/requestuserattentiontype.md)
  These constants specify the level of severity of a user attention request and are used by [`cancelUserAttentionRequest(_:)`](nsapplication/canceluserattentionrequest(_:).md) and [`requestUserAttention(_:)`](nsapplication/requestuserattention(_:).md).
- [func cancelUserAttentionRequest(Int)](nsapplication/canceluserattentionrequest(_:).md)
  Cancels a previous user attention request.
- [func reply(toOpenOrPrint: NSApplication.DelegateReply)](nsapplication/reply(toopenorprint:).md)
  Handles errors that might occur when the user attempts to open or print files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/delegatereply)*