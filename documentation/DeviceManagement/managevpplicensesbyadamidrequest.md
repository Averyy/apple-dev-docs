# ManageVppLicensesByAdamIdRequest

**Framework**: Device Management  
**Kind**: dictionary

The request to manage licenses.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ManageVppLicensesByAdamIdRequest
```

#### Discussion

The maximum number of entries allowed in the `associate*` and `disassociate*` arrays are indicated by the `maxBatchAssociateLicenseCount` or `maxBatchDisassociateLicenseCount` fields available from the [`Service Configuration`](service-configuration.md) response.

Requests that exceed the current limits are rejected with the error code 9602 “Invalid Argument” and no work is done. If you receive this error code, query the [`Service Configuration`](service-configuration.md) endpoint to retrieve new `maxBatchAssociateLicenseCount` and `maxBatchDisassociateLicenseCount` values, correct the last request that was rejected, and resend the request.

## See Also

- [object ManageVppLicensesByAdamIdResponse](managevpplicensesbyadamidresponse.md)
  The response from managing licenses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managevpplicensesbyadamidrequest)*