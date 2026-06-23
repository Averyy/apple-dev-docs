# Get Metadata for Your Authenticated Purchases

**Framework**: Device Management  
**Kind**: httpRequest

Fetch metadata for your authenticated purchases by using their identifiers with a specified resource type.

**Availability**:
- VPP License Management 2.2+

#### Discussion

##### Example Request and Response

**Request**:

```None
?ids[apps]=1234&ids[books]=5678&ids[in-apps]=9012&platform=web
```

**Response**:

```json
{
"data": [
  { "id": "1234", "type": "apps",    "href": "/v1/catalog/us/apps/1234",    "attributes": { "…": "…" } },
  { "id": "5678", "type": "books",   "href": "/v1/catalog/us/books/5678",   "attributes": { "…": "…" } },
  { "id": "9012", "type": "in-apps", "href": "/v1/catalog/us/in-apps/9012",  "attributes": { "…": "…" } }
]
}
```

## Topics

### Responses
- [object ResourceCollectionResponse](resourcecollectionresponse.md)
  A response that contains the resource objects for the request.
- [object UnauthorizedResponse](unauthorizedresponse.md)
  A response that indicates an incorrect authorization header.
- [object ErrorsResponse](errorsresponse.md)
  The collection of errors that occurred while processing the request.

## Endpoint

`GET https://api.ent.apple.com/v1/catalog/{storefront}/stoken-authenticated-purchases`

## Parameters

- `extend` ([string]): A list of attribute extensions to apply to resources in the response. These attributes are usually more expensive, so only extend them if absolutely necessary. Classifier (optional): A resource type to apply the parameter to, `apps`, `books`, or `in-apps`.
- `ids` ([string]) *(required)*: The unique identifiers for the purchases. Classifier (required): The resource type of the purchase, `apps`, `books`, or `in-apps`.
- `include` ([string]): A list of relationship names to include for resources in the response. Classifier (optional): A resource type to apply the parameter to.
- `l` (string): The localization to use, which you specify with a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object that `storefront` specifies. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `relate` ([string]): A list of relationship names to relate for resources in the response. Classifier (optional): A resource type to apply the parameter to.

## See Also

- [Get Metadata for Your Apps](get-your-apps-metadata.md)
  Fetch metadata for your apps by using their identifiers.
- [Get Metadata for Your Books](get-your-books-metadata.md)
  Fetch metadata for your books by using their identifiers.
- [Get Metadata for a Catalog App](get-v1-catalog-_storefront_-apps-_id_.md)
  Fetch metadata for an app from the catalog by using its identifier.
- [Get Metadata for Multiple Catalog Apps](get-v1-catalog-_storefront_-apps.md)
  Fetch metadata for apps from the catalog by using their identifiers.
- [Get Metadata for a Catalog Book](get-v1-catalog-_storefront_-books-_id_.md)
  Fetch metadata for a book from the catalog by using its identifier.
- [Get Metadata for Multiple Catalog Books](get-v1-catalog-_storefront_-books.md)
  Fetch metadata for books from the catalog by using their identifiers.
- [Get Catalog Search Results](get-catalog-search-results.md)
  Fetch metadata for apps, books, and subscriptions from the catalog by using a search term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-v1-catalog-_storefront_-stoken-authenticated-purchases)*