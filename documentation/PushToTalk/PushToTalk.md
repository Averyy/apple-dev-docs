# Push to Talk

**Framework**: Pushtotalk  
**Kind**: module

Display the system user interface for your app’s Push to Talk services.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

#### Overview

The Push to Talk framework is a power-efficient, user-friendly, and privacy-focused API. It gives your apps the ability to provide user interface controls that allow your users to transmit audio from anywhere. It supplies an ephemeral Apple Push Notification service token so the system can wake your app in the background to handle incoming audio while a session is ongoing.

> **Note**:  Push to Talk services aren’t available to compatible iPad and iPhone apps running in visionOS.

## Topics

### Essentials
- [Creating a Push to Talk app](creating-a-push-to-talk-app.md)
  Build a walkie-talkie style app with system user interface controls.
- [class PTChannelManager](ptchannelmanager.md)
  An object that represents a push-to-talk channel manager.
### Channel management
- [protocol PTChannelManagerDelegate](ptchannelmanagerdelegate.md)
  A type that represents your life cycle of a channel manager.
- [enum PTTransmissionMode](pttransmissionmode.md)
  Identifies the type of audio transmission modes.
- [enum PTServiceStatus](ptservicestatus.md)
  Identifies the type that indicates the status of the service.
- [enum PTChannelJoinReason](ptchanneljoinreason.md)
  Identifies the type that indicates the join reason.
- [enum PTChannelLeaveReason](ptchannelleavereason.md)
  Identifies the type that indicates the leave reason.
- [enum PTChannelTransmitRequestSource](ptchanneltransmitrequestsource.md)
  Identifies the type that indicates the transmission request source.
### Channel restoration
- [class PTChannelDescriptor](ptchanneldescriptor.md)
  An object that describes a channel.
- [protocol PTChannelRestorationDelegate](ptchannelrestorationdelegate.md)
  A type that represents the channel restoration behavior.
### Channel participants
- [class PTParticipant](ptparticipant.md)
  An object that represents a participant.
### Push notification results
- [class PTPushResult](ptpushresult.md)
  An object that represents a push result.
### Push to Talk errors
- [struct PTChannelError](ptchannelerror-swift.struct.md)
  A structure that represents a channel error.
- [PTChannelError.Code](ptchannelerror-swift.struct/code.md)
  Error codes for channel operations.
- [struct PTInstantiationError](ptinstantiationerror-swift.struct.md)
  A structure that represents an instantiation error.
- [PTInstantiationError.Code](ptinstantiationerror-swift.struct/code.md)
  Error codes for instantiation operations.
- [let PTChannelErrorDomain: String](ptchannelerrordomain.md)
  A string representation of the channel error domain.
- [let PTInstantiationErrorDomain: String](ptinstantiationerrordomain.md)
  A string representation of the instantiation error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/PushToTalk)*