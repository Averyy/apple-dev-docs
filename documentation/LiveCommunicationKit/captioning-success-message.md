# Receive Success Message

**Framework**: LiveCommunicationKit  
**Role**: Article

Receive confirmation that FaceTime Web delivered a caption message to the call.

## JSON

```json
    interface SuccessMessage {
      type: "success";
      seq: number;
      timestamp: string;
    }```
```

## Parameters

| Member | Type | Description |
| --- | --- | --- |
| `type` | String | The string `success`. |
| `timestamp` | String | An ISO-8601 timestamp. |
| `seq` | Number | A unique sequence number, as provided by the original `CaptionMessage` that this `SuccessMessage` corresponds to. |

## Discussion

FaceTime Web sends this message to the captioning app to indicate successful handling of a sent captioning message. Receiving this message indicates that FaceTime Web successfully forwarded the caption indicated by the sequence number.

Keep track of the sequence number indicated by `seq` and increment it for the next caption message your app sends.

```json
{
  "type": "success",
  "seq": 3
  "timestamp": "2026-02-02T20:41:49.116Z",
}
```

## See Also

### WebSocket messages
- [Send Caption Message](./captioning-caption-message.md)
  Send content and timing information for an individual caption.
- [Receive Error Message](./captioning-error-message.md)
  Receive notification that FaceTime Web couldn’t deliver a caption to the call.
- [Send Sequence Message](./captioning-send-sequence-message.md)
  Request the most recent sequence number from the FaceTime Web service.
- [Receive Sequence Message](./captioning-receive-sequence-message.md)
  Receive the most recent sequence number from the FaceTime Web service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/captioning-success-message)*