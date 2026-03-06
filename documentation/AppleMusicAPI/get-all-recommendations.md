# Get Default Recommendations

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch default recommendations.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains an array of `Recommendation` objects. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/recommendations
```

**Response**:

```json
{
    "data": [
        {
            "id": "6-27s5hU6azhJY",
            "type": "personal-recommendation",
            "href": "/v1/me/recommendations/6-27s5hU6azhJY",
            "attributes": {
                "resourceTypes": [
                    "playlists"
                ],
                "title": {
                    "stringForDisplay": "Made for You"
                },
                "isGroupRecommendation": false,
                "kind": "music-recommendations",
                "nextUpdateDate": "2021-10-07T15: 59: 59Z"
            },
            "relationships": {
                "contents": {
                    "href": "/v1/me/recommendations/6-27s5hU6azhJY/contents",
                    "data": [
                        {
                            "id": "pl.pm-20e9f373919da080f53d220d517f74d7",
                            "type": "playlists",
                            "href": "/v1/catalog/us/playlists/pl.pm-20e9f373919da080f53d220d517f74d7",
                            "attributes": {
                                "artwork": {
                                    "width": 4320,
                                    "height": 1080,
                                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Features124/v4/c7/65/0e/c7650e0f-1403-bf84-4631-b43fcf5c0e65/source/{w}x{h}cc.jpg",
                                    "bgColor": "5500e8",
                                    "textColor1": "ffffff",
                                    "textColor2": "b18bfd",
                                    "textColor3": "d45be3",
                                    "textColor4": "9d6ef9"
                                },
                                "isChart": false,
                                "url": "https: //music.apple.com/us/playlist/favorites-mix/pl.pm-20e9f373919da080f53d220d517f74d7",
                                "lastModifiedDate": "2021-10-05T10: 22: 32Z",
                                "name": "Favorites Mix",
                                "playlistType": "personal-mix",
                                "curatorName": "Apple Music for Me",
                                "playParams": {
                                    "id": "pl.pm-20e9f373919da080f53d220d517f74d7",
                                    "kind": "playlist",
                                    "versionHash": "63962df0-28ba-4366-a8bc-051a013a7302"
                                },
                                "description": {
                                    "standard": "The songs you love. The more you use Apple Music, the better the mix. Refreshed every Tuesday."
                                }
                            }
                        },
                        {
                            "id": "pl.pm-20e9f373919da080c9acf072d1e4e905",
                            "type": "playlists",
                            "href": "/v1/catalog/us/playlists/pl.pm-20e9f373919da080c9acf072d1e4e905",
                            "attributes": {
                                "artwork": {
                                    "width": 4320,
                                    "height": 1080,
                                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Features124/v4/89/c5/6b/89c56b0c-1368-cd76-df44-0711943e4d52/source/{w}x{h}cc.jpg",
                                    "bgColor": "f02807",
                                    "textColor1": "ffffff",
                                    "textColor2": "120f03",
                                    "textColor3": "321401",
                                    "textColor4": "331403"
                                },
                                "isChart": false,
                                "url": "https: //music.apple.com/us/playlist/get-up-mix/pl.pm-20e9f373919da080c9acf072d1e4e905",
                                "lastModifiedDate": "2021-10-04T10: 22: 32Z",
                                "name": "Get Up! Mix",
                                "playlistType": "personal-mix",
                                "curatorName": "Apple Music for Me",
                                "playParams": {
                                    "id": "pl.pm-20e9f373919da080c9acf072d1e4e905",
                                    "kind": "playlist",
                                    "versionHash": "3ed341de-6df7-4838-9028-f0317b371f10"
                                },
                                "description": {
                                    "standard": "Whether it’s Monday morning or Friday night, get going with this personalized mix of upbeat music."
                                }
                            }
                        },
                        {
                            "id": "pl.pm-20e9f373919da080fcdea99a51f26916",
                            "type": "playlists",
                            "href": "/v1/catalog/us/playlists/pl.pm-20e9f373919da080fcdea99a51f26916",
                            "attributes": {
                                "artwork": {
                                    "width": 4320,
                                    "height": 1080,
                                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/Features114/v4/d9/ef/1d/d9ef1d48-27cb-8c70-b160-7259f93a4ad5/source/{w}x{h}cc.jpg",
                                    "bgColor": "145079",
                                    "textColor1": "ffffff",
                                    "textColor2": "5cfafb",
                                    "textColor3": "5ed7de",
                                    "textColor4": "4cd5df"
                                },
                                "isChart": false,
                                "url": "https: //music.apple.com/us/playlist/chill-mix/pl.pm-20e9f373919da080fcdea99a51f26916",
                                "lastModifiedDate": "2021-10-03T16: 18: 56Z",
                                "name": "Chill Mix",
                                "playlistType": "personal-mix",
                                "curatorName": "Apple Music for Me",
                                "playParams": {
                                    "id": "pl.pm-20e9f373919da080fcdea99a51f26916",
                                    "kind": "playlist",
                                    "versionHash": "747882d9-7d52-4c67-b5fe-91431dfd3065"
                                },
                                "description": {
                                    "standard": "Handpicked songs to help you relax and unwind. Updated every Sunday."
                                }
                            }
                        },
                        {
                            "id": "pl.pm-20e9f373919da080ed066797045413d1",
                            "type": "playlists",
                            "href": "/v1/catalog/us/playlists/pl.pm-20e9f373919da080ed066797045413d1",
                            "attributes": {
                                "artwork": {
                                    "width": 4320,
                                    "height": 1080,
                                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/Features114/v4/b0/6e/4f/b06e4f16-e1d2-083a-041c-ace63bac19f4/source/{w}x{h}cc.jpg",
                                    "bgColor": "fc6a7b",
                                    "textColor1": "ffffff",
                                    "textColor2": "121010",
                                    "textColor3": "351418",
                                    "textColor4": "351f21"
                                },
                                "isChart": false,
                                "url": "https: //music.apple.com/us/playlist/new-music-mix/pl.pm-20e9f373919da080ed066797045413d1",
                                "lastModifiedDate": "2021-10-01T12: 37: 58Z",
                                "name": "New Music Mix",
                                "playlistType": "personal-mix",
                                "curatorName": "Apple Music for Me",
                                "playParams": {
                                    "id": "pl.pm-20e9f373919da080ed066797045413d1",
                                    "kind": "playlist",
                                    "versionHash": "5d0a8b96-5b41-423b-915f-df89fc7dc3b3"
                                },
                                "description": {
                                    "standard": "Discover new music from artists we think you’ll like. Refreshed every Friday."
                                }
                            }
                        }
                    ]
                }
            }
        }
    ]
}

```

## Endpoint

`GET https://api.music.apple.com/v1/me/recommendations`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `offset` (string): The next page or group of objects to fetch.
- `include` ([string]): Additional relationships to include in the fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object PersonalRecommendation](personalrecommendation.md)
  A resource object that represents recommended resources for a user calculated using their selected preferences.
- [object PersonalRecommendationResponse](personalrecommendationresponse.md)
  The response to a request for personal recommendations.
- [Get a Recommendation](get-a-recommendation.md)
  Fetch a recommendation by using its identifier.
- [Get a Recommendation Relationship Directly by Name](get-a-relationship-on-the-recommendation.md)
  Fetch a recommendation’s relationship by using its identifier.
- [Get Multiple Recommendations](get-multiple-recommendations.md)
  Fetch one or more recommendations by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-all-recommendations)*