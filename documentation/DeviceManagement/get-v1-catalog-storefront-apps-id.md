# Get Metadata for a Catalog App

**Framework**: Device Management  
**Kind**: httpRequest

Fetch metadata for an app from the catalog by using its identifier.

**Availability**:
- VPP License Management 2.2+

#### Discussion

##### Example Request and Response

**Request**:

```None
/app_id_123?platform=iphone
```

**Response**:

```json
{
  "data":[
    {
        "id": "app_id_123",
        "type": "apps",
        "href": "/v1/catalog/us/apps/app_id_123?l=en-US",
        "attributes": {
          "isVppDeviceBasedLicensingEnabled": true,
          "offers": [
            {
              "buyParams": "productType=C&price=0&salableAdamId=app_id_123&pricingParameters=STDQ&pg=default&marketType=ENT&appExtVrsId=861079254",
              "type": "get",
              "priceFormatted": "$0.00",
              "price": 0,
              "currencyCode": "USD",
              "assets": [
                {
                  "flavor": "iosSoftware",
                  "size": 415137792
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
                "Infrequent/Mild Cartoon or Fantasy Violence",
                "Infrequent/Mild Profanity or Crude Humor",
                "Infrequent/Mild Alcohol, Tobacco, or Drug Use or References",
                "Infrequent/Mild Sexual Content and Nudity",
                "Infrequent/Mild Mature/Suggestive Themes"
              ]
            }
          },
          "deviceFamilies": [
            "iphone",
            "ipad",
            "ipod"
          ],
          "url": "https://apps.apple.com/us/app/FooBarApp/idapp_id_123",
          "usesClassKit": false,
          "userRating": {
            "value": 3.6,
            "ratingCount": 8
          },
          "isB2BCustomApp": false,
          "genreDisplayName": "Entertainment",
          "name": "FooBarApp",
          "isIOSBinaryMacOSCompatible": false,
          "artistName": "Foo",
          "supportsDeviceSharing": false,
          "hasEula": false,
          "platformAttributes": {
            "ios": {
              "seller": "FooBarApp PTE. LTD.",
              "requiredCapabilitiesForRealityDevice": "arm64 ",
              "minimumMacOSVersion": "11.0",
              "isXROSCompatible": false,
              "minimumOSVersion": "11.0",
              "minimumXROSVersion": "1.0",
              "subtitle": "\u2063Videos, Music & Live Streams",
              "bundleId": "com.bundle.developer",
              "artwork": {
                "width": 1024,
                "height": 1024,
                "url": "IMAGE_URL",
                "bgColor": "000000",
                "textColor1": "ffffff",
                "textColor2": "25faf3",
                "textColor3": "cbcbcb",
                "textColor4": "1ec8c3"
              },
              "externalVersionId": 861079254,
              "requiredCapabilities": "arm64 "
            }
          }
        },
        "relationships": {
          "genres": {
            "href": "/v1/catalog/us/apps/app_id_123/genres?l=en-US",
            "data": [
              {
                "id": "6016",
                "type": "genres",
                "href": "/v1/catalog/us/genres/6016?l=en-US",
                "attributes": {
                  "parentName": "App Store",
                  "name": "Entertainment",
                  "parentId": "36",
                  "url": "https://itunes.apple.com/us/genre/id6016"
                }
              },
              {
                "id": "6008",
                "type": "genres",
                "href": "/v1/catalog/us/genres/6008?l=en-US",
                "attributes": {
                  "parentName": "App Store",
                  "name": "Photo & Video",
                  "parentId": "36",
                  "url": "https://itunes.apple.com/us/genre/id6008"
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

`GET https://api.ent.apple.com/v1/catalog/{storefront}/apps/{id}`

## Parameters

- `additionalPlatforms` ([string]): Additional platforms the app supports that you want to get metadata for.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response. These attributes are usually more expensive, so only extend them if absolutely necessary. Classifier (optional): A resource type to apply the parameter to, `apps` or `books`.
- `include` ([string]): A list of relationship names to include for resources in the response. Classifier (optional): A resource type to apply the parameter to, `apps` or `books`.
- `l` (string): The localization to use, which you specify with a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object that `storefront` specifies. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `platform` (string) *(required)*: The platform the user-facing app is running on. You use this to get metadata for the specified platform.
- `relate` ([string]): A list of relationship names to relate for resources in the response. Classifier (optional): A resource type to apply the parameter to.

## See Also

- [Get Metadata for Your Apps](get-your-apps-metadata.md)
  Fetch metadata for your apps by using their identifiers.
- [Get Metadata for Your Books](get-your-books-metadata.md)
  Fetch metadata for your books by using their identifiers.
- [Get Metadata for Multiple Catalog Apps](get-v1-catalog-_storefront_-apps.md)
  Fetch metadata for apps from the catalog by using their identifiers.
- [Get Metadata for a Catalog Book](get-v1-catalog-_storefront_-books-_id_.md)
  Fetch metadata for a book from the catalog by using its identifier.
- [Get Metadata for Multiple Catalog Books](get-v1-catalog-_storefront_-books.md)
  Fetch metadata for books from the catalog by using their identifiers.
- [Get Catalog Search Results](get-catalog-search-results.md)
  Fetch metadata for apps, books, and subscriptions from the catalog by using a search term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-v1-catalog-_storefront_-apps-_id_)*