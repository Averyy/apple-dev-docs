# fileProvider

**Framework**: PushKit  
**Kind**: property  
**Role**: Type Property

A push type for file provider updates.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
static let fileProvider: PKPushType
```

```c
extern PKPushType const PKPushTypeFileProvider;
```

## Discussion

Use file provider notifications to update your File Provider extension’s content from your server. For more information, see [Tracking Your File Provider’s Changes](../../FileProvider/tracking-your-file-provider-s-changes.md).

## See Also

### Notification Types
- [static let complication: PKPushType](./complication.md)
  A push type for watchOS complications.
- [static let voIP: PKPushType](./voip.md)
  A push type for Voice-over-IP (VoIP) call invitations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushtype/fileprovider)*