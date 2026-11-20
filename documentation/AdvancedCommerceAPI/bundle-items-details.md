# Bundle Items Details

**Framework**: Advanced Commerce API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- Advanced Commerce API 1.3+

## Endpoint

`GET https://api.storekit-sandbox.apple.com/advancedCommerce/v2/bundleItems/details/{transactionId}`

## Parameters

### Path Parameters

- `transactionId` (string) *(required)*

## Responses

- `200` OK (`BundleItemsDetailsResponse`, `application/json`)
- `400` Bad Request (`(InvalidTransactionIdError | TransactionIdMustBeBundleError | FamilyTransactionNotSupportedError)`, `application/json`)
- `401` Unauthorized (`UnauthorizedError`, `application/json`)
- `403` Forbidden (`ForbiddenError`, `application/json`)
- `404` Not Found (`(NotFoundError | TransactionIdNotFoundError)`, `application/json`)
- `429` (`RateLimitExceededError`, `application/json`)
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`)

## See Also

### Bundle items details from the server
- [object BundleItemsDetailsResponse](./bundleitemsdetailsresponse.md)
- [object BundleItemsDetailsItem](./bundleitemsdetailsitem.md)
- [object BundleItemsDetailsBundleItem](./bundleitemsdetailsbundleitem.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/bundle-items-details)*