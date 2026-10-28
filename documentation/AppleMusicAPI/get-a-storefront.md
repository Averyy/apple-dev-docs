# Get a Storefront

**Framework**: Apple Music API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetch a single storefront by using its identifier.

**Availability**:
- Apple Music 1.0+

## Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains a single [`Storefronts`](./storefronts.md) object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

### Example

**Request**:

```
https://api.music.apple.com/v1/storefronts/jp
```

**Response**:

```json
{
    "data": [
        {
            "id": "jp",
            "type": "storefronts",
            "href": "/v1/storefronts/jp",
            "attributes": {
                "defaultLanguageTag": "ja",
                "name": "Japan",
                "explicitContentPolicy": "allowed",
                "supportedLanguageTags": [
                    "ja",
                    "en-US"
                ]
            }
        }
    ]
}


```

## Endpoint

`GET https://api.music.apple.com/v1/storefronts/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The identifier (an ISO 3166 alpha-2 country code) for the storefront you want to fetch.

### Query Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## Responses

- `200` OK (`StorefrontsResponse`, `application/json`): The request was successful.
- `401` Unauthorized (`UnauthorizedResponse`, `application/json`): A response indicating an incorrect `Authorization` header.
- `500` Internal Server Error (`ErrorsResponse`, `application/json`): A response indicating an error occurred on the server.

## See Also

### Related Documentation
- [object Storefronts](./storefronts.md)
  A resource object that represents a storefront, an Apple Music and iTunes Store territory that the content is available in.
- [object StorefrontsResponse](./storefrontsresponse.md)
  The response to a storefront request.
### Requesting a Catalog Storefront
- [Get Multiple Storefronts](./get-multiple-storefronts.md)
  Fetch one or more storefronts by using their identifiers.
- [Get All Storefronts](./get-all-storefronts.md)
  Fetch all the storefronts in alphabetical order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-storefront)*