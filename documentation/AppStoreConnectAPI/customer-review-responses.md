# Customer Review Responses

**Framework**: App Store Connect API

Get, create, update, and delete your responses to customer reviews.

#### Overview

The `customerReviewResponses` resource represents your responses to customer reviews for apps you publish on the App Store. Each customer review can have at most one review response.

Use this API to get, create, update, and delete your responses to customer reviews for your app. First, get a list of customer reviews, including their resource IDs, by calling the [`List All Customer Reviews for an App`](get-v1-apps-_id_-customerreviews.md) or [`List All Customer Reviews for an App Store Version`](get-v1-appstoreversions-_id_-customerreviews.md) endpoints. Next use this API as follows:

- Respond to a customer review by calling [`Create or Update a Response to a Customer Review`](post-v1-customerreviewresponses.md) using the review’s resource ID. Update your existing review using the same endpoint.
- Get your existing review response by calling [`Get a Customer Review Response`](get-v1-customerreviews-_id_-response.md), using the resource ID of the customer review.
- Delete your response to a customer review by calling [`Delete a Response to a Customer Review`](delete-v1-customerreviewresponses-_id_.md), using the resource ID of your response.

For more information about reviews, see [`Ratings, Reviews, and Responses`](https://developer.apple.comhttps://developer.apple.com/app-store/ratings-and-reviews/).

## Topics

### Getting Review Responses
- [Get a Customer Review Response](get-v1-customerreviews-_id_-response.md)
  Get the response to a specific customer review.
- [Read Customer Review Response Information](get-v1-customerreviewresponses-_id_.md)
  Get information about a specific response you wrote to a customer review, including the response content and its state.
### Creating, Updating, and Deleting Review Responses
- [Create or Update a Response to a Customer Review](post-v1-customerreviewresponses.md)
  Create a response or replace an existing response you wrote to a customer review.
- [Delete a Response to a Customer Review](delete-v1-customerreviewresponses-_id_.md)
  Delete a specific response you wrote to a customer review.
### Objects and Types
- [object CustomerReviewResponseV1Response](customerreviewresponsev1response.md)
  A response that contains a single Customer Review Responses resource.
- [object CustomerReviewResponseV1](customerreviewresponsev1.md)
  The data structure that represents the Customer Review Responses resource.
- [object CustomerReviewResponseV1CreateRequest](customerreviewresponsev1createrequest.md)
  The request body to use to create a response to a customer review.
- [object CustomerReview](customerreview.md)
  The data structure that represents a Customer Reviews resource.

## See Also

- [Customer Reviews](customer-reviews.md)
  Get the customer reviews for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/customer-review-responses)*