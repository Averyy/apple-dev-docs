# List All Customer Reviews for an App Store Version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of customer reviews for a specific version of your app.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/d716c220-3de9-4cf2-a885-8cfb43a11087/customerReviews?limit=1&filter%5Bterritory%5D=USA
```

**Response**:

```json
{
  "data": [
    {
      "type": "customerReviews",
      "id": "00000028-b08c-0014-9674-c54800000000",
      "attributes": {
        "rating": 5,
        "title": "Pretty Stellar",
        "body": "I love how creative I can be when I use this app. I can really explore the depths of my imagination!",
        "reviewerNickname": "Juan Chavez",
        "createdDate": "2024-01-02T11:19:36-07:00",
        "territory": "USA"
      },
      "relationships": {
        "response": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/customerReviews/00000028-b08c-0014-9674-c54800000000/relationships/response",
            "related": "https://api.appstoreconnect.apple.com/v1/customerReviews/00000028-b08c-0014-9674-c54800000000/response"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/customerReviews/00000028-b08c-0014-9674-c54800000000"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/d716c220-3de9-4cf2-a885-8cfb43a11087/customerReviews?filter%5Bterritory%5D=USA&limit=1",
    "next": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/d716c220-3de9-4cf2-a885-8cfb43a11087/customerReviews?cursor=AQ.AJJtGDc&filter%5Bterritory%5D=USA&limit=1"
  },
  "meta": {
    "paging": {
      "total": 10,
      "limit": 1
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/customerReviews`

## Parameters

- `fields[customerReviewResponses]` ([string]): Fields to return for included related types.
- `fields[customerReviews]` ([string]): Fields to return for included related types.
- `filter[rating]` ([string]): An array of numerical rating values by which to filter. For example, filtering for 1,2,5 shows only reviews with ratings of 1, 2, or 5. The minimum numeric rating value is 1, and the maximum is 5.
- `include` ([string]): Relationship data to include in the response.
- `limit` (integer): Number of resources to return.
- `sort` ([string]): Attributes by which to sort. Supports one sort parameter at a time.
- `filter[territory]` ([string]): A filter of territories to include in the response.
- `exists[publishedResponse]` (boolean): A Boolean value that filters the reviews based on whether the review has a published response in the App Store. Use `true` to return the customer reviews that already have a published response in the App Store. Use `false` to return the customer reviews that don’t have a published response. Note that it’s possible that a review has a response that isn’t yet published.

## See Also

- [List All Customer Reviews for an App](get-v1-apps-_id_-customerreviews.md)
  Get a list of customer reviews for a specific app.
- [GET /v1/apps/{id}/relationships/customerReviews](get-v1-apps-_id_-relationships-customerreviews.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-customerreviews)*