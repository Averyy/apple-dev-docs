# Create or Update a Response to a Customer Review

**Framework**: App Store Connect API  
**Kind**: httpRequest

Create a response or replace an existing response you wrote to a customer review.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

Use this endpoint to create a response to a customer review and publish it in the App Store. If a response already exists, this endpoint updates the response by overwriting it.

Responses don’t appear in the App Store instantly. Allow some time for the App Store to publish the response.

## Request Body

The request body of the customer review response.

## See Also

- [Delete a Response to a Customer Review](delete-v1-customerreviewresponses-_id_.md)
  Delete a specific response you wrote to a customer review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-customerreviewresponses)*