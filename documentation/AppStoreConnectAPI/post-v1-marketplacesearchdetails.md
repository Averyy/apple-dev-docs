# Add a marketplace search detail url

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add a search detail URL for the alternative marketplace.

**Availability**:
- App Store Connect API 3.3+

## Mentions

- [Building a searchable catalog for your marketplace app for inclusion in Spotlight](building-a-searchable-catalog-for-your-marketplace-app-for-inclusion-in-spotlight.md)
- [App Store Connect API 3.3 release notes](app-store-connect-api-3-3-release-notes.md)
- [Configuring alternative marketplaces and alternative marketplace apps](configuring-alternative-marketplaces-and-alternative-marketplace-apps.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
POST https://api.appstoreconnect.apple.com/v1/marketplaceSearchDetails
{
  "data": {
    "type": "marketplaceSearchDetails",
    "attributes": {
      "catalogUrl": "https://example.com/crawler-site/sitemap.xml"
    },
    "relationships": {
      "app": {
        "data": {
          "type": "apps",
          "id": "6476788026"
        }
      }
    }
  }
}
```

**Response**:

```json
{
  “data” : {
    “type” : “marketplaceSearchDetails”,
    “id” : “cfcfc44f-8291-4b75-84f0-4d9a55e8b878”,
    “attributes” : {
      “catalogUrl” : “https://example.com/crawler-site/sitemap.xml”
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/marketplaceSearchDetails/cfcfc44f-8291-4b75-84f0-4d9a55e8b878”
    }
  },
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/apps/6476788026/marketplaceSearchDetail”
  }
}

```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/marketplaceSearchDetails`

## See Also

- [Building a searchable catalog for your marketplace app for inclusion in Spotlight](building-a-searchable-catalog-for-your-marketplace-app-for-inclusion-in-spotlight.md)
  Set up and build your alternative marketplace’s searchable index.
- [Read the marketplace search detail url](get-v1-apps-_id_-marketplacesearchdetail.md)
  Get search detail URL for the alternative marketplace.
- [Get the marketplace search detail ID for an app](get-v1-apps-_id_-relationships-marketplacesearchdetail.md)
- [Modify a marketplace search detail url](patch-v1-marketplacesearchdetails-_id_.md)
  Update the search detail URL for the alternative marketplace.
- [Delete a marketplace search detail url](delete-v1-marketplacesearchdetails-_id_.md)
  Delete search detail URL for the alternative marketplace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-marketplacesearchdetails)*