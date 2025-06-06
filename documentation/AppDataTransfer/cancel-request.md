# Cancel request

**Framework**: App Data Transfer  
**Kind**: httpRequest

Tells the server to stop processing an active request.

**Availability**:
- App Data Transfer 1.0+

#### Overview

A cancellation request only succeeds if the request is currently in progress.

##### Cancel a One Time Download

##### Cancel a Recurring Download

## Request Body

An object that identifies the request to cancel.

## See Also

- [object CancellationRequest](cancellationrequest.md)
  An object that identifies a one-time request, or an individual instance of a recurring request, to cancel.
- [object CancellationResponse](cancellationresponse.md)
  An object that describes the outcome of canceling a download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appdatatransfer/cancel-request)*