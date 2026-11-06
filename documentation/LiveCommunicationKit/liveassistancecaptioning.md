# Live assistance captioning

**Framework**: LiveCommunicationKit

Use a WebSocket API to perform real-time captioning in a FaceTime call.

## Overview

The [`LiveAssistanceExtension`](./liveassistanceextension.md) and [`LiveAssistance`](./liveassistance.md) APIs allow a participant in a FaceTime to invite an interpreter or captioner to the call. When someone requests captioning, your service can also use a WebSocket connection to deliver caption text to the call in real time.

## Topics

### Essentials
- [Providing captioning for a FaceTime call](./providing-captioning-for-a-facetime-call.md)
  Connect to FaceTime Web to provide real-time caption services.
### WebSocket messages
- [Send Caption Message](./captioning-caption-message.md)
  Send content and timing information for an individual caption.
- [Receive Success Message](./captioning-success-message.md)
  Receive confirmation that FaceTime Web delivered a caption message to the call.
- [Receive Error Message](./captioning-error-message.md)
  Receive notification that FaceTime Web couldn’t deliver a caption to the call.
- [Send Sequence Message](./captioning-send-sequence-message.md)
  Request the most recent sequence number from the FaceTime Web service.
- [Receive Sequence Message](./captioning-receive-sequence-message.md)
  Receive the most recent sequence number from the FaceTime Web service.

## See Also

### Conversation assistance
- [protocol LiveAssistanceExtension](./liveassistanceextension.md)
  The protocol you extend to provide live assistance services.
- [enum LiveAssistance](./liveassistance.md)
  A namespace to collect APIs for use by container apps that provide live assistance services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistancecaptioning)*