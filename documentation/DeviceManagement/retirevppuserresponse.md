# RetireVppUserResponse

**Framework**: Device Management  
**Kind**: dictionary

The response from retiring a user.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RetireVppUserResponse
```

#### Discussion

> **Note**:  If the user passes the `userId` value for an already-retired user, this request returns an error that indicates the user has already been retired.

## Properties

- `clientContext` (string): The value currently associated with the provided sToken. This field is only included in the response when a value has been set via the [`Client Configuration`](client-configuration.md) endpoint. See [`Protecting Your VPP Account`](protecting-your-vpp-account.md) for more information.
- `errorMessage` (string): The human-readable explanation of the error.
- `errorNumber` (int32): The numeric code of the error.
- `expirationMillis` (int64): The UNIX epoch timestamp, in milliseconds, when the account’s sToken or password expires (whichever is earlier).
- `location` (VppLocation): The location associated with the provided sToken. This field is only returned when a location token is used with an Apple School Manager account.
- `status` (int32): The status code for the response. Possible values are: `0` = Success. `-1` = Failure.
- `uId` (string): The unique library identifier. When querying records using multiple tokens that may share libraries, use the `uId` field to filter duplicates. In this way, you can avoid double-counting records when duplicate tokens are uploaded by different content managers.
- `user` (VppUser): The retired user.

## See Also

- [object RetireVppUserRequest](retirevppuserrequest.md)
  The request to retire a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/retirevppuserresponse)*