# RequestStatus

**Framework**: Account Data Transfer  
**Kind**: dictionary

An object that represents the status of a download request.

**Availability**:
- Account Data Transfer 1.0+

## Declaration

```swift
object RequestStatus
```

## Properties

- `jobStatus` (string): The status of the download request.
- `status` (string): `success` if the operation succeeded; `error` otherwise.
- `statusCheckDelay` (integer): The number of seconds to wait before re-requesting the status.

## See Also

- [Get one-time request status](get-one-time-request-status.md)
  Find the status of a one-time download request.
- [Get recurring request status](get-recurring-request-status.md)
  Get the status of an instance of a recurring download request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountdatatransfer/requeststatus)*