# NSApplication.DelegateReply

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate whether a copy or print operation was successful, was canceled, or failed.

**Availability**:
- macOS

## Declaration

```swift
enum DelegateReply
```

```c
enum NSApplicationDelegateReply : NSUInteger;
```

#### Overview

These constants are used by the [`reply(toOpenOrPrint:)`](./reply%28toopenorprint%29.md) method.

## Topics

### Constants
- [NSApplication.DelegateReply.success](./delegatereply/success.md)
  Indicates the operation succeeded.
- [NSApplication.DelegateReply.cancel](./delegatereply/cancel.md)
  Indicates the user cancelled the operation.
- [NSApplication.DelegateReply.failure](./delegatereply/failure.md)
  Indicates an error occurred processing the operation.
### Initializers
- [init?(rawValue: UInt)](./delegatereply/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing user attention requests
- [func requestUserAttention(NSApplication.RequestUserAttentionType) -> Int](./requestuserattention%28_%29.md)
  Starts a user attention request.
- [NSApplication.RequestUserAttentionType](./requestuserattentiontype.md)
  These constants specify the level of severity of a user attention request and are used by [`cancelUserAttentionRequest(_:)`](./canceluserattentionrequest%28_%29.md) and [`requestUserAttention(_:)`](./requestuserattention%28_%29.md).
- [func cancelUserAttentionRequest(Int)](./canceluserattentionrequest%28_%29.md)
  Cancels a previous user attention request.
- [func reply(toOpenOrPrint: NSApplication.DelegateReply)](./reply%28toopenorprint%29.md)
  Handles errors that might occur when the user attempts to open or print files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/delegatereply)*