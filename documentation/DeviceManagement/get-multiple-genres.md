# Get Multiple Genres

**Framework**: Device Management  
**Kind**: httpRequest

Fetch metadata for genres from the catalog by using their identifiers.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

##### Example

**Request**:

```None

```

**Response**:

```json

```

## Topics

### Responses
- [object GenresResponse](genresresponse.md)
- [object UnauthorizedResponse](unauthorizedresponse.md)
  A response that indicates an incorrect authorization header.
- [object ErrorsResponse](errorsresponse.md)
  The collection of errors that occurred while processing the request.

## Endpoint

`GET https://api.ent.apple.com/v1/catalog/{storefront}/genres`

## Parameters

- `ids` ([string]) *(required)*: The unique identifiers for the genres.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.

## See Also

- [Fetch a apps resource's relationship](fetch-a-apps-resource's-relationship.md)
- [Fetch a books resource's relationship](fetch-a-books-resource's-relationship.md)
- [Get a Genre](get-a-genre.md)
  Fetch metadata for a genre from the catalog by using its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-multiple-genres)*