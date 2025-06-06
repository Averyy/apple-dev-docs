# ProtocolException

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

An exception response from a media service.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object ProtocolException
```

#### Discussion

You can define a mapping of exception `code` values that’s meaningful for your service. The client logs these exception codes.

The client doesn’t retry if the `retryWithDelay` value is negative or absent. If the value is greater than 5 seconds, the client may not retry so it can preserve the real-time interaction with the user.

Include the `methodName` and `methodIndex` whenever the reason is `unsupported`, `unauthorized`, `invalid`, or `busy`. For other reason values, these properties may help diagnose issues, but aren’t a requirement.

## See Also

- [object ProtocolExceptionInvocationResponse](protocolexceptioninvocationresponse.md)
  A response object that indicates when the service fails to process the client’s request.
- [type ProtocolExceptionReason](protocolexceptionreason.md)
  Categories of exceptions a service can encounter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/protocolexception)*