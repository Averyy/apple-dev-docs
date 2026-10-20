# List all actions for an xcode cloud build

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all actions Xcode Cloud performed during a specific build.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below lists actions Xcode Cloud performed during a specific build. Use the information provided in the response to display detailed action information on a dashboard or to read additional data; for example, test results.

##### Example Request and Response

**Request**:

```
GET https://api.appstoreconnect.apple.com/v1/ciBuildRuns/074e6e3e-8343-49dd-87a3-c4274ba0faab/actions
```

**Response**:

```json
{
    "data": [
        {
            "type": "ciBuildActions",
            "id": "457284a8-7168-4c41-982a-75d764dea585",
            "attributes": {
                "name": "archive",
                "actionType": "ARCHIVE",
                "startedDate": null,
                "finishedDate": null,
                "issueCounts": null,
                "executionProgress": "PENDING",
                "completionStatus": null,
                "isRequiredToPass": true
            },
            "relationships": {
                "buildRun": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/457284a8-7168-4c41-982a-75d764dea585/relationships/buildRun",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/457284a8-7168-4c41-982a-75d764dea585/buildRun"
                    }
                },
                "artifacts": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/457284a8-7168-4c41-982a-75d764dea585/relationships/artifacts",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/457284a8-7168-4c41-982a-75d764dea585/artifacts"
                    }
                },
                "issues": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/457284a8-7168-4c41-982a-75d764dea585/relationships/issues",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/457284a8-7168-4c41-982a-75d764dea585/issues"
                    }
                },
                "testResults": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/457284a8-7168-4c41-982a-75d764dea585/relationships/testResults",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/457284a8-7168-4c41-982a-75d764dea585/testResults"
                    }
                }
            },
            "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/457284a8-7168-4c41-982a-75d764dea585"
            }
        }
    ],
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns/074e6e3e-8343-49dd-87a3-c4274ba0faab/actions"
    },
    "meta": {
        "paging": {
            "limit": 50
        }
    }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciBuildRuns/{id}/actions`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Build Runs resource.

### Query Parameters

- `fields[ciBuildActions]` ([string]): Additional fields to include for each Actions resource returned by the response.

  **Allowed Values**: `name`, `actionType`, `startedDate`, `finishedDate`, `issueCounts`, `executionProgress`, `completionStatus`, `isRequiredToPass`, `buildRun`, `artifacts`, `issues`, `testResults`
- `limit` (integer): The number of Actions resources to return.

  **Maximum**: `200`
- `fields[ciBuildRuns]` ([string]): **Allowed Values**: `number`, `createdDate`, `startedDate`, `finishedDate`, `sourceCommit`, `destinationCommit`, `isPullRequestBuild`, `issueCounts`, `executionProgress`, `completionStatus`, `startReason`, `cancelReason`, `builds`, `workflow`, `product`, `sourceBranchOrTag`, `destinationBranch`, `actions`, `pullRequest`
- `include` ([string]): **Allowed Values**: `buildRun`

## Responses

- `200` OK (`CiBuildActionsResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Build Information
- [Read xcode cloud build information](./get-v1-cibuildruns-_id_.md)
  Get information about a specific Xcode Cloud build.
- [List all builds xcode cloud created in app store connect](./get-v1-cibuildruns-_id_-builds.md)
  List All App Store Connect and TestFlight Builds when it performed a build.
- [List action IDs for a CI build run](./get-v1-cibuildruns-_id_-relationships-actions.md)
- [List build IDs for a CI build run](./get-v1-cibuildruns-_id_-relationships-builds.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cibuildruns-_id_-actions)*