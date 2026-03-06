# Read Xcode Cloud Workflow Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific Xcode Cloud workflow.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below accesses information about an Xcode Cloud workflow. Display the workflow data provided in the response on a dashboard or use it to read additional information; for example, detailed data about builds Xcode Cloud performed.

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/ciWorkflows/3fa0575f-4de0-44cb-bf0f-9aa2651c2f1f
```

**Response**:

```json
{
    "data": {
        "type": "ciWorkflows",
        "id": "3fa0575f-4de0-44cb-bf0f-9aa2651c2f1f",
        "attributes": {
            "name": "My Workflow",
            "description": "",
            "branchStartCondition": {
                "source": {
                    "isAllMatch": false,
                    "patterns": [
                        {
                            "pattern": "main",
                            "isPrefix": false
                        }
                    ]
                },
                "filesAndFoldersRule": {
                    "mode": "START_IF_ANY_FILE_MATCHES",
                    "matchers": []
                },
                "autoCancel": true
            },
            "tagStartCondition": null,
            "pullRequestStartCondition": null,
            "scheduledStartCondition": null,
            "actions": [
                {
                    "name": "Archive iOS",
                    "actionType": "ARCHIVE",
                    "destination": null,
                    "buildDistributionAudience": null,
                    "testConfiguration": null,
                    "scheme": "MyApp",
                    "platform": "IOS",
                    "isRequiredToPass": true
                }
            ],
            "isEnabled": true,
            "isLockedForEditing": false,
            "clean": false,
            "containerFilePath": "MyXcodeProject.xcodeproj",
            "lastModifiedDate": null
        },
        "relationships": {
            "product": {
                "data": {
                    "type": "ciProducts",
                    "id": "8ca28eb1-2948-4848-813b-07c500665157"
                }
            },
            "repository": {
                "data": {
                    "type": "scmRepositories",
                    "id": "195430ae-7262-4b24-abd2-cbb6891feab8"
                },
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciWorkflows/3fa0575f-4de0-44cb-bf0f-9aa2651c2f1f/relationships/repository",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciWorkflows/3fa0575f-4de0-44cb-bf0f-9aa2651c2f1f/repository"
                }
            },
            "xcodeVersion": {
                "data": {
                    "type": "ciXcodeVersions",
                    "id": "Xcode12E507:stable"
                }
            },
            "macOsVersion": {
                "data": {
                    "type": "ciMacOsVersions",
                    "id": "20G95"
                }
            },
            "buildRuns": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciWorkflows/3fa0575f-4de0-44cb-bf0f-9aa2651c2f1f/relationships/buildRuns",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciWorkflows/3fa0575f-4de0-44cb-bf0f-9aa2651c2f1f/buildRuns"
                }
            }
        },
        "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/ciWorkflows/3fa0575f-4de0-44cb-bf0f-9aa2651c2f1f"
        }
    },
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/ciWorkflows/3fa0575f-4de0-44cb-bf0f-9aa2651c2f1f?include=macOsVersion%2Cproduct%2Crepository%2CxcodeVersion"
    }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciWorkflows/{id}`

## Parameters

- `fields[ciWorkflows]` ([string]): Additional fields to include for the Workflows resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `fields[scmRepositories]` ([string]): Additional fields to include for the Workflows resource returned by the response.

## See Also

- [List All Xcode Cloud Builds for a Workflow](get-v1-ciworkflows-_id_-buildruns.md)
  List all builds Xcode Cloud performed for a specific workflow.
- [Read the Repository Information for an Xcode Cloud Workflow](get-v1-ciworkflows-_id_-repository.md)
  Get information about the Git repository of a specific Xcode Cloud workflow.
- [GET /v1/ciWorkflows/{id}/relationships/buildRuns](get-v1-ciworkflows-_id_-relationships-buildruns.md)
- [GET /v1/ciWorkflows/{id}/relationships/repository](get-v1-ciworkflows-_id_-relationships-repository.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-ciworkflows-_id_)*