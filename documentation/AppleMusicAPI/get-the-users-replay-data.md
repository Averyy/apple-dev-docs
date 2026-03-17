# Get the user's replay data

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch the user’s replay data for the latest eligible year.

**Availability**:
- Apple Music 1.0+

#### Discussion

A successful HTTP request returns music summaries for the most recent year that the user has enough listening history. If unsuccessful, the HTTP status code indicates the error, and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

## Endpoint

`GET https://api.music.apple.com/v1/me/music-summaries`

## Parameters

- `extend` ([string]): A list of attribute extensions applied to resources in the response.
- `filter[year]` ([string]) *(required)*: A filter applied to the request. The value is always `latest`.
- `include` ([string]): A list of relationship names to include for resouces in the response.
- `l` (string): The localization specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by the storefront. Otherwise, the storefront’s `defaultLanguageTag` is used.
- `views` ([string]): The views to activate for the music summaries resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-the-user's-replay-data)*