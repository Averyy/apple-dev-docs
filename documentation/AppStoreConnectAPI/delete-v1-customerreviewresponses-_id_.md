# Delete a response to a customer review

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete a specific response you wrote to a customer review.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

Deletions of responses don’t take effect instantly in the App Store. Allow some time for the deletion to take effect.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/customerReviewResponses/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies a `customerReviewResponses` resource that represents your review response.

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Updating, and Deleting Review Responses
- [Create or update a response to a customer review](./post-v1-customerreviewresponses.md)
  Create a response or replace an existing response you wrote to a customer review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-customerreviewresponses-_id_)*