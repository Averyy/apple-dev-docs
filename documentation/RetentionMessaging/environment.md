# environment

**Framework**: Retention Messaging API  
**Kind**: typealias  
**Role**: Type

The server environment, either sandbox or production.

**Availability**:
- Retention Messaging API 1.1+

## Declaration

```
string environment
```

## Possible Values

- `Sandbox`: Indicates that the request applies to testing in the sandbox environment.
- `Production`: Indicates that the request applies to the production environment.

## Mentions

- [Retention Messaging API changelog](./retention-messaging-changelog.md)

## See Also

### Real-time request body
- [type signedPayload](./signedpayload.md)
  The payload in a JSON Web Signature (JWS) format, signed by the App Store.
- [type originalTransactionId](./originaltransactionid.md)
  The original transaction identifier of an In-App Purchase.
- [type appAppleId](./appappleid.md)
  The unique identifier of an app in the App Store.
- [type requestIdentifier](./requestidentifier.md)
  A unique identifier the App Store server creates for its requests.
- [type signedDate](./signeddate.md)
  The UNIX time, in milliseconds, that the App Store signed the JSON Web Signature data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/environment)*