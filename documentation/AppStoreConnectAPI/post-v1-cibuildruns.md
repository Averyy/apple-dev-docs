# Start a build

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Start a new Xcode Cloud build for a workflow.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below starts a new build for a specific workflow. Use the information provided in the response to display build information on a dashboard or to access additional information; for example, the actions Xcode Cloud performs during the build.

##### Example Request and Response

**Request**:

```
{
    “data”: {
        “type”: “ciBuildRuns”,
        “attributes”: {},
        “relationships”: {
            “workflow”: {
                “data”: {
                    “type”: “ciWorkflows”,
                    “id”: “a3946af0-cc38-4e0b-acba-5575c8dad050”
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
        "type": "ciBuildRuns",
        "id": "574f26a1-193c-409e-98ab-33ed4105a2ff",
        "attributes": {
            "number": 1,
            "createdDate": "2021-08-17T19:04:31.876Z",
            "startedDate": null,
            "finishedDate": null,
            "sourceCommit": {
                "commitSha": "The commit hash of the source commit.",
                "message": "A commit message.",
                "author": {
                    "displayName": "An author",
                    "avatarUrl": "https://example.com/user/avatar/author.png"
                },
                "committer": {
                    "displayName": "A committer",
                    "avatarUrl": "https://example.com/user/avatar/author.png"
                },
                "webUrl": "https://example.cpm/commits/abc123"
            },
            "destinationCommit": null,
            "isPullRequestBuild": false,
            "issueCounts": null,
            "executionProgress": "PENDING",
            "completionStatus": null,
            "startReason": "MANUAL",
            "cancelReason": null
        },
        "relationships": {
            "builds": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns/574f26a1-193c-409e-98ab-33ed4105a2ff/relationships/builds",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns/574f26a1-193c-409e-98ab-33ed4105a2ff/builds"
                }
            },
            "actions": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns/574f26a1-193c-409e-98ab-33ed4105a2ff/relationships/actions",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns/574f26a1-193c-409e-98ab-33ed4105a2ff/actions"
                }
            }
        },
        "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns/574f26a1-193c-409e-98ab-33ed4105a2ff"
        }
    },
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns"
    }
}


```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/ciBuildRuns`

## Request Body

**Content-Type**: `application/json`  
**Type**: `CiBuildRunCreateRequest`

The request body you use to start a new Xcode Cloud build.

## Responses

- `201` Created (`CiBuildRunResponse`, `application/json`): The request completed successfully and a new Build Runs resource has been created.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-cibuildruns)*