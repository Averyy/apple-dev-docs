# GetVppAssetResponse

**Framework**: Device Management  
**Kind**: dictionary

The response with the asset.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object GetVppAssetResponse
```

## Properties

- `assets` ([VppAsset]): The list of assets managed by the provided `sToken`.
- `clientContext` (string): The value currently associated with the provided `sToken`. This field is only included in the response when a value has been set via the [`Client Configuration`](client-configuration.md) endpoint. See [`Protecting Your VPP Account`](protecting-your-vpp-account.md) for more information.
- `errorMessage` (string): The human-readable explanation of the error.
- `errorNumber` (int32): The numeric code of the error.
- `expirationMillis` (int64): The UNIX epoch timestamp, in milliseconds, when the account’s `sToken` or password expires (whichever is earlier).
- `location` (VppLocation): The location associated with the provided `sToken`. This field is only returned when a location token is used with an Apple School Manager account.
- `status` (int32): The status code for the response. Possible values are: `0` = Success. `-1` = Failure.
- `totalCount` (int32): The total number of assets that will be returned.
- `uId` (string): The unique library identifier. When querying records using multiple tokens that may share libraries, use the `uId` field to filter duplicates. In this way, you can avoid double counting records when duplicate tokens are uploaded by different content managers.

## See Also

- [object GetVppAssetRequest](getvppassetrequest.md)
  The request for an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/getvppassetresponse)*