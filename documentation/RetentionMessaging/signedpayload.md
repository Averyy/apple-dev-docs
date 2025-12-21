# signedPayload

**Framework**: Retention Messaging API  
**Kind**: typealias

The payload in a JSON Web Signature (JWS) format, signed by the App Store.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
string signedPayload
```

## Mentions

- [Responding to real-time retention messaging requests](responding-to-realtime-retention-messaging-requests.md)

#### Discussion

The signed payload is a property of [`RealtimeRequestBody`](realtimerequestbody.md). The App Store server sends this request to your `Get Retention Message` endpoint.

For information about parsing the signed payload and validating the signature, see [`Responding to real-time retention messaging requests`](responding-to-realtime-retention-messaging-requests.md).

## See Also

- [type originalTransactionId](originaltransactionid.md)
  The original transaction identifier of an In-App Purchase.
- [type appAppleId](appappleid.md)
  The unique identifier of an app in the App Store.
- [type requestIdentifier](requestidentifier.md)
  A unique identifier the App Store server creates for its requests.
- [type signedDate](signeddate.md)
  The UNIX time, in milliseconds, that the App Store signed the JSON Web Signature data.
- [type environment](environment.md)
  The server environment, either sandbox or production.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/signedpayload)*