# List all customer reviews for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of customer reviews for a specific app.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

The example below limits the number of reviews returned in the response.

##### Example Request and Response

**Request**:

```
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

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the `apps` resource that represents your app. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[customerReviewResponses]` ([string]): Fields to return for the included related types.

  **Allowed Values**: `responseBody`, `lastModifiedDate`, `state`, `review`
- `fields[customerReviews]` ([string]): Fields to return for the included related types.

  **Allowed Values**: `rating`, `title`, `body`, `reviewerNickname`, `createdDate`, `territory`, `response`, `reviewTerritory`
- `filter[rating]` ([string]): An array of numerical rating values by which to filter. For example, filtering for 1,2,5 shows only reviews with ratings of 1, 2, or 5. The minimum numeric rating value is 1, and the maximum is 5.
- `include` ([string]): Relationship data to include in the response.

  **Allowed Values**: `response`, `reviewTerritory`
- `limit` (integer): Number of resources to return.

  **Maximum**: `200`
- `sort` ([string]): Attributes by which to sort. Supports one sort parameter at a time.

  **Allowed Values**: `rating`, `-rating`, `createdDate`, `-createdDate`
- `filter[territory]` ([string]): A filter of territories to include in the response.

  **Allowed Values**: `ABW`, `AFG`, `AGO`, `AIA`, `ALB`, `AND`, `ANT`, `ARE`, `ARG`, `ARM`, `ASM`, `ATG`, `AUS`, `AUT`, `AZE`, `BDI`, `BEL`, `BEN`, `BES`, `BFA`, `BGD`, `BGR`, `BHR`, `BHS`, `BIH`, `BLR`, `BLZ`, `BMU`, `BOL`, `BRA`, `BRB`, `BRN`, `BTN`, `BWA`, `CAF`, `CAN`, `CHE`, `CHL`, `CHN`, `CIV`, `CMR`, `COD`, `COG`, `COK`, `COL`, `COM`, `CPV`, `CRI`, `CUB`, `CUW`, `CXR`, `CYM`, `CYP`, `CZE`, `DEU`, `DJI`, `DMA`, `DNK`, `DOM`, `DZA`, `ECU`, `EGY`, `ERI`, `ESP`, `EST`, `ETH`, `FIN`, `FJI`, `FLK`, `FRA`, `FRO`, `FSM`, `GAB`, `GBR`, `GEO`, `GGY`, `GHA`, `GIB`, `GIN`, `GLP`, `GMB`, `GNB`, `GNQ`, `GRC`, `GRD`, `GRL`, `GTM`, `GUF`, `GUM`, `GUY`, `HKG`, `HND`, `HRV`, `HTI`, `HUN`, `IDN`, `IMN`, `IND`, `IRL`, `IRQ`, `ISL`, `ISR`, `ITA`, `JAM`, `JEY`, `JOR`, `JPN`, `KAZ`, `KEN`, `KGZ`, `KHM`, `KIR`, `KNA`, `KOR`, `KWT`, `LAO`, `LBN`, `LBR`, `LBY`, `LCA`, `LIE`, `LKA`, `LSO`, `LTU`, `LUX`, `LVA`, `MAC`, `MAR`, `MCO`, `MDA`, `MDG`, `MDV`, `MEX`, `MHL`, `MKD`, `MLI`, `MLT`, `MMR`, `MNE`, `MNG`, `MNP`, `MOZ`, `MRT`, `MSR`, `MTQ`, `MUS`, `MWI`, `MYS`, `MYT`, `NAM`, `NCL`, `NER`, `NFK`, `NGA`, `NIC`, `NIU`, `NLD`, `NOR`, `NPL`, `NRU`, `NZL`, `OMN`, `PAK`, `PAN`, `PER`, `PHL`, `PLW`, `PNG`, `POL`, `PRI`, `PRT`, `PRY`, `PSE`, `PYF`, `QAT`, `REU`, `ROU`, `RUS`, `RWA`, `SAU`, `SEN`, `SGP`, `SHN`, `SLB`, `SLE`, `SLV`, `SMR`, `SOM`, `SPM`, `SRB`, `SSD`, `STP`, `SUR`, `SVK`, `SVN`, `SWE`, `SWZ`, `SXM`, `SYC`, `TCA`, `TCD`, `TGO`, `THA`, `TJK`, `TKM`, `TLS`, `TON`, `TTO`, `TUN`, `TUR`, `TUV`, `TWN`, `TZA`, `UGA`, `UKR`, `UMI`, `URY`, `USA`, `UZB`, `VAT`, `VCT`, `VEN`, `VGB`, `VIR`, `VNM`, `VUT`, `WLF`, `WSM`, `XKS`, `YEM`, `ZAF`, `ZMB`, `ZWE`
- `exists[publishedResponse]` (boolean): A Boolean value that filters the reviews based on whether the review has a published response in the App Store. Use `true` to return the customer reviews that already have a published response in the App Store. Use `false` to return the customer reviews that don’t have a published response. Note that it’s possible that a review has a response that isn’t yet published.
- `fields[territories]` ([string]): **Allowed Values**: `currency`
- `filter[reviewTerritory]` ([string])

## Responses

- `200` OK (`CustomerReviewsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting customer reviews
- [List customer review IDs for an app](./get-v1-apps-_id_-relationships-customerreviews.md)
- [Read Customer Review Summarizations](./get-v1-apps-_id_-customerreviewsummarizations.md)
  Get the customer review summarization for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-customerreviews)*