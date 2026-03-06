# Read the Xcode Cloud Product for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the Xcode Cloud product information for an app you build with Xcode Cloud.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below retrieves information about a specific Xcode Cloud product. Use the data provided in the response to read additional information; for example, workflow information.

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/6446998023/ciProduct
```

**Response**:

```json
{
    "data": {
        "type": "ciProducts",
        "id": "6446998023",
        "attributes": {
            "name": "Your Next Cortado",
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

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/ciProduct`

## Parameters

- `fields[ciProducts]` ([string]): Additional fields to include for each Products resource returned by the response.
- `fields[scmRepositories]` ([string]): Additional fields to include for each Products resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[primaryRepositories]` (integer): The number of included Products resources to return if the primary repositories relationship is included.
- `fields[apps]` ([string])
- `fields[bundleIds]` ([string])

## See Also

- [GET /v1/apps/{id}/relationships/ciProduct](get-v1-apps-_id_-relationships-ciproduct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-ciproduct)*