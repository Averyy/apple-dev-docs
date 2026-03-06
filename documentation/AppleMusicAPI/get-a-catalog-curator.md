# Get a Catalog Curator

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a curator by using the curator’s identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains a single `Curator` object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/curators/1107687517
```

**Response**:

```json
{
    "data": [
        {
            "attributes": {
                "artwork": {
                    "bgColor": "ffffff",
                    "height": 1080,
                    "textColor1": "000000",
                    "textColor2": "2d2d2d",
                    "textColor3": "333333",
                    "textColor4": "575757",
                    "url": "https://example.mzstatic.com/image/thumb/Features30/v4/8a/d7/80/8ad7800c-06cd-db72-91c7-55ff8bec0346/source/{w}x{h}bb.jpeg",
                    "width": 1080
                },
                "editorialNotes": {
                    "short": "LargeUp is the global platform for Caribbean music, arts and culture. ",
                    "standard": "LargeUp, the global platform for Caribbean music, arts and culture. Since 2009, LargeUp.com has captured the vibrant sounds, styles, flavors, destinations and activities of the islands, spotlighting the best in reggae, dancehall, soca, reggaeton and kompa."
                },
                "name": "LargeUp",
                "url": "https://itunes.apple.com/us/curator/largeup/id1107687517"
            },
            "href": "/v1/catalog/us/curators/1107687517",
            "id": "1107687517",
            "relationships": {
                "playlists": {
                    "data": [],
                    "href": "/v1/catalog/us/curators/1107687517/playlists"
                }
            },
            "type": "curators"
        }
    ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/curators/{id}`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Curators](curators.md)
  A resource object that represents a curator.
- [object CuratorsResponse](curatorsresponse.md)
  The response to a request for curators.
- [Get a Catalog Curator's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-1091z.md)
  Fetch a curator’s relationship by using its identifier.
- [Get Multiple Catalog Curators](get-multiple-catalog-curators.md)
  Fetch one or more curators by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-catalog-curator)*