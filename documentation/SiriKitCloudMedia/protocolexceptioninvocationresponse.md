# ProtocolExceptionInvocationResponse

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

A response object that indicates when the service fails to process the client’s request.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object ProtocolExceptionInvocationResponse
```

#### Discussion

When your service receives a well-formed request, but it can’t fulfill the intent, use an [`IntentResponse`](./intentresponse.md) or [`IntentResolutionResult`](./intentresolutionresult.md) instead of a `ProtocolExceptionInvocationResponse`. Those objects allow the client to provide more specific information to the user about errors that occur.

## Properties

- `exception` (ProtocolException) *(required)*: The reason your service can’t provide a response.
- `method` (string) *(required)*: The action your service takes to process this intent.

  **Allowed Values**: `ProtocolException`

## Relationships

### Inherits From
- [InvocationResponse](./invocationresponse.md)

## See Also

### Exceptions
- [object ProtocolException](./protocolexception.md)
  An exception response from a media service.
- [type ProtocolExceptionReason](./protocolexceptionreason.md)
  Categories of exceptions a service can encounter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/protocolexceptioninvocationresponse)*