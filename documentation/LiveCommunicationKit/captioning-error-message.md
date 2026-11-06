# Receive Error Message

**Framework**: LiveCommunicationKit  
**Role**: Article

Receive notification that FaceTime Web couldn’t deliver a caption to the call.

## JSON

```json
    interface ErrorMessage {
      type: "error";
      error: string;
      description: string;
      seq: number;
    }
```

## Parameters

| Member | Type | Description |
| --- | --- | --- |
| `type` | String | The string `error`. |
| `error` | String | A string that identifies the error. |
| `description` | String | An optional description of the error. |
| `seq` | Number | A unique sequence number, as provided by the original `CaptionMessage` that this `ErrorMessage` corresponds to. |

## Error field values

| Error value | Meaning |
| --- | --- |
| `invalid_request` | The message format is invalid. |
| `rate_limited` | The submission of caption requests exceeded the rate limit. Receiving this error means the caption message with the corresponding sequence number wasn’t forwarded to the FaceTime call. |
| `nocall` | The local participant hasn’t joined the call, or the call already ended. The captioning app can try again. This isn’t a signal to the captioning app that the call is over; the WebSocket closing is the signal to stop. |
| `unknown` | An error occurred within FaceTime Web. |

## Discussion

FaceTime Web sends this message to the captioning app to indicate it failed to handle a captioning message. Use the `error` field to determine the cause of the error.

Keep track of the sequence number indicated by `seq` and increment it for the next caption message your app sends.

```json
{
  "type": "error",
  "error": "INVALID_REQUEST",
  "description": "The request format is invalid",
  "seq": 2
}
```

## See Also

### WebSocket messages
- [Send Caption Message](./captioning-caption-message.md)
  Send content and timing information for an individual caption.
- [Receive Success Message](./captioning-success-message.md)
  Receive confirmation that FaceTime Web delivered a caption message to the call.
- [Send Sequence Message](./captioning-send-sequence-message.md)
  Request the most recent sequence number from the FaceTime Web service.
- [Receive Sequence Message](./captioning-receive-sequence-message.md)
  Receive the most recent sequence number from the FaceTime Web service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/captioning-error-message)*