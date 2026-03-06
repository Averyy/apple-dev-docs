# Read Xcode Cloud Product Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific Xcode Cloud product.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below retrieves information about a specific Xcode Cloud product. Use the data provided in the response to read additional information; for example, workflow information.

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.comv1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469
```

**Response**:

```json
{
    "data": {
        "type": "ciProducts",
        "id": "1987a0d5-a64d-4799-b7d2-a9135ffca469",
        "attributes": {
            "name": "test-ac822ba6-97a1-4a4f-84f3-4b80a71150fc",
            "createdDate": "2021-08-17T18:02:43.097Z",
            "productType": "APP"
        },
        "relationships": {
            "app": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/relationships/app",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/app"
                }
            },
            "workflows": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/relationships/workflows",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/workflows"
                }
            },
            "primaryRepositories": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/relationships/primaryRepositories",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/primaryRepositories"
                }
            },
            "additionalRepositories": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/relationships/additionalRepositories",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/additionalRepositories"
                }
            },
            "buildRuns": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/relationships/buildRuns",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469/buildRuns"
                }
            }
        },
        "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469"
        }
    },
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/1987a0d5-a64d-4799-b7d2-a9135ffca469"
    }
}


```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciProducts/{id}`

## Parameters

- `fields[ciProducts]` ([string]): Additional fields to include for each Products resource returned by the response.
- `fields[scmRepositories]` ([string]): Additional fields to include for each Products resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[primaryRepositories]` (integer): The number of included Products resources to return if the primary repositories relationship is included.
- `fields[apps]` ([string]): Additional fields to include for each Products resource returned by the response.

## See Also

- [List All Xcode Cloud Products](get-v1-ciproducts.md)
  Get a list of all products you created in Xcode Cloud.
- [List All Additional Repositories for an Xcode Cloud Product](get-v1-ciproducts-_id_-additionalrepositories.md)
  List all additional Git repositories you associated with an Xcode Cloud product.
- [GET /v1/ciProducts/{id}/relationships/additionalRepositories](get-v1-ciproducts-_id_-relationships-additionalrepositories.md)
- [Read App Information for an Xcode Cloud Product](get-v1-ciproducts-_id_-app.md)
  Get the app in App Store Connect that’s related to an Xcode Cloud product.
- [GET /v1/ciProducts/{id}/relationships/app](get-v1-ciproducts-_id_-relationships-app.md)
- [List All Xcode Cloud Builds for an Xcode Cloud Product](get-v1-ciproducts-_id_-buildruns.md)
  List all builds Xcode Cloud performed for a specific product.
- [GET /v1/ciProducts/{id}/relationships/buildRuns](get-v1-ciproducts-_id_-relationships-buildruns.md)
- [List All Primary Git Repositories for an Xcode Cloud Product](get-v1-ciproducts-_id_-primaryrepositories.md)
  List all primary Git repositories for a specific Xcode Cloud product.
- [GET /v1/ciProducts/{id}/relationships/primaryRepositories](get-v1-ciproducts-_id_-relationships-primaryrepositories.md)
- [List All Workflows for an Xcode Cloud Product](get-v1-ciproducts-_id_-workflows.md)
  List all workflows for a specific Xcode Cloud product.
- [GET /v1/ciProducts/{id}/relationships/workflows](get-v1-ciproducts-_id_-relationships-workflows.md)
- [Read the Xcode Cloud Product for an App](get-v1-apps-_id_-ciproduct.md)
  Get the Xcode Cloud product information for an app you build with Xcode Cloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-ciproducts-_id_)*