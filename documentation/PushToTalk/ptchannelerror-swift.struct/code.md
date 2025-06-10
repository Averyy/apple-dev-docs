# PTChannelError.Code

**Framework**: Push to Talk  
**Kind**: enum

Error codes for channel operations.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum Code
```

## Mentions

- [Creating a Push to Talk app](creating-a-push-to-talk-app.md)

## Topics

### Error codes
- [PTChannelError.Code.unknown](ptchannelerror-swift.struct/code/unknown.md)
  A channel error that indicates an unknown error.
- [PTChannelError.Code.appNotForeground](ptchannelerror-swift.struct/code/appnotforeground.md)
  A channel error that indicates the operation failed because the app isn’t in the foreground.
- [PTChannelError.Code.channelNotFound](ptchannelerror-swift.struct/code/channelnotfound.md)
  A channel error that indicates the system can’t perform the action because there’s no active channel with the UUID you specify.
- [PTChannelError.Code.channelLimitReached](ptchannelerror-swift.struct/code/channellimitreached.md)
  A channel error that indicates you reached the maximum of one active channel at a time for the entire device.
- [PTChannelError.Code.callActive](ptchannelerror-swift.struct/code/callactive.md)
  A channel error that indicates there’s an active call that prevents the channel action.
- [PTChannelError.Code.transmissionInProgress](ptchannelerror-swift.struct/code/transmissioninprogress.md)
  A channel error that indicates a transmission is already in progress.
- [PTChannelError.Code.transmissionNotFound](ptchannelerror-swift.struct/code/transmissionnotfound.md)
  A channel error that indicates there’s no transmission to stop.
- [PTChannelError.Code.deviceManagementRestriction](ptchannelerror-swift.struct/code/devicemanagementrestriction.md)
  A channel error that indicates a device-management policy or profile forbids joining the channel.
- [PTChannelError.Code.screenTimeRestriction](ptchannelerror-swift.struct/code/screentimerestriction.md)
  A channel error that indicates a Screen Time restriction prevents the action.
- [PTChannelError.Code.transmissionNotAllowed](ptchannelerror-swift.struct/code/transmissionnotallowed.md)
  A channel error that indicates the current transmission mode of the channel doesn’t allow the mode you specify.
### Initializers
- [init?(rawValue: Int)](ptchannelerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PTChannelError](ptchannelerror-swift.struct.md)
  A structure that represents a channel error.
- [struct PTInstantiationError](ptinstantiationerror-swift.struct.md)
  A structure that represents an instantiation error.
- [PTInstantiationError.Code](ptinstantiationerror-swift.struct/code.md)
  Error codes for instantiation operations.
- [let PTChannelErrorDomain: String](ptchannelerrordomain.md)
  A string representation of the channel error domain.
- [let PTInstantiationErrorDomain: String](ptinstantiationerrordomain.md)
  A string representation of the instantiation error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelerror-swift.struct/code)*