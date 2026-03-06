# Get Multiple Catalog Activities

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more activities by using their identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains an array of one or more `Activity` objects. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/activities?ids=976439514,976439503
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
        },
        {
            "attributes": {
                "artwork": {
                    "bgColor": "b4f4ff",
                    "height": 1080,
                    "textColor1": "17120a",
                    "textColor2": "1b3215",
                    "textColor3": "363f3b",
                    "textColor4": "3a5943",
                    "url": "https://example.mzstatic.com/image/thumb/Features117/v4/8e/fc/15/8efc1532-b710-e673-121a-69e4e04303b2/source/{w}x{h}bb.jpeg",
                    "width": 1080
                },
                "editorialNotes": {
                    "short": "This is a Short Note."
                },
                "name": "Chilling Out",
                "url": "https://itunes.apple.com/us/activity/chilling-out/id976439503"
            },
            "href": "/v1/catalog/us/activities/976439503",
            "id": "976439503",
            "relationships": {
                "playlists": {
                    "data": [
                        {
                            "href": "/v1/catalog/us/playlists/pl.06e740110c28496983475a46b6e513f3",
                            "id": "pl.06e740110c28496983475a46b6e513f3",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.cce754188e9c4adfa91910454b1df2f0",
                            "id": "pl.cce754188e9c4adfa91910454b1df2f0",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.6e9457a3cd2d46de928f864571a3c9d3",
                            "id": "pl.6e9457a3cd2d46de928f864571a3c9d3",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.106ed7fa2c264f489583700e102dcaa4",
                            "id": "pl.106ed7fa2c264f489583700e102dcaa4",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.cf3334ec6a1e4c39b1b87fbd7850c11c",
                            "id": "pl.cf3334ec6a1e4c39b1b87fbd7850c11c",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.8ff6a890525d4bd38f9cb4c5132e6866",
                            "id": "pl.8ff6a890525d4bd38f9cb4c5132e6866",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.e6b02269cff64fd4af2b1a3c0b46907d",
                            "id": "pl.e6b02269cff64fd4af2b1a3c0b46907d",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.8311c063dfae4776b1f111bdd8af5cc2",
                            "id": "pl.8311c063dfae4776b1f111bdd8af5cc2",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.588df270ded249cbad1dd1e40e906faf",
                            "id": "pl.588df270ded249cbad1dd1e40e906faf",
                            "type": "playlists"
                        },
                        {
                            "href": "/v1/catalog/us/playlists/pl.b37923ba50e74c71948dabdaaa6a8dc5",
                            "id": "pl.b37923ba50e74c71948dabdaaa6a8dc5",
                            "type": "playlists"
                        }
                    ],
                    "href": "/v1/catalog/us/activities/976439503/playlists",
                    "next": "/v1/catalog/us/activities/976439503/playlists?offset=10"
                }
            },
            "type": "activities"
        }
    ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/activities`

## Parameters

- `ids` ([string]) *(required)*: The unique identifiers for the activities. The maximum fetch limit is `100`.
- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Activities](activities.md)
  A resource object that represents an activity curator.
- [object ActivitiesResponse](activitiesresponse.md)
  The response to a request for activities.
- [Get a Catalog Activity](get-a-catalog-activity.md)
  Fetch an activity by using its identifier.
- [Get a Catalog Activity's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-1eqct.md)
  Fetch an activity’s relationship by using its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-catalog-activities)*