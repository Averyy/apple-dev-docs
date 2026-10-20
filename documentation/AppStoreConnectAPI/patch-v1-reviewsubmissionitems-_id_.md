# Update a review submission item

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update a specific review submission item.

**Availability**:
- App Store Connect API 1.7+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/reviewSubmissionItems/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `ReviewSubmissionItemUpdateRequest`

## Responses

- `200` OK (`ReviewSubmissionItemResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create a Review Submission Item](./post-v1-reviewsubmissionitems.md)
  Create a new review submission item.
- [Remove a review submission item](./delete-v1-reviewsubmissionitems-_id_.md)
  Remove a specific item from a review submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-reviewsubmissionitems-_id_)*