# requestIdentifier

**Framework**: Retention Messaging API  
**Kind**: typealias

A unique identifier the App Store server creates for its requests.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
uuid requestIdentifier
```

#### Discussion

The request identifier uniquely identifies each request the App Store server sends to your server’s `Get Retention Message` endpoint. For more information, see [`DecodedRealtimeRequestBody`](decodedrealtimerequestbody.md).

## See Also

- [type signedPayload](signedpayload.md)
  The payload in a JSON Web Signature (JWS) format, signed by the App Store.
- [type originalTransactionId](originaltransactionid.md)
  The original transaction identifier of an In-App Purchase.
- [type appAppleId](appappleid.md)
  The unique identifier of an app in the App Store.
- [type signedDate](signeddate.md)
  The UNIX time, in milliseconds, that the App Store signed the JSON Web Signature data.
- [type environment](environment.md)
  The server environment, either sandbox or production.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/requestidentifier)*