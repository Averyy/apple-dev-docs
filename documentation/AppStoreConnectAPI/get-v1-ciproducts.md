# List All Xcode Cloud Products

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of all products you created in Xcode Cloud.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below lists ten Xcode Cloud products and sorts the list using the `latestBuildCreatedDate` attribute. Use the information provided in the response to display data about your Xcode Cloud products on a dashboard or to read additional information; for example, workflow information.

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/ciProducts?limit=10&sort=latestBuildCreatedDate
```

**Response**:

```json
{
    "data": [
        {
            "type": "ciProducts",
            "id": "cfdc7a3b-0fdf-4463-a0e7-cf9067557beb",
            "attributes": {
                "name": "My Product 5",
                "createdDate": "2021-08-17T18:11:04.616669Z",
                "productType": "APP"
            },
            "relationships": {
                "app": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/cfdc7a3b-0fdf-4463-a0e7-cf9067557beb/relationships/app",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/cfdc7a3b-0fdf-4463-a0e7-cf9067557beb/app"
                    }
                },
                "workflows": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/cfdc7a3b-0fdf-4463-a0e7-cf9067557beb/relationships/workflows",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/cfdc7a3b-0fdf-4463-a0e7-cf9067557beb/workflows"
                    }
                },
                "buildRuns": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/cfdc7a3b-0fdf-4463-a0e7-cf9067557beb/relationships/buildRuns",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/cfdc7a3b-0fdf-4463-a0e7-cf9067557beb/buildRuns"
                    }
                }
            },
            "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/cfdc7a3b-0fdf-4463-a0e7-cf9067557beb"
            }
        },
        {
            "type": "ciProducts",
            "id": "00c99dd4-fb26-41e7-9aa0-18859cf6d2f7",
            "attributes": {
                "name": "My Product 4",
                "createdDate": "2021-08-17T18:11:04.614927Z",
                "productType": "APP"
            },
            "relationships": {
                "app": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/00c99dd4-fb26-41e7-9aa0-18859cf6d2f7/relationships/app",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/00c99dd4-fb26-41e7-9aa0-18859cf6d2f7/app"
                    }
                },
                "workflows": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/00c99dd4-fb26-41e7-9aa0-18859cf6d2f7/relationships/workflows",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/00c99dd4-fb26-41e7-9aa0-18859cf6d2f7/workflows"
                    }
                },
                "buildRuns": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/00c99dd4-fb26-41e7-9aa0-18859cf6d2f7/relationships/buildRuns",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/00c99dd4-fb26-41e7-9aa0-18859cf6d2f7/buildRuns"
                    }
                }
            },
            "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/00c99dd4-fb26-41e7-9aa0-18859cf6d2f7"
            }
        },
        {
            "type": "ciProducts",
            "id": "9501b490-307c-46a5-abee-83ae612a7caf",
            "attributes": {
                "name": "My Product 3",
                "createdDate": "2021-08-17T18:11:04.613099Z",
                "productType": "APP"
            },
            "relationships": {
                "app": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/9501b490-307c-46a5-abee-83ae612a7caf/relationships/app",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/9501b490-307c-46a5-abee-83ae612a7caf/app"
                    }
                },
                "workflows": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/9501b490-307c-46a5-abee-83ae612a7caf/relationships/workflows",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/9501b490-307c-46a5-abee-83ae612a7caf/workflows"
                    }
                },
                "buildRuns": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/9501b490-307c-46a5-abee-83ae612a7caf/relationships/buildRuns",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/9501b490-307c-46a5-abee-83ae612a7caf/buildRuns"
                    }
                }
            },
            "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/9501b490-307c-46a5-abee-83ae612a7caf"
            }
        },
        {
            "type": "ciProducts",
            "id": "d529e42c-f19a-4552-be11-6d74d6211872",
            "attributes": {
                "name": "My Product 2",
                "createdDate": "2021-08-17T18:11:04.611258Z",
                "productType": "APP"
            },
            "relationships": {
                "app": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/d529e42c-f19a-4552-be11-6d74d6211872/relationships/app",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/d529e42c-f19a-4552-be11-6d74d6211872/app"
                    }
                },
                "workflows": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/d529e42c-f19a-4552-be11-6d74d6211872/relationships/workflows",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/d529e42c-f19a-4552-be11-6d74d6211872/workflows"
                    }
                },
                "buildRuns": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/d529e42c-f19a-4552-be11-6d74d6211872/relationships/buildRuns",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/d529e42c-f19a-4552-be11-6d74d6211872/buildRuns"
                    }
                }
            },
            "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/d529e42c-f19a-4552-be11-6d74d6211872"
            }
        },
        {
            "type": "ciProducts",
            "id": "986a7c7a-a336-4b29-b4ba-de7d3b396be9",
            "attributes": {
                "name": "My Product 1",
                "createdDate": "2021-08-17T18:11:04.609109Z",
                "productType": "APP"
            },
            "relationships": {
                "app": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/986a7c7a-a336-4b29-b4ba-de7d3b396be9/relationships/app",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/986a7c7a-a336-4b29-b4ba-de7d3b396be9/app"
                    }
                },
                "workflows": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/986a7c7a-a336-4b29-b4ba-de7d3b396be9/relationships/workflows",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/986a7c7a-a336-4b29-b4ba-de7d3b396be9/workflows"
                    }
                },
                "buildRuns": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/986a7c7a-a336-4b29-b4ba-de7d3b396be9/relationships/buildRuns",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciProducts/986a7c7a-a336-4b29-b4ba-de7d3b396be9/buildRuns"
                    }
                }
            },
            "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/ciProducts/986a7c7a-a336-4b29-b4ba-de7d3b396be9"
            }
        }
    ],
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/ciProducts?limit=10&sort=latestBuildCreatedDate"
    },
    "meta": {
        "paging": {
            "total": 5,
            "limit": 10
        }
    }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciProducts`

## Parameters

- `fields[ciProducts]` ([string]): Additional fields to include for each Products resource returned by the response.
- `fields[scmRepositories]` ([string]): Additional fields to include for each Products resource returned by the response.
- `filter[app]` ([string]): Filter the returned products using the ID of the related Apps resource.
- `filter[productType]` ([string]): Filter the returned products using the product type attribute.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The number of Products resources to return.
- `limit[primaryRepositories]` (integer): The number of included Products resources to return if the primary repositories relationship is included.
- `fields[apps]` ([string]): Additional fields to include for each Products resource returned by the response.

## See Also

- [Read Xcode Cloud Product Information](get-v1-ciproducts-_id_.md)
  Get information about a specific Xcode Cloud product.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-ciproducts)*