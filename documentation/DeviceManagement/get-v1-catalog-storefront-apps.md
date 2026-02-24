# Get Metadata for Multiple Catalog Apps

**Framework**: Device Management  
**Kind**: httpRequest

Fetch metadata for apps from the catalog by using their identifiers.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

##### Example Request and Response

**Request**:

```None
?ids=623592465,363556704&platform=iphone
```

**Response**:

```json
{
  "data": [
    {
      "id": "623592465",
      "type": "apps",
      "href": "/v1/catalog/us/apps/623592465",
      "attributes": {
        "isVppDeviceBasedLicensingEnabled": true,
        "offers": [
          {
            "buyParams": "productType=C&price=1990&salableAdamId=623592465&pricingParameters=STDQ&pg=default&marketType=EDU&appExtVrsId=860907818",
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
          },
          {
            "pricePerUnitFormatted": "$1.99",
            "buyParams": "productType=C&price=39800&salableAdamId=623592465&pricingParameters=STDQ&pg=default&marketType=EDU&appExtVrsId=860907818",
            "quantity": 20,
            "pricePerUnit": 1.99,
            "currencyCode": "USD",
            "type": "buy",
            "priceFormatted": "$39.80",
            "assets": [
              {
                "flavor": "iosSoftware",
                "size": 207355904
              }
            ],
            "price": 39.8
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
        "name": "app name 1",
        "genreDisplayName": "Word",
        "artistName": "artist",
        "isIOSBinaryMacOSCompatible": false,
        "supportsDeviceSharing": false,
        "hasEula": false,
        "platformAttributes": {
          "ios": {
            "requiredCapabilitiesForRealityDevice": "arm64 gamekit metal ",
            "seller": "company",
            "minimumMacOSVersion": "11.0",
            "minimumOSVersion": "13.0",
            "subtitle": "subtitle",
            "bundleId": "com.bundle.id",
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
            "minimumVisionOSVersion": "1.0",
            "externalVersionId": 860907818,
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
    },
    {
      "id": "363556704",
      "type": "apps",
      "href": "/v1/catalog/us/apps/363556704",
      "attributes": {
        "isVppDeviceBasedLicensingEnabled": true,
        "offers": [
          {
            "buyParams": "productType=C&price=27990&salableAdamId=363556704&pricingParameters=STDQ&pg=default&marketType=EDU&appExtVrsId=865697157",
            "type": "buy",
            "priceFormatted": "$27.99",
            "price": 27.99,
            "currencyCode": "USD",
            "assets": [
              {
                "flavor": "iosSoftware",
                "size": 81773568
              }
            ]
          },
          {
            "pricePerUnitFormatted": "$27.99",
            "buyParams": "productType=C&price=559800&salableAdamId=363556704&pricingParameters=STDQ&pg=default&marketType=EDU&appExtVrsId=865697157",
            "quantity": 20,
            "pricePerUnit": 27.99,
            "currencyCode": "USD",
            "type": "buy",
            "priceFormatted": "$559.80",
            "assets": [
              {
                "flavor": "iosSoftware",
                "size": 81773568
              }
            ],
            "price": 559.8
          }
        ],
        "isFirstPartyHideableApp": false,
        "contentRatingsBySystem": {
          "appsApple": {
            "name": "4+",
            "value": 100,
            "rank": 1
          }
        },
        "deviceFamilies": [
          "watch",
          "iphone",
          "ipad",
          "ipod"
        ],
        "usesClassKit": false,
        "url": "url",
        "userRating": {
          "value": 0,
          "ratingCount": 0
        },
        "watchBundleId": "com.watch.bundle",
        "isB2BCustomApp": false,
        "name": "app2",
        "genreDisplayName": "Sports",
        "artistName": "artist",
        "isIOSBinaryMacOSCompatible": false,
        "supportsDeviceSharing": false,
        "hasEula": false,
        "platformAttributes": {
          "ios": {
            "requiredCapabilitiesForRealityDevice": "accelerometer arm64 gamekit location-services wifi ",
            "seller": "seller",
            "minimumMacOSVersion": "11.0",
            "minimumOSVersion": "12.0",
            "bundleId": "com.bundle.id",
            "artwork": {
              "width": 1024,
              "height": 1024,
              "url": "https://isq11.mzstatic.com/image/thumb/Purple221/v4/4d/f2/5b/4df25b59-eace-40b1-7a88-d0882780fe41/AppIcon-0-0-1x_U007emarketing-0-7-0-0-85-220.png/{w}x{h}bb.{f}",
              "bgColor": "e9e9e9",
              "textColor1": "000000",
              "textColor2": "4a0000",
              "textColor3": "2f2f2f",
              "textColor4": "6a2e2e"
            },
            "isVisionOSCompatible": false,
            "externalVersionId": 865697157,
            "requiredCapabilities": "accelerometer arm64 gamekit location-services wifi "
          }
        }
      },
      "relationships": {
        "genres": {
          "href": "/v1/catalog/us/apps/363556704/genres",
          "data": [
            {
              "id": "6004",
              "type": "genres",
              "href": "/v1/catalog/us/genres/6004",
              "attributes": {
                "parentName": "App Store",
                "name": "Sports",
                "parentId": "36",
                "url": "https://itunes.apple.com/us/genre/id6004"
              }
            },
            {
              "id": "6010",
              "type": "genres",
              "href": "/v1/catalog/us/genres/6010",
              "attributes": {
                "parentName": "App Store",
                "name": "Navigation",
                "parentId": "36",
                "url": "https://itunes.apple.com/us/genre/id6010"
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
- [object AppsResponse](appsresponse.md)
  A response that contains the resource objects for the request.
- [object UnauthorizedResponse](unauthorizedresponse.md)
  A response that indicates an incorrect authorization header.
- [object ErrorsResponse](errorsresponse.md)
  The collection of errors that occurred while processing the request.

## Endpoint

`GET https://api.ent.apple.com/v1/catalog/{storefront}/apps#ids`

