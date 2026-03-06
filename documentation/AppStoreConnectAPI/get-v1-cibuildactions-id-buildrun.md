# Read the Xcode Cloud Build Information for a Build Action

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get Xcode Cloud build information for a given build action.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below retrieves detailed information for a specific action Xcode Cloud performed. Use the data provided in the response to display detailed build information on a dashboard or to access related information.

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/ciBuildActions/6034552c-6cc0-4ac3-ad18-c3d24970882d/buildRun
```

**Response**:

```json
{
    "data": {
        "type": "ciBuildRuns",
        "id": "56c512e6-111e-4067-8e88-640c28ce91a7",
        "attributes": {
            "number": 1,
            "createdDate": "2021-08-17T17:48:11.806Z",
            "startedDate": null,
            "finishedDate": null,
            "sourceCommit": {
                "commitSha": "SHA",
                "message": "Summary Message.\n\nSome more details about the commit.",
                "author": {
                    "displayName": "Source Author",
                    "avatarUrl": ""
                },
                "committer": {
                    "displayName": "Source Committer",
                    "avatarUrl": ""
                },
                "webUrl": "https://example.com/commit/abc123"
            },
            "destinationCommit": {
                "commitSha": "A commit hash.",
                "message": "BASE MESSAGE",
                "author": {
                    "displayName": "Base Author",
                    "avatarUrl": "https://example.com/user/avatar/author.png"
                },
                "committer": {
                    "displayName": "Base Committer",
                    "avatarUrl": "https://example.com/user/avatar/author.png"
                },
                "webUrl": "https://example.com/commit/xyz987"
            },
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
                    "self": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns/56c512e6-111e-4067-8e88-640c28ce91a7/relationships/builds",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns/56c512e6-111e-4067-8e88-640c28ce91a7/builds"
                }
            },
            "actions": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns/56c512e6-111e-4067-8e88-640c28ce91a7/relationships/actions",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns/56c512e6-111e-4067-8e88-640c28ce91a7/actions"
                }
            }
        },
        "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns/56c512e6-111e-4067-8e88-640c28ce91a7"
        }
    },
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns/56c512e6-111e-4067-8e88-640c28ce91a7"
    }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciBuildActions/{id}/buildRun`

## Parameters

- `fields[builds]` ([string]): Additional fields to include for each Build Runs resource returned by the response.
- `fields[ciBuildRuns]` ([string]): Additional fields to include for each Build Runs resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[builds]` (integer): The number of included Build Runs resources to return if the builds relationship is included.
- `fields[scmGitReferences]` ([string])
- `fields[ciWorkflows]` ([string])
- `fields[scmPullRequests]` ([string])
- `fields[ciProducts]` ([string])

## See Also

- [Read Build Action Information](get-v1-cibuildactions-_id_.md)
  Get information about a specific action Xcode Cloud performed as part of a build.
- [List All Artifacts for a Build Action](get-v1-cibuildactions-_id_-artifacts.md)
  List all artifacts Xcode Cloud created when it performed an action.
- [List All Issues for a Build Action](get-v1-cibuildactions-_id_-issues.md)
  List all issues that occurred for a specific action that Xcode Cloud performed as part of a build.
- [List All Test Results for an Xcode Cloud Test Action](get-v1-cibuildactions-_id_-testresults.md)
  List all test results for a specific test action Xcode Cloud performed as part of a build.
- [GET /v1/ciBuildActions/{id}/relationships/artifacts](get-v1-cibuildactions-_id_-relationships-artifacts.md)
- [GET /v1/ciBuildActions/{id}/relationships/buildRun](get-v1-cibuildactions-_id_-relationships-buildrun.md)
- [GET /v1/ciBuildActions/{id}/relationships/issues](get-v1-cibuildactions-_id_-relationships-issues.md)
- [GET /v1/ciBuildActions/{id}/relationships/testResults](get-v1-cibuildactions-_id_-relationships-testresults.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cibuildactions-_id_-buildrun)*