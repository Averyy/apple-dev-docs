# Customer Reviews

**Framework**: App Store Connect API

Get the customer reviews for your app.

#### Overview

The `customerReviews` resource represents the ratings and reviews that customers write for your app that the App Store displays. Customers can provide reviews for your app in the App Store, or when your app requests a review. For more information about reviews, see [`Ratings, Reviews, and Responses`](https://developer.apple.comhttps://developer.apple.com/app-store/ratings-and-reviews/).

Use this API to read the customer reviews for your app as follows:

- Call the [`List all customer reviews for an app`](get-v1-apps-_id_-customerreviews.md) endpoint to get all customer reviews for your app. Filter the reviews by territory and rating, and sort them by date or rating. You can also get a list of the reviews with or without published responses.
- Call the [`List all customer reviews for an app store version`](get-v1-appstoreversions-_id_-customerreviews.md) endpoint to get the customer reviews for a specific app version.
- Call the [`Read customer review information`](get-v1-customerreviews-_id_.md) endpoint using the resource ID of the review to read the details of a specific review.

To manage your responses to the customers reviews, use the endpoints in [`Customer Review Responses`](customer-review-responses.md). For example, call [`Get a customer review response`](get-v1-customerreviews-_id_-response.md) using the resource ID of the customer review to read your response to that review.

## Topics

### Getting customer reviews for an app or app version
- [List all customer reviews for an app](get-v1-apps-_id_-customerreviews.md)
  Get a list of customer reviews for a specific app.
- [List customer review IDs for an app](get-v1-apps-_id_-relationships-customerreviews.md)
- [List all customer reviews for an app store version](get-v1-appstoreversions-_id_-customerreviews.md)
  Get a list of customer reviews for a specific version of your app.
### Reading customer reviews
- [Read customer review information](get-v1-customerreviews-_id_.md)
  Get information about a specific customer review, including the review content.
### Reading review summariztions
- [Read Customer Review Summarizations](get-v1-apps-_id_-customerreviewsummarizations.md)
  Get the customer review summarization for a specific app.
### Objects
- [object CustomerReviewsResponse](customerreviewsresponse.md)
  The response body for endpoints that list customer reviews for an app.
- [object CustomerReviewResponse](customerreviewresponse.md)
  The response body for endpoints that read a single customer review for an app.
- [object CustomerReview](customerreview.md)
  A customer’s rating and written review of your app on the App Store.
- [object AppCustomerReviewsLinkagesResponse](appcustomerreviewslinkagesresponse.md)
- [object CustomerReviewSummarization](customerreviewsummarization.md)
  An AI-generated summary of customer reviews for an app in a specific App Store territory.
- [object CustomerReviewSummarizationsResponse](customerreviewsummarizationsresponse.md)
  A response containing a list of AI-generated review summaries for an app across territories.

## See Also

- [Customer Review Responses](customer-review-responses.md)
  Get, create, update, and delete your responses to customer reviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/customer-reviews)*