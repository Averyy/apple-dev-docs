# Get a Catalog Activity

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch an activity by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains a single `Activity` object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/activities/976439514
```

**Response**:

```json
{
    "data": [
        {
            "attributes": {
                "artwork": {
                    "bgColor": "fff3ab",
                    "height": 1080,
                    "textColor1": "541621",
                    "textColor2": "3d2d09",
                    "textColor3": "76423c",
                    "textColor4": "645529",
                    "url": "https://example.mzstatic.com/image/thumb/Features22/v4/83/fb/ed/83fbede3-1d5b-1173-cf10-952b629365f2/source/{w}x{h}bb.jpeg",
                    "width": 1080
                },
                "name": "Partying",
                "url": "https://itunes.apple.com/us/activity/partying/id976439514"
            },
            "href": "/v1/catalog/us/activities/976439514",
            "id": "976439514",
            "relationships": {
                "playlists": {
                    "data": [
                        {
                            "href": "/v1/catalog/us/playlists/pl.d4b72ba561fa4e26987b2fdac6493583",
                            "id": "pl.d4b72ba561fa4e26987b2fdac6493583",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.f33b77ef120e4cfdac94327b7a8dbec1",
                            "id": "pl.f33b77ef120e4cfdac94327b7a8dbec1",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.756f800e808a498ead67e6f1da818099",
                            "id": "pl.756f800e808a498ead67e6f1da818099",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.345858950de7481da73960314556679a",
                            "id": "pl.345858950de7481da73960314556679a",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.b5743c7fd4794020b0900d1f9be541f9",
                            "id": "pl.b5743c7fd4794020b0900d1f9be541f9",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.ae2769bd404b4116a8519581f8b311ec",
                            "id": "pl.ae2769bd404b4116a8519581f8b311ec",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.a04c08c92f40482bba229f630a9a01d8",
                            "id": "pl.a04c08c92f40482bba229f630a9a01d8",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.157cd02723c24f9aa01ca753a3127509",
                            "id": "pl.157cd02723c24f9aa01ca753a3127509",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.ff54c80a3733484cad0a0ea1104cfd5d",
                            "id": "pl.ff54c80a3733484cad0a0ea1104cfd5d",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.7445287d235749269e6f5a3a97a8efbc",
                            "id": "pl.7445287d235749269e6f5a3a97a8efbc",
                            "type": "playlists"
                        }
                    ],
                    "href": "/v1/catalog/us/activities/976439514/playlists",
                    "next": "/v1/catalog/us/activities/976439514/playlists?offset=10"
                }
            },
            "type": "activities"
        }
    ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/activities/{id}`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Activities](activities.md)
  A resource object that represents an activity curator.
- [object ActivitiesResponse](activitiesresponse.md)
  The response to a request for activities.
- [Get a Catalog Activity's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-1eqct.md)
  Fetch an activity’s relationship by using its identifier.
- [Get Multiple Catalog Activities](get-multiple-catalog-activities.md)
  Fetch one or more activities by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-catalog-activity)*