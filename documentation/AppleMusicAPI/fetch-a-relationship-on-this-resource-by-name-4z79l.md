# Get a Catalog Music Video's Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a music video’s relationship by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/music-videos/1555764127/artists
```

**Response**:

```json
{
  "data": [
    {
      "id": "444520760",
      "type": "artists",
      "href": "/v1/catalog/us/artists/444520760",
      "attributes": {
        "genreNames": [
          "Urbano latino"
        ],
        "url": "https://music.apple.com/us/artist/j-balvin/444520760",
        "name": "J Balvin",
        "artwork": {
          "width": 2509,
          "height": 2509,
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/65/a8/8f/65a88fc6-2f6d-b47a-a98c-daff3699857a/pr_source.png/{w}x{h}bb.jpg",
          "bgColor": "221e13",
          "textColor1": "eacdcc",
          "textColor2": "e0bbb5",
          "textColor3": "c2aaa7",
          "textColor4": "ba9b94"
        }
      },
      "relationships": {
        "albums": {
          "href": "/v1/catalog/us/artists/444520760/albums",
          "next": "/v1/catalog/us/artists/444520760/albums?offset=25",
          "data": [
            {
              "id": "1473307002",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1473307002"
            },
            {
              "id": "1470146332",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1470146332"
            },
            {
              "id": "1500490683",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1500490683"
            },
            {
              "id": "1368816332",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1368816332"
            },
            {
              "id": "1550164245",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1550164245"
            },
            {
              "id": "1581021903",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1581021903"
            },
            {
              "id": "1440834941",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1440834941"
            },
            {
              "id": "1523626060",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1523626060"
            },
            {
              "id": "1440862370",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1440862370"
            },
            {
              "id": "1600960018",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1600960018"
            },
            {
              "id": "1440817272",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1440817272"
            },
            {
              "id": "1442872595",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1442872595"
            },
            {
              "id": "1457085973",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1457085973"
            },
            {
              "id": "1523100098",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1523100098"
            },
            {
              "id": "1460707396",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1460707396"
            },
            {
              "id": "1466700223",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1466700223"
            },
            {
              "id": "1299972303",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1299972303"
            },
            {
              "id": "1550172227",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1550172227"
            },
            {
              "id": "1453721558",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1453721558"
            },
            {
              "id": "1497621658",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1497621658"
            },
            {
              "id": "1573431826",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1573431826"
            },
            {
              "id": "1526901305",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1526901305"
            },
            {
              "id": "1314699505",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1314699505"
            },
            {
              "id": "1529959307",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1529959307"
            },
            {
              "id": "1538192838",
              "type": "albums",
              "href": "/v1/catalog/us/albums/1538192838"
            }
          ]
        }
      }
    }
  ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/music-videos/{id}/{relationship}`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object MusicVideos](musicvideos.md)
  A resource object that represents a music video.
- [object MusicVideosResponse](musicvideosresponse.md)
  The response to a music videos request.
- [Get a Catalog Music Video](get-a-catalog-music-video.md)
  Fetch a music video by using its identifier.
- [Get a Catalog Music Video’s Relationship View Directly by Name](fetch-a-view-on-this-resource-by-name-5657g.md)
  Fetch related resources for a single music video’s relationship view.
- [Get Multiple Catalog Music Videos by ID](get-multiple-catalog-music-videos-by-id.md)
  Fetch one or more music videos by using their identifiers.
- [Get Multiple Catalog Music Videos by ISRC](get-multiple-catalog-music-videos-by-isrc.md)
  Fetch one or more music videos by using their International Standard Recording Code (ISRC) values.
- [Get Equivalent Catalog Music Videos by ID](get-equivalent-ids-for-the-albums-8tp4l.md)
  Fetch the equivalent, available content in the storefront for the provided music videos’ identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-relationship-on-this-resource-by-name-4z79l)*