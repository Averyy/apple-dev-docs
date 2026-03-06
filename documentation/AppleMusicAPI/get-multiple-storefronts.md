# Get Multiple Storefronts

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more storefronts by using their identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains one or more [`Storefronts`](storefronts.md) objects. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

##### Example

**Request**:

```None
https://api.music.apple.com/v1/storefronts?ids=us,ca,cn,au,hk
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
                "explicitContentPolicy": "allowed",
                "defaultLanguageTag": "en-US",
                "name": "United States",
                "supportedLanguageTags": [
                    "en-US",
                    "es-MX",
                    "ar",
                    "ru",
                    "zh-Hans-CN"
                ]
            }
        },
        {
            "id": "ca",
            "type": "storefronts",
            "href": "/v1/storefronts/ca",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "defaultLanguageTag": "en-CA",
                "name": "Canada",
                "supportedLanguageTags": [
                    "en-CA",
                    "fr-CA"
                ]
            }
        },
        {
            "id": "cn",
            "type": "storefronts",
            "href": "/v1/storefronts/cn",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "defaultLanguageTag": "zh-Hans-CN",
                "name": "China mainland",
                "supportedLanguageTags": [
                    "zh-Hans-CN",
                    "en-GB"
                ]
            }
        },
        {
            "id": "au",
            "type": "storefronts",
            "href": "/v1/storefronts/au",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "defaultLanguageTag": "en-AU",
                "name": "Australia",
                "supportedLanguageTags": [
                    "en-AU",
                    "en-GB"
                ]
            }
        },
        {
            "id": "hk",
            "type": "storefronts",
            "href": "/v1/storefronts/hk",
            "attributes": {
                "explicitContentPolicy": "allowed",
                "defaultLanguageTag": "zh-Hant-HK",
                "name": "Hong Kong",
                "supportedLanguageTags": [
                    "zh-Hant-HK",
                    "en-GB",
                    "zh-Hant-TW"
                ]
            }
        }
    ]
}



```

## Endpoint

`GET https://api.music.apple.com/v1/storefronts`

## Parameters

- `ids` ([string]) *(required)*: A list of the identifiers (ISO 3166 alpha-2 country codes) for the storefronts you want to fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Storefronts](storefronts.md)
  A resource object that represents a storefront, an Apple Music and iTunes Store territory that the content is available in.
- [object StorefrontsResponse](storefrontsresponse.md)
  The response to a storefront request.
- [Get a Storefront](get-a-storefront.md)
  Fetch a single storefront by using its identifier.
- [Get All Storefronts](get-all-storefronts.md)
  Fetch all the storefronts in alphabetical order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-storefronts)*