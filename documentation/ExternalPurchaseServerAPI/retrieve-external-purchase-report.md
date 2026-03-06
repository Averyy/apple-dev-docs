# Retrieve External Purchase Report

**Framework**: External Purchase Server API  
**Kind**: httpRequest

Get an external purchase report by providing its request identifier.

**Availability**:
- External Purchase Server API 1.0.0+

#### Discussion

Call this endpoint to retrieve an external purchase report that you successfully sent to Apple. This endpoint takes the `requestIdentifier` that you create when you call [`Send External Purchase Report`](send-external-purchase-report.md), for reports that were successfully submitted.

## Topics

### Data types
- [type requestIdentifier](requestidentifier.md)
  A UUID that uniquely identifies an external purchase report.

## Endpoint

`GET https://api.storekit-sandbox.apple.com/externalPurchase/v1/reports/{requestIdentifier}`

## Parameters

- `requestIdentifier` (requestIdentifier) *(required)*: The UUID that identifies the external purchase report you’re requesting.

## See Also

- [object RetrieveReportSuccessResponse](retrievereportsuccessresponse.md)
  A response that indicates success and includes your external purchase report data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/retrieve-external-purchase-report)*