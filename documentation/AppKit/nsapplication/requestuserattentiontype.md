# NSApplication.RequestUserAttentionType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

These constants specify the level of severity of a user attention request and are used by [`cancelUserAttentionRequest(_:)`](./canceluserattentionrequest%28_%29.md) and [`requestUserAttention(_:)`](./requestuserattention%28_%29.md).

**Availability**:
- macOS

## Declaration

```swift
enum RequestUserAttentionType
```

```c
enum NSRequestUserAttentionType : NSUInteger;
```

## Topics

### Constants
- [NSApplication.RequestUserAttentionType.criticalRequest](./requestuserattentiontype/criticalrequest.md)
  The user attention request is a critical request.
- [NSApplication.RequestUserAttentionType.informationalRequest](./requestuserattentiontype/informationalrequest.md)
  The user attention request is an informational request.
### Initializers
- [init?(rawValue: UInt)](./requestuserattentiontype/init%28rawvalue%29.md)

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
- [func cancelUserAttentionRequest(Int)](./canceluserattentionrequest%28_%29.md)
  Cancels a previous user attention request.
- [func reply(toOpenOrPrint: NSApplication.DelegateReply)](./reply%28toopenorprint%29.md)
  Handles errors that might occur when the user attempts to open or print files.
- [NSApplication.DelegateReply](./delegatereply.md)
  Constants that indicate whether a copy or print operation was successful, was canceled, or failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/requestuserattentiontype)*