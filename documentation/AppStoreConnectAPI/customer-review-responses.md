# Customer Review Responses

**Framework**: App Store Connect API

Get, create, update, and delete your responses to customer reviews.

#### Overview

The `customerReviewResponses` resource represents your responses to customer reviews for apps you publish on the App Store. Each customer review can have at most one review response.

Use this API to get, create, update, and delete your responses to customer reviews for your app. First, get a list of customer reviews, including their resource IDs, by calling the [`List all customer reviews for an app`](get-v1-apps-_id_-customerreviews.md) or [`List all customer reviews for an app store version`](get-v1-appstoreversions-_id_-customerreviews.md) endpoints. Next use this API as follows:

- Respond to a customer review by calling [`Create or update a response to a customer review`](post-v1-customerreviewresponses.md) using the review’s resource ID. Update your existing review using the same endpoint.
- Get your existing review response by calling [`Get a customer review response`](get-v1-customerreviews-_id_-response.md), using the resource ID of the customer review.
- Delete your response to a customer review by calling [`Delete a response to a customer review`](delete-v1-customerreviewresponses-_id_.md), using the resource ID of your response.

For more information about reviews, see [`Ratings, Reviews, and Responses`](https://developer.apple.comhttps://developer.apple.com/app-store/ratings-and-reviews/).

## Topics

### Getting Review Responses
- [Get a customer review response](get-v1-customerreviews-_id_-response.md)
  Get the response to a specific customer review.
- [Read customer review response information](get-v1-customerreviewresponses-_id_.md)
  Get information about a specific response you wrote to a customer review, including the response content and its state.
- [Get the response ID for a customer review](get-v1-customerreviews-_id_-relationships-response.md)
### Creating, Updating, and Deleting Review Responses
- [Create or update a response to a customer review](post-v1-customerreviewresponses.md)
  Create a response or replace an existing response you wrote to a customer review.
- [Delete a response to a customer review](delete-v1-customerreviewresponses-_id_.md)
  Delete a specific response you wrote to a customer review.
### Objects and types
- [object CustomerReviewResponseV1Response](customerreviewresponsev1response.md)
  The response body for endpoints that create, read, or modify a developer’s response to a customer review.
- [object CustomerReviewResponseV1](customerreviewresponsev1.md)
  A developer’s public reply to a customer review on the App Store.
- [object CustomerReviewResponseV1CreateRequest](customerreviewresponsev1createrequest.md)
  The request body to use to create a response to a customer review.
- [object CustomerReview](customerreview.md)
  A customer’s rating and written review of your app on the App Store.
- [object AppCustomerReviewsLinkagesResponse](appcustomerreviewslinkagesresponse.md)
- [object CustomerReviewResponseLinkageResponse](customerreviewresponselinkageresponse.md)

## See Also

- [Customer Reviews](customer-reviews.md)
  Get the customer reviews for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/customer-review-responses)*