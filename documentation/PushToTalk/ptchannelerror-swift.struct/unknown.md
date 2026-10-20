# unknown

**Framework**: Push to Talk  
**Kind**: property  
**Role**: Type Property

A channel error that indicates an unknown error.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
static var unknown: PTChannelError.Code { get }
```

## See Also

### Constants
- [static var appNotForeground: PTChannelError.Code](./appnotforeground.md)
  A channel error that indicates the operation failed because the app isn’t in the foreground.
- [static var channelNotFound: PTChannelError.Code](./channelnotfound.md)
  A channel error that indicates the system can’t perform the action because there’s no active channel with the UUID you specify.
- [static var channelLimitReached: PTChannelError.Code](./channellimitreached.md)
  A channel error that indicates you reached the maximum of one active channel at a time for the entire device.
- [static var callActive: PTChannelError.Code](./callactive.md)
  A channel error that indicates there’s an active call that prevents the channel action.
- [static var transmissionInProgress: PTChannelError.Code](./transmissioninprogress.md)
  A channel error that indicates a transmission is already in progress.
- [static var transmissionNotFound: PTChannelError.Code](./transmissionnotfound.md)
  A channel error that indicates there’s no transmission to stop.
- [static var deviceManagementRestriction: PTChannelError.Code](./devicemanagementrestriction.md)
  A channel error that indicates a device-management policy or profile forbids joining the channel.
- [static var screenTimeRestriction: PTChannelError.Code](./screentimerestriction.md)
  A channel error that indicates a Screen Time restriction prevents the action.
- [static var transmissionNotAllowed: PTChannelError.Code](./transmissionnotallowed.md)
  A channel error that indicates the current transmission mode of the channel doesn’t allow the mode you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelerror-swift.struct/unknown)*