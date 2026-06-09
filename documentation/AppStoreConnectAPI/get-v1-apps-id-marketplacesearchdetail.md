# Read the marketplace search detail url

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get search detail URL for the alternative marketplace.

**Availability**:
- App Store Connect API 3.3+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/6476788026/marketplaceSearchDetail
```

**Response**:

```json
{
  "data" : {
    "type" : "marketplaceSearchDetails",
    "id" : "cfcfc44f-8291-4b75-84f0-4d9a55e8b878",
    "attributes" : {
      "catalogUrl" : "https://example.com/crawler-site/sitemap.xml"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/marketplaceSearchDetails/cfcfc44f-8291-4b75-84f0-4d9a55e8b878"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/apps/6476788026/marketplaceSearchDetail"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/marketplaceSearchDetail`

## Parameters

- `fields[marketplaceSearchDetails]` ([string]): Additional fields to include for each marketplace search detail resource returned by the response.

## See Also

- [Building a searchable catalog for your marketplace app for inclusion in Spotlight](building-a-searchable-catalog-for-your-marketplace-app-for-inclusion-in-spotlight.md)
  Set up and build your alternative marketplace’s searchable index.
- [Add a marketplace search detail url](post-v1-marketplacesearchdetails.md)
  Add a search detail URL for the alternative marketplace.
- [Get the marketplace search detail ID for an app](get-v1-apps-_id_-relationships-marketplacesearchdetail.md)
- [Modify a marketplace search detail url](patch-v1-marketplacesearchdetails-_id_.md)
  Update the search detail URL for the alternative marketplace.
- [Delete a marketplace search detail url](delete-v1-marketplacesearchdetails-_id_.md)
  Delete search detail URL for the alternative marketplace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-marketplacesearchdetail)*