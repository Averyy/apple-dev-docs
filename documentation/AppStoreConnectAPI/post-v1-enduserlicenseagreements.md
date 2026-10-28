# Create an end user license agreement

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Add a custom end user license agreement (EULA) to an app and configure the territories to which it applies.

**Availability**:
- App Store Connect API 1.2+

## Discussion

Use this endpoint to associate a custom license agreement with an app in the specified App Store territories. Any other territories will use the standard Apple-provided license agreement.

In the following example the request contains a blank value for the `agreementText` attribute. Replace that attribute value with your actual agreement text.

### Create a Custom License Agreement for USA and China

**Request**:

```
POST https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements

{
  "data": {
    "type": "endUserLicenseAgreements",
    "attributes": {
      "agreementText": "..."
    },
    "relationships": {
      "app": {
        "data": {
          "type": "apps",
          "id": "284993459"
        }
      },
      "territories": {
        "data": [
          {
            "type": "territories",
            "id": "USA"
          },
          {
            "type": "territories",
            "id": "CHN"
          }
        ]
      }
    }
  }
}
```

**Response**:

```json
{
  "data" : {
    "type" : "endUserLicenseAgreements",
    "id" : "b25d1669-d6b1-4e9b-8679-02863557222a",
    "attributes" : {
      "agreementText" : "..."
    },
    "relationships" : {
      "app" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/b25d1669-d6b1-4e9b-8679-02863557222a/relationships/app",
          "related" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/b25d1669-d6b1-4e9b-8679-02863557222a/app"
        }
      },
      "territories" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/b25d1669-d6b1-4e9b-8679-02863557222a/relationships/territories",
          "related" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/b25d1669-d6b1-4e9b-8679-02863557222a/territories"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/b25d1669-d6b1-4e9b-8679-02863557222a"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements"
  }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements`

## Request Body

**Content-Type**: `application/json`  
**Type**: `EndUserLicenseAgreementCreateRequest`

## Responses

- `201` Created (`EndUserLicenseAgreementResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Deleting an EULA
- [Modify an end user license agreement](./patch-v1-enduserlicenseagreements-_id_.md)
  Update the text or territories for your custom end user license agreement.
- [Delete an end user license agreement](./delete-v1-enduserlicenseagreements-_id_.md)
  Delete the custom end user license agreement that is associated with an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-enduserlicenseagreements)*