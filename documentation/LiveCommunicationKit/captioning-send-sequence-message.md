# Send Sequence Message

**Framework**: LiveCommunicationKit  
**Role**: Article

Request the most recent sequence number from the FaceTime Web service.

## JSON

```json
    interface SequenceMessage {
      type: "msg";
    }
```

## Parameters

| Member | Type | Description |
| --- | --- | --- |
| `type` | String | The string `seq`. |

## Discussion

The captioning app sends this message immediately upon connecting to FaceTime Web. The response tells the app the sequence number to use when resuming after a reconnection.

Send the message as a JSON string, similar to the following:

```json
{
  "type": "seq"
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
- [Receive Sequence Message](./captioning-receive-sequence-message.md)
  Receive the most recent sequence number from the FaceTime Web service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/captioning-send-sequence-message)*