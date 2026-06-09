# Create a Custom Product Page

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add a custom product page for your app.

**Availability**:
- App Store Connect API 1.7+

#### Discussion

##### Example Request and Response

**Request**:

```None
POST https://api.appstoreconnect.apple.com/v1/appCustomProductPages
{
  "data": {
    "type": "appCustomProductPages",
    "attributes": {
      "name": "Customer Product Page 1"
    },
    "relationships": {
      "app": {
        "data": {
          "type": "apps",
          "id": "01234"
        }
      },
      "appStoreVersionTemplate": {
        "data": {
          "type": "appStoreVersions",
          "id": "3b439e1a-5647-4734-9378-5e0b2b82ccb4"
        }
      },
      "appCustomProductPageVersions": {
        "data": [
          {
            "type": "appCustomProductPageVersions",
            "id": "${new-appCustomProductPageVersion-id}"
          }
        ]
      }
    }
  },
  "included": [
    {
      "type": "appCustomProductPageVersions",
      "id": "${new-appCustomProductPageVersion-id}",
      "relationships": {
        "appCustomProductPage": {},
        "appCustomProductPageLocalizations": {
          "data": [
            {
              "type": "appCustomProductPageLocalizations",
              "id": "${new-appCustomProductPageLocalization-id}"
            }
          ]
        }
      }
    },
    {
      "type": "appCustomProductPageLocalizations",
      "id": "${new-appCustomProductPageLocalization-id}",
      "attributes": {
        "locale": "en-US",
        "promotionalText": "This app will really excite!"
      }
    }
  ]
}
```

**Response**:

```json
{
  "data": {
    "type": "appCustomProductPages",
    "id": "eb2b3606-2fef-4aab-a54e-b2e5547c9bc3",
    "attributes": {
      "name": "Customer Product Page 1",
      "url": "https://apps.apple.com/us/app/gersey-numba/id1526908970?ppid=eb2b3606-2fef-4aab-a54e-b2e5547c9bc3",
      "visible": true
    },
    "relationships": {
      "appCustomProductPageVersions": {
        "meta": {
          "paging": {
            "total": 1,
            "limit": 10
          }
        },
        "data": [
          {
            "type": "appCustomProductPageVersions",
            "id": "c7eadc0b-48d9-48c4-bdb2-109dd94a793a"
          }
        ],
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPages/eb2b3606-2fef-4aab-a54e-b2e5547c9bc3/relationships/appCustomProductPageVersions",
          "related": "https://api.appstoreconnect.apple.com/v1/appCustomProductPages/eb2b3606-2fef-4aab-a54e-b2e5547c9bc3/appCustomProductPageVersions"
        }
      }
    },
    "links": {
      "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPages/eb2b3606-2fef-4aab-a54e-b2e5547c9bc3"
    }
  },
  "included": [
    {
      "type": "appCustomProductPageVersions",
      "id": "c7eadc0b-48d9-48c4-bdb2-109dd94a793a",
      "attributes": {
        "version": "1",
        "state": "PREPARE_FOR_SUBMISSION"
      },
      "relationships": {
        "appCustomProductPageLocalizations": {
          "meta": {
            "paging": {
              "total": 1,
              "limit": 10
            }
          },
          "data": [
            {
              "type": "appCustomProductPageLocalizations",
              "id": "1a0e5f2a-938a-400d-935c-7bb7c6b3476a"
            }
          ],
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageVersions/c7eadc0b-48d9-48c4-bdb2-109dd94a793a/relationships/appCustomProductPageLocalizations",
            "related": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageVersions/c7eadc0b-48d9-48c4-bdb2-109dd94a793a/appCustomProductPageLocalizations"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageVersions/c7eadc0b-48d9-48c4-bdb2-109dd94a793a"
      }
    },
    {
      "type": "appCustomProductPageLocalizations",
      "id": "1a0e5f2a-938a-400d-935c-7bb7c6b3476a",
      "attributes": {
        "locale": "en-US",
        "promotionalText": "This app will really excite!"
      },
      "relationships": {
        "appScreenshotSets": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/1a0e5f2a-938a-400d-935c-7bb7c6b3476a/relationships/appScreenshotSets",
            "related": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/1a0e5f2a-938a-400d-935c-7bb7c6b3476a/appScreenshotSets"
          }
        },
        "appPreviewSets": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/1a0e5f2a-938a-400d-935c-7bb7c6b3476a/relationships/appPreviewSets",
            "related": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/1a0e5f2a-938a-400d-935c-7bb7c6b3476a/appPreviewSets"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/1a0e5f2a-938a-400d-935c-7bb7c6b3476a"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPages"
  }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appCustomProductPages`

## See Also

- [Modify an App Custom Product Page](patch-v1-appcustomproductpages-_id_.md)
  Update the name and visibility status of an app custom product page.
- [List All Custom Product Pages for an App](get-v1-apps-_id_-appcustomproductpages.md)
  Get a list of all custom product pages for a specific app.
- [Read Custom Product Page Information](get-v1-appcustomproductpages-_id_.md)
  Get information about a specific app custom product page.
- [List Custom Product Page Versions](get-v1-appcustomproductpages-_id_-appcustomproductpageversions.md)
  List the versions for a custom product page version.
- [Get all version ids for an app custom product page](get-v1-appcustomproductpages-_id_-relationships-appcustomproductpageversions.md)
  Get a list of custom product page version IDs associated with a custom product page.
- [Delete an App Custom Product Page](delete-v1-appcustomproductpages-_id_.md)
  Delete metadata that you configured for a custom product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appcustomproductpages)*