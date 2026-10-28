# Get the user's replay data

**Framework**: Apple Music API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetch the user’s replay data for the latest eligible year.

**Availability**:
- Apple Music 1.0+

## Discussion

A successful HTTP request returns music summaries for the most recent year that the user has enough listening history. If unsuccessful, the HTTP status code indicates the error, and the details are in the `errors` array. For more information, see [Handling Requests and Responses](./handling-requests-and-responses.md).

## Endpoint

`GET https://api.music.apple.com/v1/me/music-summaries`

## Parameters

### Query Parameters

- `extend` ([string]): A list of attribute extensions applied to resources in the response.
- `filter[year]` ([string]) *(required)*: A filter applied to the request. The value is always `latest`.
- `include` ([string]): A list of relationship names to include for resouces in the response.
- `l` (string): The localization specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by the storefront. Otherwise, the storefront’s `defaultLanguageTag` is used.
- `views` ([string]): The views to activate for the music summaries resource.

  **Allowed Values**: `top-artists`, `top-albums`, `top-songs`

## Responses

- `200` OK (`MusicSummariesResponse`, `application/json`): The request was successful.
- `401` Unauthorized (`UnauthorizedResponse`, `application/json`): A response indicating an incorrect `Authorization` header.
- `403` Forbidden (`ForbiddenResponse`, `application/json`): A response indicating invalid or insufficient authentication.
- `500` Internal Server Error (`ErrorsResponse`, `application/json`): A response indicating an error occurred on the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-the-user's-replay-data)*