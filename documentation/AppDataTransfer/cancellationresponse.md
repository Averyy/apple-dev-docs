# CancellationResponse

**Framework**: App Data Transfer  
**Kind**: dictionary

An object that describes the outcome of canceling a download request.

**Availability**:
- App Data Transfer 1.0+

## Declaration

```swift
object CancellationResponse
```

## Properties

- `jobStatus` (string): The current status of the download request.
- `status` (string): The outcome of the cancellation operation.

## See Also

- [Cancel request](cancel-request.md)
  Tells the server to stop processing an active request.
- [object CancellationRequest](cancellationrequest.md)
  An object that identifies a one-time request, or an individual instance of a recurring request, to cancel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appdatatransfer/cancellationresponse)*