# Get the best supported language for a storefront

**Framework**: Apple Music API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetch the best supported language for a storefront from a list.

**Availability**:
- Apple Music 1.0+

#### Discussion

##### Example

**Request**:

```
https://api.music.apple.com/v1/language/us/tag?acceptLanguage=en-US
```

**Response**:

```json
{
    “results”: {
        “tag”: “en-US”
    }
}
```

## Endpoint

`GET https://api.music.apple.com/v1/language/{storefront}/tag`

## Parameters

### Path Parameters

- `storefront` (string) *(required)*: An iTunes Store territory, specified by an ISO 3166 alpha-2 country code. The possible values are the `id` attributes of `Storefront` objects.

### Query Parameters

- `acceptLanguage` ([string]) *(required)*: A list of languages to accept.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.

## Responses

- `200` OK (`LangageTagResponse`, `application/json`): The request was successful.
- `401` Unauthorized (`UnauthorizedResponse`, `application/json`): A response indicating an incorrect `Authorization` header.
- `500` Internal Server Error (`ErrorsResponse`, `application/json`): A response indicating an error occurred on the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-the-best-supported-language-based-on-the-acceptlanguage)*