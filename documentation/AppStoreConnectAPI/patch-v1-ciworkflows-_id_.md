# Update an xcode cloud workflow

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Make changes to an Xcode Cloud workflow.

**Availability**:
- App Store Connect API 1.5+

## Discussion

The example request below updates the name of an existing Xcode Cloud workflow. For a successful update, the response includes detailed information about the workflow. Use it to access additional information, start a new build, and so on.

### Example Request and Response

**Request**:

```
PATCH https://api.appstoreconnect.apple.com/v1/ciWorkflows/3fa0575f-4de0-44cb-bf0f-9aa2651c2f1f

{
    "data": {
        "type": "ciWorkflows",
        "id": "3fa0575f-4de0-44cb-bf0f-9aa2651c2f1f",
        "attributes": {
            "name": "A new name for an existing workflow."
        }
    }
}
```

**Response**:

```json
{
    "data": {
        "type": "ciWorkflows",
        "id": "3fa0575f-4de0-44cb-bf0f-9aa2651c2f1f",
        "attributes": {
            "name": "A new name for an existing workflow.",
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
            "repository": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciWorkflows/3fa0575f-4de0-44cb-bf0f-9aa2651c2f1f/relationships/repository",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciWorkflows/3fa0575f-4de0-44cb-bf0f-9aa2651c2f1f/repository"
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
        "self": "https://api.appstoreconnect.apple.com/v1/ciWorkflows/3fa0575f-4de0-44cb-bf0f-9aa2651c2f1f"
    }
}
```

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/ciWorkflows/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Workflows resource.

## Request Body

**Content-Type**: `application/json`  
**Type**: `CiWorkflowUpdateRequest`

The request body you use to update an Xcode Cloud workflow.

## Responses

- `200` OK (`CiWorkflowResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Xcode Cloud Workflows
- [Create a workflow](./post-v1-ciworkflows.md)
  Create a new Xcode Cloud workflow for an Xcode Cloud product.
- [Delete a workflow](./delete-v1-ciworkflows-_id_.md)
  Delete an Xcode Cloud workflow and all of its associated data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-ciworkflows-_id_)*