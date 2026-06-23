# Get Metadata for a Catalog Book

**Framework**: Device Management  
**Kind**: httpRequest

Fetch metadata for a book from the catalog by using its identifier.

**Availability**:
- VPP License Management 2.2+

#### Discussion

##### Example Request and Response

**Request**:

```None
/book_id_123?platform=iphone
```

**Response**:

```json
{
  "data":[
    {
        "id": "book_id_123",
        "type": "books",
        "href": "/v1/catalog/us/books/book_id_123?l=en-US",
        "attributes": {
          "offers": [
            {
              "buyParams": "productType=PUB&price=13990&salableAdamId=book_id_123&pricingParameters=STDQ&pg=default&marketType=ENT",
              "type": "buy",
              "priceFormatted": "$13.99",
              "price": 13.99,
              "currencyCode": "USD",
              "assets": [
                {
                  "flavor": "publication",
                  "size": 98316906
                }
              ]
            }
          ],
          "genreNames": [
            "Art & Architecture",
            "Books",
            "Arts & Entertainment",
            "Health, Mind & Body",
            "Self-Improvement"
          ],
          "isbn": "123456789",
          "name": "A Very Famous Book",
          "artistName": "FamousAuthor",
          "artwork": {
            "width": 2213,
            "height": 2400,
            "url": "IMAGE_URL",
            "bgColor": "b7c2c4",
            "textColor1": "0e0c11",
            "textColor2": "301f1b",
            "textColor3": "303035",
            "textColor4": "4b403d"
          },
          "url": "https://books.apple.com/us/book/foo-bar/id123456",
          "userRating": {
            "value": 0,
            "ratingCount": 0
          }
        },
        "relationships": {
          "genres": {
            "href": "/v1/catalog/us/books/book_id_123/genres?l=en-US",
            "data": [
              {
                "id": "10002",
                "type": "genres",
                "href": "/v1/catalog/us/genres/10002?l=en-US",
                "attributes": {
                  "parentName": "Arts & Entertainment",
                  "name": "Art & Architecture",
                  "parentId": "9007",
                  "url": "https://itunes.apple.com/us/genre/id10002"
                }
              },
              {
                "id": "38",
                "type": "genres",
                "href": "/v1/catalog/us/genres/38?l=en-US",
                "attributes": {
                  "name": "Books",
                  "url": "https://itunes.apple.com/us/genre/id38"
                }
              }
            ]
          }
        }
      }
  ]
}

```

## Topics

### Responses
- [object BooksResponse](booksresponse.md)
  A response that contains the resource objects for the request.
- [object UnauthorizedResponse](unauthorizedresponse.md)
  A response that indicates an incorrect authorization header.
- [object ErrorsResponse](errorsresponse.md)
  The collection of errors that occurred while processing the request.

## Endpoint

`GET https://api.ent.apple.com/v1/catalog/{storefront}/books/{id}`

## Parameters

- `additionalPlatforms` ([string]): Additional platforms the app supports that you want to get metadata for.
- `include` ([string]): A list of relationship names to include for resources in the response. Classifier (optional): A resource type to apply the parameter to, `apps` or `books`.
- `l` (string): The localization to use, which you specify with a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object that `storefront` specifies. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `platform` (string) *(required)*: The platform the user-facing app is running on. You use this to get metadata for the specified platform.
- `relate` ([string]): A list of relationship names to relate for resources in the response. Classifier (optional): A resource type to apply the parameter to, `apps` or `books`.

## See Also

- [Get Metadata for Your Authenticated Purchases](get-v1-catalog-_storefront_-stoken-authenticated-purchases.md)
  Fetch metadata for your authenticated purchases by using their identifiers with a specified resource type.
- [Get Metadata for Your Apps](get-your-apps-metadata.md)
  Fetch metadata for your apps by using their identifiers.
- [Get Metadata for Your Books](get-your-books-metadata.md)
  Fetch metadata for your books by using their identifiers.
- [Get Metadata for a Catalog App](get-v1-catalog-_storefront_-apps-_id_.md)
  Fetch metadata for an app from the catalog by using its identifier.
- [Get Metadata for Multiple Catalog Apps](get-v1-catalog-_storefront_-apps.md)
  Fetch metadata for apps from the catalog by using their identifiers.
- [Get Metadata for Multiple Catalog Books](get-v1-catalog-_storefront_-books.md)
  Fetch metadata for books from the catalog by using their identifiers.
- [Get Catalog Search Results](get-catalog-search-results.md)
  Fetch metadata for apps, books, and subscriptions from the catalog by using a search term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-v1-catalog-_storefront_-books-_id_)*