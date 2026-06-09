# List all customer reviews for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of customer reviews for a specific app.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

The example below limits the number of reviews returned in the response.

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/682658836/customerReviews?limit=1
```

**Response**:

```json
{
  "data": [
    {
      "type": "customerReviews",
      "id": "00000028-b08c-0014-729e-fbd500000000",
      "attributes": {
        "rating": 5,
        "title": "Awesome!!!",
        "body": "It's a really fantastic app!",
        "reviewerNickname": "Anne Johnson",
        "createdDate": "2017-11-15T08:10:34-08:00",
        "territory": "USA"
      },
      "relationships": {
        "response": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/customerReviews/00000028-b08c-0014-729e-fbd500000000/relationships/response",
            "related": "https://api.appstoreconnect.apple.com/v1/customerReviews/00000028-b08c-0014-729e-fbd500000000/response"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/customerReviews/00000028-b08c-0014-729e-fbd500000000"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/apps/682658836/customerReviews?limit=1",
    "next": "https://api.appstoreconnect.apple.com/v1/apps/682658836/customerReviews?cursor=AQ.AMt2C-U&limit=1"
  },
  "meta": {
    "paging": {
      "total": 4326,
      "limit": 1
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/customerReviews`

## Parameters

- `fields[customerReviewResponses]` ([string]): Fields to return for the included related types.
- `fields[customerReviews]` ([string]): Fields to return for the included related types.
- `filter[rating]` ([string]): An array of numerical rating values by which to filter. For example, filtering for 1,2,5 shows only reviews with ratings of 1, 2, or 5. The minimum numeric rating value is 1, and the maximum is 5.
- `include` ([string]): Relationship data to include in the response.
- `limit` (integer): Number of resources to return.
- `sort` ([string]): Attributes by which to sort. Supports one sort parameter at a time.
- `filter[territory]` ([string]): A filter of territories to include in the response.
- `exists[publishedResponse]` (boolean): A Boolean value that filters the reviews based on whether the review has a published response in the App Store. Use `true` to return the customer reviews that already have a published response in the App Store. Use `false` to return the customer reviews that don’t have a published response. Note that it’s possible that a review has a response that isn’t yet published.
- `fields[territories]` ([string])
- `filter[reviewTerritory]` ([string])

## See Also

- [List customer review IDs for an app](get-v1-apps-_id_-relationships-customerreviews.md)
- [Read Customer Review Summarizations](get-v1-apps-_id_-customerreviewsummarizations.md)
  Get the customer review summarization for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-customerreviews)*