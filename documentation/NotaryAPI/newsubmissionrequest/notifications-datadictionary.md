# NewSubmissionRequest.Notifications

**Framework**: Notary API  
**Kind**: dictionary

A notification that the notary service sends you when notarization finishes.

**Availability**:
- Notary API 2.0.0+

## Declaration

```swift
object NewSubmissionRequest.Notifications
```

## Mentions

- [Submitting software for notarization over the web](submitting-software-for-notarization-over-the-web.md)

#### Discussion

If you want a notification when notarization completes, include a data structure of this type in the `notifications` array that’s part of the body when you post to the [`Submit Software`](submit-software.md) endpoint. Set the value for the `channel` key to `webhook`, and provide a URL as the value for the `target` key. The service indicates when notarization finishes by posting a body to the URL like this:

```javascript
{
  "payload": "{\"completed_time\":\"2022-06-08T22:04:00.886Z\",\"event\":\"processing-complete\",\"start_time\":\"2022-06-08T22:03:42.801Z\",\"submission_id\":\"c00fe84b-95f2-4890-b7ea-019a7f546abd\",\"team_id\":\"JA62H4Q78D\"}",
  "signature": "MEUCIEqr...",
  "cert_chain": "LS0tLS1CR..."
}

```

The value for the `payload` key indicates when the operation starts and completes, as well as the submission ID and your Team ID. The submission ID matches the value that you receive in response to the [`Submit Software`](submit-software.md) call. You can use the `signature` and `cert_chain` fields to verify the authenticity of the message against the Apple Inc. Root certificate that you can download from the [`Apple PKI`](https://developer.apple.comhttps://www.apple.com/certificateauthority/) site. If you need the certificate repeatedly, store a copy of the certificate on your server rather than downloading it every time you need it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/newsubmissionrequest/notifications-data.dictionary)*