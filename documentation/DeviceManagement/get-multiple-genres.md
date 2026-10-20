# Get Multiple Genres

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetch metadata for genres from the catalog by using their identifiers.

**Availability**:
- VPP License Management 2.2+

#### Discussion

##### Example

**Request**:

```

```

**Response**:

```json

```

## Topics

### Responses
- [object GenresResponse](./genresresponse.md)
- [object UnauthorizedResponse](./unauthorizedresponse.md)
  A response that indicates an incorrect authorization header.
- [object ErrorsResponse](./errorsresponse.md)
  The collection of errors that occurred while processing the request.

## Endpoint

`GET https://api.ent.apple.com/v1/catalog/{storefront}/genres`

## Parameters

### Path Parameters

- `storefront` (string) *(required)*: An iTunes Store territory, specified by an ISO 3166 alpha-2 country code. The possible values are the `id` attributes of `Storefrontobjects`.

### Query Parameters

- `ids` ([string]) *(required)*: The unique identifiers for the genres.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.

## Responses

- `200` OK (`GenresResponse`, `application/json`): The request was successful.
- `401` Unauthorized (`UnauthorizedResponse`, `application/json`): A response indicating an incorrect `Authorization` header.
- `500` Internal Server Error (`ErrorsResponse`, `application/json`): A response indicating an error occurred on the server.

## See Also

### Fetching genres
- [Get a Genre](./get-a-genre.md)
  Fetch metadata for a genre from the catalog by using its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-multiple-genres)*