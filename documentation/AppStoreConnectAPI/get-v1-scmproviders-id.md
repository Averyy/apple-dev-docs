# Get a source code management provider

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific source code management provider you connected to Xcode Cloud.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below retrieves information about a specific source code management provider you connected to Xcode Cloud. Use the data provided in the response to read additional information; for example, repository information.

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/scmProviders/d1b5479e-ce72-402c-8b9a-ea26ef6773f4
```

**Response**:

```json
{
    "data": {
        "type": "scmProviders",
        "id": "d1b5479e-ce72-402c-8b9a-ea26ef6773f4",
        "attributes": {
            "scmProviderType": {
                "kind": "GITHUB_CLOUD",
                "displayName": "GitHub",
                "isOnPremise": false
            },
            "url": "github.com"
        },
        "relationships": {
            "repositories": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/scmProviders/d1b5479e-ce72-402c-8b9a-ea26ef6773f4/relationships/repositories",
                    "related": "https://api.appstoreconnect.apple.com/v1/scmProviders/d1b5479e-ce72-402c-8b9a-ea26ef6773f4/repositories"
                }
            }
        },
        "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/scmProviders/d1b5479e-ce72-402c-8b9a-ea26ef6773f4"
        }
    },
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/scmProviders/d1b5479e-ce72-402c-8b9a-ea26ef6773f4"
    }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/scmProviders/{id}`

## Parameters

- `fields[scmProviders]` ([string]): Additional fields to include for the Providers resource returned by the response.

## See Also

- [List all source code management providers](get-v1-scmproviders.md)
  List all source code management providers you connected to Xcode Cloud.
- [List all repositories for a source code management provider](get-v1-scmproviders-_id_-repositories.md)
  List all Git repositories for a specific source code management provider you connected to Xcode Cloud.
- [List repository IDs for an SCM provider](get-v1-scmproviders-_id_-relationships-repositories.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-scmproviders-_id_)*