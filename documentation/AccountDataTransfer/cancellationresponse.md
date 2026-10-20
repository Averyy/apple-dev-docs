# CancellationResponse

**Framework**: Account Data Transfer  
**Kind**: dictionary  
**Role**: Object

An object that describes the outcome of canceling a download request.

**Availability**:
- Account Data Transfer 1.0+

## Declaration

```
object CancellationResponse
```

## Properties

- `jobStatus` (string): The current status of the download request.

  **Allowed Values**: `cancelled`
- `status` (string): The outcome of the cancellation operation.

  **Allowed Values**: `success`, `error`

## See Also

### Cancellation
- [Cancel request](./cancel-request.md)
  Tells the server to stop processing an active request.
- [object CancellationRequest](./cancellationrequest.md)
  An object that identifies a one-time request, or an individual instance of a recurring request, to cancel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountdatatransfer/cancellationresponse)*