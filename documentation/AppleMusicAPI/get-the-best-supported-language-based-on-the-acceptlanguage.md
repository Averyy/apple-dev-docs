# Get the best supported language for a storefront

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch the best supported language for a storefront from a list.

**Availability**:
- Apple Music 1.0+

#### Discussion

##### Example

**Request**:

```None
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

- `acceptLanguage` ([string]) *(required)*: A list of languages to accept.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-the-best-supported-language-based-on-the-acceptlanguage)*