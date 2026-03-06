# Get Multiple Catalog Curators

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more curators by using their identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains an array of `Curator` objects. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/curators?ids=976439448,1107687517
```

**Response**:

```json
{
    "data": [
        {
            "attributes": {
                "artwork": {
                    "bgColor": "0a0a0a",
                    "height": 1080,
                    "textColor1": "ffffff",
                    "textColor2": "ededed",
                    "textColor3": "cdcdcd",
                    "textColor4": "bfbfbf",
                    "url": "https://example.mzstatic.com/image/thumb/Features7/v4/e8/f0/98/e8f098f5-6220-7203-105a-fdae6d5c4a10/source/{w}x{h}bb.jpeg",
                    "width": 1080
                },
                "editorialNotes": {
                    "short": "The show that made country music famous.",
                    "standard": "The Grand Ole Opry is the show that made country music famous. Emanating from Nashville, Tennessee since 1925, the Opry showcases a country music mix featuring traditional country, today's chart-topping hits, bluegrass, Americana, and more performed by new stars, superstars, and legends of the genre."
                },
                "name": "Grand Ole Opry",
                "url": "https://itunes.apple.com/us/curator/grand-ole-opry/id976439448"
            },
            "href": "/v1/catalog/us/curators/976439448",
            "id": "976439448",
            "relationships": {
                "playlists": {
                    "data": [
                        {
                            "href": "/v1/catalog/us/playlists/pl.a3fbcd31033f4667b7e4cadb26cdffd6",
                            "id": "pl.a3fbcd31033f4667b7e4cadb26cdffd6",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.421a7655263e413781d8cf1e7532c4c0",
                            "id": "pl.421a7655263e413781d8cf1e7532c4c0",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.969172eed79a40509bc6ab1673b7ec73",
                            "id": "pl.969172eed79a40509bc6ab1673b7ec73",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.18e8e689ee634fecb335e2b01f2b0533",
                            "id": "pl.18e8e689ee634fecb335e2b01f2b0533",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.4d49950c76ec4bc988487c37f900a363",
                            "id": "pl.4d49950c76ec4bc988487c37f900a363",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.23e9754f77b240ff839a591b4832330a",
                            "id": "pl.23e9754f77b240ff839a591b4832330a",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.8a13d72feb1c41179ca7241ebdf36a44",
                            "id": "pl.8a13d72feb1c41179ca7241ebdf36a44",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.e6acb8e6798845b68d2b231dd318d64c",
                            "id": "pl.e6acb8e6798845b68d2b231dd318d64c",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.e2a4aadbf54c446b826ea10f1d0997be",
                            "id": "pl.e2a4aadbf54c446b826ea10f1d0997be",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.b39649bcfc3f49a0bb143025784d6d90",
                            "id": "pl.b39649bcfc3f49a0bb143025784d6d90",
                            "type": "playlists"
                        }
                    ],
                    "href": "/v1/catalog/us/curators/976439448/playlists",
                    "next": "/v1/catalog/us/curators/976439448/playlists?offset=10"
                }
            },
            "type": "curators"
        },
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

`GET https://api.music.apple.com/v1/catalog/{storefront}/curators`

## Parameters

- `ids` ([string]) *(required)*: The unique identifiers for the curators. The maximum fetch limit is 100.
- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Curators](curators.md)
  A resource object that represents a curator.
- [object CuratorsResponse](curatorsresponse.md)
  The response to a request for curators.
- [Get a Catalog Curator](get-a-catalog-curator.md)
  Fetch a curator by using the curator’s identifier.
- [Get a Catalog Curator's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-1091z.md)
  Fetch a curator’s relationship by using its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-catalog-curators)*