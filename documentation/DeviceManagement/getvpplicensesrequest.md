# GetVppLicensesRequest

**Framework**: Device Management  
**Kind**: dictionary

The request for licenses.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object GetVppLicensesRequest
```

#### Discussion

The `batchToken` and `sinceModifiedToken` encode whether `adamId` and `pricingParam` were originally passed; therefore, if the `batchToken` or `sinceModifiedToken` is present on the request, the `adamId` and `pricingParam` fields (if passed) are ignored.

## See Also

- [object GetVppLicensesResponse](getvpplicensesresponse.md)
  The response with the licenses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/getvpplicensesrequest)*