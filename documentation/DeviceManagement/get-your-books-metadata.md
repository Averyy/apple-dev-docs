# Get Metadata for Your Books

**Framework**: Device Management  
**Kind**: httpRequest

Fetch metadata for your books by using their identifiers.

**Availability**:
- VPP License Management 2.1+

#### Discussion

##### Example Request and Response

**Request**:

```None
?ids=431617578&platform=iphone
```

**Response**:

```json
{
    "data": [
        {
            "attributes": {
                "artistName": "Walter Isaacson",
                "artwork": {
                "height": 2131,
                "url": "https://isq11.mzstatic.com/image/thumb/Publication4/v4/3f/33/b5/3f33b53e-78bb-5bb5-4007-09b5a1969842/9781451648553.jpg/{w}x{h}bb.{f}",
                "width": 1399
                },
                "genreNames": [
                    "Biographies & Memoirs",
                    "Books",
                    "Business & Personal Finance",
                    "Management & Leadership",
                    "Computers & Internet",
                    "Computers"
                ],
                "isbn": "9781451648553",
                "name": "Steve Jobs",
                "offers": [
                    {
                        "assets": [
                            {
                                "flavor": "publication",
                                "size": 27582389
                            }
                        ],
                        "buyParams":"productType=PUB&price=14990&salableAdamId=431617578&pricingParameters=STDQ&pg=default&marketType=ENT",
                        "currencyCode": "USD",
                        "price": 14.99,
                        "priceFormatted": "$14.99",
                        "type": "buy"
                    }
                ],
                "url": "https://books.apple.com/us/book/steve-jobs/id431617578",
                "userRating": {
                    "ratingCount": 10,
                    "value": 4.4
                }
            },
            "href": "/v1/catalog/us/books/431617578",
            "id": "431617578",
            "relationships": {
                "genres": {
                    "data": [
                        {
                            "attributes": {
                                "name": "Biographies & Memoirs",
                                "parentId": "38",
                                "parentName": "Books",
                                "url": "https://itunes.apple.com/us/genre/id9008"
                            },
                            "href": "/v1/catalog/us/genres/9008",
                            "id": "9008",
                            "type": "genres"
                        },
                        {
                            "attributes": {
                                "name": "Books",
                                "url": "https://itunes.apple.com/us/genre/id38"
                            },
                            "href": "/v1/catalog/us/genres/38",
                            "id": "38",
                            "type": "genres"
                        },
                        {
                            "attributes": {
                                "name": "Business & Personal Finance",
                                "parentId": "38",
                                "parentName": "Books",
                                "url": "https://itunes.apple.com/us/genre/id9009"
                            },
                            "href": "/v1/catalog/us/genres/9009",
                            "id": "9009",
                            "type": "genres"
                        },
                        {
                            "attributes": {
                                "name": "Management & Leadership",
                                "parentId": "9009",
                                "parentName": "Business & Personal Finance",
                                "url": "https://itunes.apple.com/us/genre/id10014"
                            },
                            "href": "/v1/catalog/us/genres/10014",
                            "id": "10014",
                            "type": "genres"
                        },
                        {
                            "attributes": {
                                "name": "Computers & Internet",
                                "parentId": "38",
                                "parentName": "Books",
                                "url": "https://itunes.apple.com/us/genre/id9027"
                            },
                            "href": "/v1/catalog/us/genres/9027",
                            "id": "9027",
                            "type": "genres"
                        },
                        {
                            "attributes": {
                                "name": "Computers",
                                "parentId": "9027",
                                "parentName": "Computers & Internet",
                                "url": "https://itunes.apple.com/us/genre/id10017"
                            },
                            "href": "/v1/catalog/us/genres/10017",
                            "id": "10017",
                            "type": "genres"
                        }
                    ],
                    "href": "/v1/catalog/us/books/431617578/genres"
                }
            },
            "type": "books"
        }
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

`GET https://api.ent.apple.com/v1/catalog/{storefront}/stoken-authenticated-books`

## Parameters

- `additionalPlatforms` ([string]): Additional platforms the app supports that you want to get metadata for.
- `ids` ([string]): The unique identifiers for the books.
- `l` (string): The localization to use, which you specify with a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object that `storefront` specifies. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `platform` (string) *(required)*: The platform the user-facing app is running on. You use this to get metadata for the specified platform.

## See Also

- [Get Metadata for Your Authenticated Purchases](get-v1-catalog-_storefront_-stoken-authenticated-purchases.md)
  Fetch metadata for your authenticated purchases by using their identifiers with a specified resource type.
- [Get Metadata for Your Apps](get-your-apps-metadata.md)
  Fetch metadata for your apps by using their identifiers.
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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-your-books-metadata)*