# Error constants

**Framework**: Push to Talk

Error codes for channel operations.

## Topics

### Constants
- [static var unknown: PTChannelError.Code](ptchannelerror-swift.struct/unknown.md)
  A channel error that indicates an unknown error.
- [static var appNotForeground: PTChannelError.Code](ptchannelerror-swift.struct/appnotforeground.md)
  A channel error that indicates the operation failed because the app isn’t in the foreground.
- [static var channelNotFound: PTChannelError.Code](ptchannelerror-swift.struct/channelnotfound.md)
  A channel error that indicates the system can’t perform the action because there’s no active channel with the UUID you specify.
- [static var channelLimitReached: PTChannelError.Code](ptchannelerror-swift.struct/channellimitreached.md)
  A channel error that indicates you reached the maximum of one active channel at a time for the entire device.
- [static var callActive: PTChannelError.Code](ptchannelerror-swift.struct/callactive.md)
  A channel error that indicates there’s an active call that prevents the channel action.
- [static var transmissionInProgress: PTChannelError.Code](ptchannelerror-swift.struct/transmissioninprogress.md)
  A channel error that indicates a transmission is already in progress.
- [static var transmissionNotFound: PTChannelError.Code](ptchannelerror-swift.struct/transmissionnotfound.md)
  A channel error that indicates there’s no transmission to stop.
- [static var deviceManagementRestriction: PTChannelError.Code](ptchannelerror-swift.struct/devicemanagementrestriction.md)
  A channel error that indicates a device-management policy or profile forbids joining the channel.
- [static var screenTimeRestriction: PTChannelError.Code](ptchannelerror-swift.struct/screentimerestriction.md)
  A channel error that indicates a Screen Time restriction prevents the action.
- [static var transmissionNotAllowed: PTChannelError.Code](ptchannelerror-swift.struct/transmissionnotallowed.md)
  A channel error that indicates the current transmission mode of the channel doesn’t allow the mode you specify.

## See Also

- [PTChannelError.Code](ptchannelerror-swift.struct/code.md)
  Error codes for channel operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelerror-error-constants)*