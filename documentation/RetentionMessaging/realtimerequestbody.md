# RealtimeRequestBody

**Framework**: Retention Messaging API  
**Kind**: dictionary

The request body the App Store server sends to your Get Retention Message endpoint.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
object RealtimeRequestBody
```

## Mentions

- [Responding to real-time retention messaging requests](responding-to-realtime-retention-messaging-requests.md)
- [Setting up your Get Retention Message endpoint](setting-up-retention-messaging-endpoint.md)

#### Discussion

This is the request body for the `Get Retention Message` endpoint, which you can implement to choose retention messages for customers in real time. For more information about the endpoint, see [`Setting up your Get Retention Message endpoint`](setting-up-retention-messaging-endpoint.md).

The `signedPayload` is a string of three Base64URL-encoded components separated by a period. The string contains the JWS Compact Serialization of the real-time request, signed by the App Store according to the JSON Web Signature (JWS) [`IETF RFC 7515`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7515) specification.

The three components of the string are a header, a payload, and a signature, in that order.

- To read the real-time request information, Base64URL-decode the payload. Use a [`DecodedRealtimeRequestBody`](decodedrealtimerequestbody.md) object to read the payload information.
- To read the header, decode it and use a [`JWSDecodedHeader`](jwsdecodedheader.md) object to access the information. Use the information in the header to verify the signature.

## See Also

- [Setting up your Get Retention Message endpoint](setting-up-retention-messaging-endpoint.md)
  Choose retention messages for customers in real time by implementing an endpoint on your server that responds to requests from the App Store server.
- [Responding to real-time retention messaging requests](responding-to-realtime-retention-messaging-requests.md)
  Select retention messages for customers in real time by responding to requests on your Get Retention Message endpoint.
- [object DecodedRealtimeRequestBody](decodedrealtimerequestbody.md)
  The decoded request body the App Store sends to your server to request a real-time retention message.
- [object RealtimeResponseBody](realtimeresponsebody.md)
  A response you provide to choose, in real time, a retention message the system displays to the customer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/realtimerequestbody)*