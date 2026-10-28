# Retrieve External Purchase Report

**Framework**: External Purchase Server API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get an external purchase report by providing its request identifier.

**Availability**:
- External Purchase Server API 1.0.0+

## Discussion

Call this endpoint to retrieve an external purchase report that you successfully sent to Apple. This endpoint takes the `requestIdentifier` that you create when you call [`Send External Purchase Report`](./send-external-purchase-report.md), for reports that were successfully submitted.

## Topics

### Data types
- [type requestIdentifier](./requestidentifier.md)
  A UUID that uniquely identifies an external purchase report.

## Endpoint

`GET https://api.storekit-sandbox.apple.com/externalPurchase/v1/reports/{requestIdentifier}`

## Parameters

### Path Parameters

- `requestIdentifier` (requestIdentifier) *(required)*: The UUID that identifies the external purchase report you’re requesting.

## Responses

- `200` OK (`RetrieveReportSuccessResponse`, `application/json`): Success. The [`RetrieveReportSuccessResponse`](./retrievereportsuccessresponse.md) object contains your report.
- `400` Bad Request (`NotFoundError`, `application/json`): The request returned an error. Check the `requestIdentifier` parameter to ensure it’s a valid identifer for a report that you successfully submitted.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid.
- `429`: Rate limit exceeded.
- `500` Internal Server Error: Server error. Try again later.

## See Also

### External purchase report retrieval
- [object RetrieveReportSuccessResponse](./retrievereportsuccessresponse.md)
  A response that indicates success and includes your external purchase report data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/retrieve-external-purchase-report)*