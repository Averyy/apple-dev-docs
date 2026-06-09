# Delete a marketplace search detail url

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete search detail URL for the alternative marketplace.

**Availability**:
- App Store Connect API 3.3+

#### Discussion

##### Example Request and Response

**Request**:

```None
DELETE https://api.appstoreconnect.apple.com/v1/marketplaceSearchDetails/{id}
```

**Response**:

```json
204
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/marketplaceSearchDetails/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `marketplace search details` resource ID from the [`Read the marketplace search detail url`](get-v1-apps-_id_-marketplacesearchdetail.md) response.

## See Also

- [Building a searchable catalog for your marketplace app for inclusion in Spotlight](building-a-searchable-catalog-for-your-marketplace-app-for-inclusion-in-spotlight.md)
  Set up and build your alternative marketplace’s searchable index.
- [Add a marketplace search detail url](post-v1-marketplacesearchdetails.md)
  Add a search detail URL for the alternative marketplace.
- [Read the marketplace search detail url](get-v1-apps-_id_-marketplacesearchdetail.md)
  Get search detail URL for the alternative marketplace.
- [Get the marketplace search detail ID for an app](get-v1-apps-_id_-relationships-marketplacesearchdetail.md)
- [Modify a marketplace search detail url](patch-v1-marketplacesearchdetails-_id_.md)
  Update the search detail URL for the alternative marketplace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-marketplacesearchdetails-_id_)*