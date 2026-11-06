# Receive Sequence Message

**Framework**: LiveCommunicationKit  
**Role**: Article

Receive the most recent sequence number from the FaceTime Web service.

## JSON

```json
    interface SequenceMessage {
      type: "msg";
      seq: number;
    }
```

## Parameters

| Member | Type | Description |
| --- | --- | --- |
| `type` | String | The string `seq`. |
| `seq` | Number | The `seq` of the last `CaptionMessage` FaceTime Web forwarded to the call, or `0` if it hasn’t forwarded one. |

## Discussion

FaceTime Web sends this message to the captioning app in response to a request for the last sequence number. The value of `seq` represents the sequence number used by the most recent `CaptionMessage` that FaceTime Web successfully forwarded to the call.

Handle the message as a JSON string, similar to the following:

```json
    {
      "type": "seq",
      "seq": 42
    }
```

## See Also

### WebSocket messages
- [Send Caption Message](./captioning-caption-message.md)
  Send content and timing information for an individual caption.
- [Receive Success Message](./captioning-success-message.md)
  Receive confirmation that FaceTime Web delivered a caption message to the call.
- [Receive Error Message](./captioning-error-message.md)
  Receive notification that FaceTime Web couldn’t deliver a caption to the call.
- [Send Sequence Message](./captioning-send-sequence-message.md)
  Request the most recent sequence number from the FaceTime Web service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/captioning-receive-sequence-message)*