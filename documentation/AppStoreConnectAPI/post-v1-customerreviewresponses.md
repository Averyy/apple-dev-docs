# Create or update a response to a customer review

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a response or replace an existing response you wrote to a customer review.

**Availability**:
- App Store Connect API 2.0+

## Discussion

Use this endpoint to create a response to a customer review and publish it in the App Store. If a response already exists, this endpoint updates the response by overwriting it.

Responses don’t appear in the App Store instantly. Allow some time for the App Store to publish the response.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/customerReviewResponses`

## Request Body

**Content-Type**: `application/json`  
**Type**: `CustomerReviewResponseV1CreateRequest`

The request body of the customer review response.

## Responses

- `201` Created (`CustomerReviewResponseV1Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data isn’t valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Updating, and Deleting Review Responses
- [Delete a response to a customer review](./delete-v1-customerreviewresponses-_id_.md)
  Delete a specific response you wrote to a customer review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-customerreviewresponses)*