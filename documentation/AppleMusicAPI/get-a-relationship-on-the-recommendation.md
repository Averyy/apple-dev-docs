# Get a Recommendation Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a recommendation’s relationship by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains a single [`PersonalRecommendation.Relationships`](personalrecommendation/relationships-data.dictionary.md) object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/recommendations/6-27s5hU6azhJY/contents
```

**Response**:

```json
{
    "data": [
        {
            "id": "pl.pm-20e9f373919da080ea5e53d0c834bfea",
            "type": "playlists",
            "href": "/v1/catalog/us/playlists/pl.pm-20e9f373919da080ea5e53d0c834bfea",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https://is2-ssl.mzstatic.com/image/thumb/Features114/v4/9f/fe/a4/9ffea4c9-ac6e-ea9e-89c4-29c1ebf32dcf/U0MtTVMtV1ctUGVyc29uYWxpemVkX01peGVzLU5ld011c2ljLUFEQU1fSUQ9MTExOTM4OTk2Ny5wbmc.png/{w}x{h}cc.jpg",
                    "bgColor": "fc6a7b",
                    "textColor1": "ffffff",
                    "textColor2": "121010",
                    "textColor3": "351418",
                    "textColor4": "351f21"
                },
                "isChart": false,
                "url": "https://music.apple.com/us/playlist/new-music-mix/pl.pm-20e9f373919da080ea5e53d0c834bfea",
                "lastModifiedDate": "2022-04-15T01:04:34Z",
                "name": "New Music Mix",
                "playlistType": "personal-mix",
                "curatorName": "Apple Music for Me",
                "playParams": {
                    "id": "pl.pm-20e9f373919da080ea5e53d0c834bfea",
                    "kind": "playlist",
                    "versionHash": "e806c16946615eb4afbaae664b5f3b4d5558204bc768f82a64343c8aec159971"
                },
                "description": {
                    "standard": "Discover new music from artists we think you'll like. Refreshed every Friday."
                }
            }
        },
        {
            "id": "pl.pm-20e9f373919da080cebec9e066527fcc",
            "type": "playlists",
            "href": "/v1/catalog/us/playlists/pl.pm-20e9f373919da080cebec9e066527fcc",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https://is4-ssl.mzstatic.com/image/thumb/Features114/v4/83/47/18/83471885-22a3-e3f0-3589-374fd60fe6b0/U0MtTVMtV1ctUGVyc29uYWxpemVkX01peGVzLUZhdm9yaXRlcy1BREFNX0lEPTExMTk2OTMyODIucG5n.png/{w}x{h}cc.jpg",
                    "bgColor": "5500e8",
                    "textColor1": "ffffff",
                    "textColor2": "b18bfd",
                    "textColor3": "d45be3",
                    "textColor4": "9d6ef9"
                },
                "isChart": false,
                "url": "https://music.apple.com/us/playlist/favorites-mix/pl.pm-20e9f373919da080cebec9e066527fcc",
                "lastModifiedDate": "2022-04-12T00:36:26Z",
                "name": "Favorites Mix",
                "playlistType": "personal-mix",
                "curatorName": "Apple Music for Me",
                "playParams": {
                    "id": "pl.pm-20e9f373919da080cebec9e066527fcc",
                    "kind": "playlist",
                    "versionHash": "29a5a080b52a6f016e3e642db9d35c9cb415b629d8aa7e9aad11747d1268536d"
                },
                "description": {
                    "standard": "The songs you love. The more you use Apple Music, the better the mix. Refreshed every Tuesday."
                }
            }
        },
        {
            "id": "pl.pm-20e9f373919da080a92d499ffb0c8974",
            "type": "playlists",
            "href": "/v1/catalog/us/playlists/pl.pm-20e9f373919da080a92d499ffb0c8974",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https://is5-ssl.mzstatic.com/image/thumb/Features124/v4/7d/5e/8e/7d5e8efa-6d09-e23a-037a-48e19b5a7b6d/U0MtTVMtV1ctUGVyc29uYWxpemVkX01peGVzLUdldFVwLUFEQU1fSUQ9MTQ0MTI3Njc4MS5wbmc.png/{w}x{h}cc.jpg",
                    "bgColor": "f02807",
                    "textColor1": "ffffff",
                    "textColor2": "120f03",
                    "textColor3": "321401",
                    "textColor4": "331403"
                },
                "isChart": false,
                "url": "https://music.apple.com/us/playlist/get-up-mix/pl.pm-20e9f373919da080a92d499ffb0c8974",
                "lastModifiedDate": "2022-04-11T01:53:08Z",
                "name": "Get Up! Mix",
                "playlistType": "personal-mix",
                "curatorName": "Apple Music for Me",
                "playParams": {
                    "id": "pl.pm-20e9f373919da080a92d499ffb0c8974",
                    "kind": "playlist",
                    "versionHash": "72f82e6b6f2a2a2ed815ab4b3cecc1e2a4386d2a131ad1a20a4bb6e58f8f463c"
                },
                "description": {
                    "standard": "Whether it’s Monday morning or Friday night, get going with this personalized mix of upbeat music."
                }
            }
        },
        {
            "id": "pl.pm-20e9f373919da08064bdcea5b99d1fb9",
            "type": "playlists",
            "href": "/v1/catalog/us/playlists/pl.pm-20e9f373919da08064bdcea5b99d1fb9",
            "attributes": {
                "artwork": {
                    "width": 4320,
                    "height": 1080,
                    "url": "https://is2-ssl.mzstatic.com/image/thumb/Features114/v4/ab/fa/bd/abfabdec-2a43-dcb7-8991-5ab180c0fa6d/U0MtTVMtV1ctUGVyc29uYWxpemVkX01peGVzLUNoaWxsLUFEQU1fSUQ9MTE5OTIyMjI0My5wbmc.png/{w}x{h}cc.jpg",
                    "bgColor": "145079",
                    "textColor1": "ffffff",
                    "textColor2": "5cfafb",
                    "textColor3": "5ed7de",
                    "textColor4": "4cd5df"
                },
                "isChart": false,
                "url": "https://music.apple.com/us/playlist/chill-mix/pl.pm-20e9f373919da08064bdcea5b99d1fb9",
                "lastModifiedDate": "2022-04-10T01:31:40Z",
                "name": "Chill Mix",
                "playlistType": "personal-mix",
                "curatorName": "Apple Music for Me",
                "playParams": {
                    "id": "pl.pm-20e9f373919da08064bdcea5b99d1fb9",
                    "kind": "playlist",
                    "versionHash": "b0c1a0fff713230e787bc9ed2e994bd8123a7427e6da85725bbfff7180d893be"
                },
                "description": {
                    "standard": "Handpicked songs to help you relax and unwind. Updated every Sunday."
                }
            }
        }
    ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/me/recommendations/{id}/{relationship}`

## Parameters

- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object PersonalRecommendation](personalrecommendation.md)
  A resource object that represents recommended resources for a user calculated using their selected preferences.
- [object PersonalRecommendationResponse](personalrecommendationresponse.md)
  The response to a request for personal recommendations.
- [Get a Recommendation](get-a-recommendation.md)
  Fetch a recommendation by using its identifier.
- [Get Multiple Recommendations](get-multiple-recommendations.md)
  Fetch one or more recommendations by using their identifiers.
- [Get Default Recommendations](get-all-recommendations.md)
  Fetch default recommendations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-relationship-on-the-recommendation)*