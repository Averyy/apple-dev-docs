# Get Catalog Search Results

**Framework**: Device Management  
**Kind**: httpRequest

Fetch metadata for apps and books from the catalog by using a search term.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

##### Example Request and Response

**Request**:

```None
?term=harry&platform=iphone&types=apps&filter[targetPlatform]=iphone,mac&filter[genre]=6014
```

**Response**:

```json
{
  "results": {
    "contents": [
      {
        "id": "623592465",
        "type": "apps",
        "href": "/v1/catalog/us/apps/623592465",
        "attributes": {
          "isVppDeviceBasedLicensingEnabled": true,
          "offers": [
            {
              "buyParams": "productType=C&price=1990&salableAdamId=623592465&pricingParameters=STDQ&pg=default&marketType=ENT&appExtVrsId=860907818",
              "type": "buy",
              "priceFormatted": "$1.99",
              "price": 1.99,
              "currencyCode": "USD",
              "assets": [
                {
                  "flavor": "iosSoftware",
                  "size": 207355904
                }
              ]
            }
          ],
          "isFirstPartyHideableApp": false,
          "contentRatingsBySystem": {
            "appsApple": {
              "name": "12+",
              "value": 300,
              "rank": 3,
              "advisories": [
                "Infrequent/Mild Alcohol, Tobacco, or Drug Use or References",
                "Infrequent/Mild Profanity or Crude Humor",
                "Infrequent/Mild Mature/Suggestive Themes"
              ]
            }
          },
          "deviceFamilies": [
            "iphone",
            "ipad",
            "ipod"
          ],
          "usesClassKit": false,
          "url": "https://apps.apple.com/us/app/heads-up/id623592465",
          "userRating": {
            "value": 4.9,
            "ratingCount": 1987
          },
          "isB2BCustomApp": false,
          "genreDisplayName": "Word",
          "name": "Heads Up!",
          "artistName": "Warner Bros.",
          "isIOSBinaryMacOSCompatible": false,
          "supportsDeviceSharing": false,
          "hasEula": false,
          "platformAttributes": {
            "ios": {
              "seller": "Warner Bros. Entertainment",
              "requiredCapabilitiesForRealityDevice": "arm64 gamekit metal ",
              "minimumMacOSVersion": "11.0",
              "minimumOSVersion": "13.0",
              "subtitle": "Play Charades with Friends!",
              "bundleId": "com.wb.Ellen.HeadsUp",
              "artwork": {
                "width": 1024,
                "height": 1024,
                "url": "https://isq11.mzstatic.com/image/thumb/Purple126/v4/71/b3/2a/71b32a24-34d2-7a89-ffba-8c252a140eb6/AppIconHalloween-0-0-1x_U007epad-0-85-220.png/{w}x{h}bb.{f}",
                "bgColor": "ffffff",
                "textColor1": "090000",
                "textColor2": "2e150b",
                "textColor3": "3a3333",
                "textColor4": "58443c"
              },
              "isVisionOSCompatible": false,
              "externalVersionId": 860907818,
              "minimumVisionOSVersion": "1.0",
              "requiredCapabilities": "arm64 gamekit metal "
            }
          }
        },
        "relationships": {
          "genres": {
            "href": "/v1/catalog/us/apps/623592465/genres",
            "data": [
              {
                "id": "6014",
                "type": "genres",
                "href": "/v1/catalog/us/genres/6014",
                "attributes": {
                  "parentName": "App Store",
                  "name": "Games",
                  "parentId": "36",
                  "url": "https://itunes.apple.com/us/genre/id6014"
                }
              },
              {
                "id": "6016",
                "type": "genres",
                "href": "/v1/catalog/us/genres/6016",
                "attributes": {
                  "parentName": "App Store",
                  "name": "Entertainment",
                  "parentId": "36",
                  "url": "https://itunes.apple.com/us/genre/id6016"
                }
              },
              {
                "id": "7019",
                "type": "genres",
                "href": "/v1/catalog/us/genres/7019",
                "attributes": {
                  "parentName": "Games",
                  "name": "Word",
                  "parentId": "6014",
                  "url": "https://itunes.apple.com/us/genre/id7019"
                }
              },
              {
                "id": "7005",
                "type": "genres",
                "href": "/v1/catalog/us/genres/7005",
                "attributes": {
                  "parentName": "Games",
                  "name": "Card",
                  "parentId": "6014",
                  "url": "https://itunes.apple.com/us/genre/id7005"
                }
              }
            ]
          }
        }
      }
    ]
  }
}

```

## Topics

### Responses
- [object ResultsResponse](resultsresponse.md)
  A response that contains the resource objects for the request.
- [object UnauthorizedResponse](unauthorizedresponse.md)
  A response that indicates an incorrect authorization header.
- [object ErrorsResponse](errorsresponse.md)
  The collection of errors that occurred while processing the request.

## Endpoint

`GET https://api.ent.apple.com/v1/catalog/{storefront}/search`

## Parameters

- `additionalPlatforms` ([string]): Additional platforms the app supports that you want to get metadata for.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response. These attributes are usually more expensive, so only extend them if absolutely necessary. Classifier (optional): A resource type to apply the parameter to, `apps` or `books`.
- `filter` ([string]): A filter to apply to the search results. Classifier (required): The filter type, `targetPlatforms` or `genre`. Possible values for `targetPlatforms` are the same as for the `platform` parameter, and the value for `genre` is a genre ID.
- `l` (string): The localization to use, which you specify with a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object that `storefront` specifies. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `platform` (string) *(required)*: The platform the user-facing app is running on. You use this to get apps metadata for the specified platform.
- `term` (string) *(required)*: The text for the search.
- `types` ([string]) *(required)*: The resource types to include in the search results. Possible values: `apps`, `books`

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-catalog-search-results)*