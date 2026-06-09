# RetireVppUserResponse

**Framework**: Device Management  
**Kind**: dictionary

The response from retiring a user.

**Availability**:
- VPP License Management 1.0+

## Declaration

```swift
object RetireVppUserResponse
```

#### Discussion

> **Note**:  If the user passes the `userId` value for an already-retired user, this request returns an error that indicates the user was already retired.

## Properties

- `clientContext` (string): The value currently associated with the provided `sToken`. This field is only included in the response when a value is set with the [`Client Configuration`](client-configuration.md) endpoint.
- `errorMessage` (string): The human-readable explanation of the error.
- `errorNumber` (int32): The numeric code of the error.
- `expirationMillis` (int64): The UNIX epoch timestamp, in milliseconds, when the account’s `sToken` or password expires (whichever is earlier).
- `location` (VppLocation): The location associated with the provided sToken. This field is only returned when a location token is used with an Apple School Manager account.
- `status` (int32): The status code for the response. Possible values are: `0` = Success. `-1` = Failure.
- `uId` (string): The unique library identifier. When querying records using multiple tokens that may share libraries, use the `uId` field to filter duplicates. In this way, you can avoid double-counting records when duplicate tokens are uploaded by different content managers.
- `user` (VppUser): The retired user.

## See Also

- [object RetireVppUserRequest](retirevppuserrequest.md)
  The request to retire a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/retirevppuserresponse)*