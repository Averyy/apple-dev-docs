# PTChannelError.Code.transmissionNotAllowed

**Framework**: Push to Talk  
**Kind**: case  
**Role**: Case

A channel error that indicates the current transmission mode of the channel doesn’t allow the mode you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
case transmissionNotAllowed
```

```c
PTChannelErrorTransmissionNotAllowed
```

## See Also

### Error codes
- [PTChannelError.Code.unknown](./unknown.md)
  A channel error that indicates an unknown error.
- [PTChannelError.Code.appNotForeground](./appnotforeground.md)
  A channel error that indicates the operation failed because the app isn’t in the foreground.
- [PTChannelError.Code.channelNotFound](./channelnotfound.md)
  A channel error that indicates the system can’t perform the action because there’s no active channel with the UUID you specify.
- [PTChannelError.Code.channelLimitReached](./channellimitreached.md)
  A channel error that indicates you reached the maximum of one active channel at a time for the entire device.
- [PTChannelError.Code.callActive](./callactive.md)
  A channel error that indicates there’s an active call that prevents the channel action.
- [PTChannelError.Code.transmissionInProgress](./transmissioninprogress.md)
  A channel error that indicates a transmission is already in progress.
- [PTChannelError.Code.transmissionNotFound](./transmissionnotfound.md)
  A channel error that indicates there’s no transmission to stop.
- [PTChannelError.Code.deviceManagementRestriction](./devicemanagementrestriction.md)
  A channel error that indicates a device-management policy or profile forbids joining the channel.
- [PTChannelError.Code.screenTimeRestriction](./screentimerestriction.md)
  A channel error that indicates a Screen Time restriction prevents the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelerror-swift.struct/code/transmissionnotallowed)*