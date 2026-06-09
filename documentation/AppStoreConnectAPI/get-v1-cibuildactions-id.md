# Read build action information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific action Xcode Cloud performed as part of a build.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below retrieves detailed information about an action Xcode Cloud performed. It also requests detailed information about the action’s build by including the [`Build Runs`](build-runs.md) resource in the query. Use the information provided in the response to display information on a dashboard or to access additional information; for example, information about other actions Xcode Cloud performed during the build.

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/ciBuildActions/6034552c-6cc0-4ac3-ad18-c3d24970882d?include=buildRun
```

**Response**:

```json
{
    "data": {
        "type": "ciBuildActions",
        "id": "6034552c-6cc0-4ac3-ad18-c3d24970882d",
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
                "data": {
                    "type": "ciBuildRuns",
                    "id": "a2c112a3-1ed1-416d-baf8-a9f46909a16a"
                },
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/6034552c-6cc0-4ac3-ad18-c3d24970882d/relationships/buildRun",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/6034552c-6cc0-4ac3-ad18-c3d24970882d/buildRun"
                }
            },
            "artifacts": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/6034552c-6cc0-4ac3-ad18-c3d24970882d/relationships/artifacts",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/6034552c-6cc0-4ac3-ad18-c3d24970882d/artifacts"
                }
            },
            "issues": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/6034552c-6cc0-4ac3-ad18-c3d24970882d/relationships/issues",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/6034552c-6cc0-4ac3-ad18-c3d24970882d/issues"
                }
            },
            "testResults": {
                "links": {
                    "self": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/6034552c-6cc0-4ac3-ad18-c3d24970882d/relationships/testResults",
                    "related": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/6034552c-6cc0-4ac3-ad18-c3d24970882d/testResults"
                }
            }
        },
        "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/6034552c-6cc0-4ac3-ad18-c3d24970882d"
        }
    },
    "included": [
        {
            "type": "ciBuildRuns",
            "id": "a2c112a3-1ed1-416d-baf8-a9f46909a16a",
            "attributes": {
                "number": 1,
                "createdDate": "2021-08-17T17:33:22.59Z",
                "startedDate": null,
                "finishedDate": null,
                "sourceCommit": {
                    "commitSha": "SHA",
                    "message": "Summary Message\n\nSome more details about the commit message.",
                    "author": {
                        "displayName": "Source Author",
                        "avatarUrl": "https://example.com/user/avatar/author.png"
                    },
                    "committer": {
                        "displayName": "Source Committer",
                        "avatarUrl": "https://example.com/user/avatar/author.png"
                    },
                    "webUrl": "https://example.com/commit/abc123"
                },
                "destinationCommit": {
                    "commitSha": "PR_BASE_COMMIT_SHA",
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
                "buildRun": {},
                "builds": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns/a2c112a3-1ed1-416d-baf8-a9f46909a16a/relationships/builds",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns/a2c112a3-1ed1-416d-baf8-a9f46909a16a/builds"
                    }
                },
                "actions": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns/a2c112a3-1ed1-416d-baf8-a9f46909a16a/relationships/actions",
                        "related": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns/a2c112a3-1ed1-416d-baf8-a9f46909a16a/actions"
                    }
                }
            },
            "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/ciBuildRuns/a2c112a3-1ed1-416d-baf8-a9f46909a16a"
            }
        }
    ],
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/6034552c-6cc0-4ac3-ad18-c3d24970882d?include=buildRun"
    }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciBuildActions/{id}`

## Parameters

- `fields[ciBuildActions]` ([string]): Additional fields to include for the Build Actions resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `fields[ciBuildRuns]` ([string]): Additional fields to include for the Build Actions resource returned by the response.

## See Also

- [List all artifacts for a build action](get-v1-cibuildactions-_id_-artifacts.md)
  List all artifacts Xcode Cloud created when it performed an action.
- [Read the xcode cloud build information for a build action](get-v1-cibuildactions-_id_-buildrun.md)
  Get Xcode Cloud build information for a given build action.
- [List all issues for a build action](get-v1-cibuildactions-_id_-issues.md)
  List all issues that occurred for a specific action that Xcode Cloud performed as part of a build.
- [List all test results for an xcode cloud test action](get-v1-cibuildactions-_id_-testresults.md)
  List all test results for a specific test action Xcode Cloud performed as part of a build.
- [List artifact IDs for a CI build action](get-v1-cibuildactions-_id_-relationships-artifacts.md)
- [Get the build run ID for a CI build action](get-v1-cibuildactions-_id_-relationships-buildrun.md)
- [List issue IDs for a CI build action](get-v1-cibuildactions-_id_-relationships-issues.md)
- [List test result IDs for a CI build action](get-v1-cibuildactions-_id_-relationships-testresults.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cibuildactions-_id_)*