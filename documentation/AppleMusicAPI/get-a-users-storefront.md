# Get a User's Storefront

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a storefront for a specific user.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains a single [`Storefronts`](storefronts.md) object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/storefront
```

**Response**:

```json
{
    "data": [
        {
            "id": "us",
            "type": "storefronts",
            "href": "/v1/storefronts/us",
            "attributes": {
                "supportedLanguageTags": [
                    "en-US",
                    "es-MX",
                    "ar",
                    "ru",
                    "zh-Hans-CN"
                ],
                "defaultLanguageTag": "en-US",
                "name": "United States",
                "explicitContentPolicy": "allowed"
            }
        }
    ]
}

```

## Endpoint

`GET https://api.music.apple.com/v1/me/storefront`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `include` ([string]): Additional relationships to include in the fetch.
- `offset` (string): The offset to use for a paginated request. See [`Fetching Resources by Page`](fetching-resources-by-page.md).
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Storefronts](storefronts.md)
  A resource object that represents a storefront, an Apple Music and iTunes Store territory that the content is available in.
- [object StorefrontsResponse](storefrontsresponse.md)
  The response to a storefront request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-user's-storefront)*