## Parameters

- `additionalPlatforms` ([string]): Additional platforms the app supports that you want to get metadata for.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response. These attributes are usually more expensive, so only extend them if absolutely necessary. Classifier (optional): A resource type to apply the parameter to, `apps` or `books`.
- `ids` ([string]) *(required)*: The unique identifiers for the catalog apps. The maximum fetch limit is 100.
- `include` ([string]): A list of relationship names to include for resources in the response. Classifier (optional): A resource type to apply the parameter to, `apps` or `books`.
- `l` (string): The localization to use, which you specify with a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object that `storefront` specifies. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `platform` (string) *(required)*: The platform the user-facing app is running on. You use this to get metadata for the specified platform.
- `relate` ([string]): A list of relationship names to relate for resources in the response. Classifier (optional): A resource type to apply the parameter to, `apps` or `books`.

## See Also

- [Get Metadata for Your Apps](get-your-apps-metadata.md)
  Fetch metadata for your apps by using their identifiers.
- [Get Metadata for Your Books](get-your-books-metadata.md)
  Fetch metadata for your books by using their identifiers.
- [Get Metadata for a Catalog App](get-v1-catalog-_storefront_-apps-_id_.md)
  Fetch metadata for an app from the catalog by using its identifier.
- [Get Metadata for a Catalog Book](get-v1-catalog-_storefront_-books-_id_.md)
  Fetch metadata for a book from the catalog by using its identifier.
- [Get Metadata for Multiple Catalog Books](get-v1-catalog-_storefront_-books.md)
  Fetch metadata for books from the catalog by using their identifiers.
- [Get Catalog Search Results](get-catalog-search-results.md)
  Fetch metadata for apps and books from the catalog by using a search term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-v1-catalog-_storefront_-apps)*