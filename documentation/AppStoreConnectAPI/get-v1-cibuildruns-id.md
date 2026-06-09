# Read xcode cloud build information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific Xcode Cloud build.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below retrieves detailed information for a specific build. Use the data provided in the response to display detailed build information on a dashboard or to access related information for each action Xcode Cloud performed.

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/ciBuildRuns/56c512e6-111e-4067-8e88-640c28ce91a7
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

`GET https://api.appstoreconnect.apple.com/v1/ciBuildRuns/{id}`

## Parameters

- `fields[ciBuildRuns]` ([string]): Additional fields to include for the Build Runs resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[builds]` (integer): The number of included Build Runs resources to return if the builds relationship is included.
- `fields[builds]` ([string]): Additional fields to include for the Build Runs resource returned by the response.
- `fields[ciProducts]` ([string])
- `fields[ciWorkflows]` ([string])
- `fields[scmGitReferences]` ([string])
- `fields[scmPullRequests]` ([string])

## See Also

- [List all actions for an xcode cloud build](get-v1-cibuildruns-_id_-actions.md)
  List all actions Xcode Cloud performed during a specific build.
- [List all builds xcode cloud created in app store connect](get-v1-cibuildruns-_id_-builds.md)
  List All App Store Connect and TestFlight Builds when it performed a build.
- [List action IDs for a CI build run](get-v1-cibuildruns-_id_-relationships-actions.md)
- [List build IDs for a CI build run](get-v1-cibuildruns-_id_-relationships-builds.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cibuildruns-_id_)*