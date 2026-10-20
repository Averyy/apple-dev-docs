# Modify an app info

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the App Store categories and sub-categories for your app.

**Availability**:
- App Store Connect API 1.2+

#### Discussion

Use this endpoint to modify the primary and secondary categories and subcategories for an app.

##### Add an App to the Games Category and the Sports and Role Playing Subcategories

**Request**:

```
PATCH https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4

{
  "data": {
    "type": "appInfos",
    "id": "61d77dc2-9313-4330-b169-d179277ccfc4",
    "relationships": {
      "primaryCategory": {
        "data": {
          "type": "appCategories",
          "id": "GAMES"
        }
      },
      "primarySubcategoryOne": {
        "data": {
          "type": "appCategories",
          "id": "GAMES_SPORTS"
        }
      },
      "primarySubcategoryTwo": {
        "data": {
          "type": "appCategories",
          "id": "GAMES_ROLE_PLAYING"
        }
      }
    }
  }
}

```

**Response**:

```json
{
  "data": {
    "type": "appInfos",
    "id": "61d77dc2-9313-4330-b169-d179277ccfc4",
    "attributes": {
      "appStoreState": "READY_FOR_SALE",
      "appStoreAgeRating": "TWELVE_PLUS",
      "brazilAgeRating": "FOURTEEN",
      "kidsAgeBand": null
    },
    "relationships": {
      "app": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4/relationships/app",
          "related": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4/app"
        }
      },
      "appInfoLocalizations": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4/relationships/appInfoLocalizations",
          "related": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4/appInfoLocalizations"
        }
      },
      "primaryCategory": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4/relationships/primaryCategory",
          "related": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4/primaryCategory"
        }
      },
      "primarySubcategoryOne": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4/relationships/primarySubcategoryOne",
          "related": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4/primarySubcategoryOne"
        }
      },
      "primarySubcategoryTwo": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4/relationships/primarySubcategoryTwo",
          "related": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4/primarySubcategoryTwo"
        }
      },
      "secondaryCategory": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4/relationships/secondaryCategory",
          "related": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4/secondaryCategory"
        }
      },
      "secondarySubcategoryOne": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4/relationships/secondarySubcategoryOne",
          "related": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4/secondarySubcategoryOne"
        }
      },
      "secondarySubcategoryTwo": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4/relationships/secondarySubcategoryTwo",
          "related": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4/secondarySubcategoryTwo"
        }
      }
    },
    "links": {
      "self": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4"
    }
  },
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/appInfos/61d77dc2-9313-4330-b169-d179277ccfc4"
  }
}

```

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appInfos/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `appInfo` resource ID from the [`List all app infos for an app`](./get-v1-apps-_id_-appinfos.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AppInfoUpdateRequest`

The request body you use to update an App Info.

## Responses

- `200` OK (`AppInfoResponse`, `application/json`): Request succeeded.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appinfos-_id_)*