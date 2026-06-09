# Read pull request information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific pull request.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below retrieves information about a specific pull request. For example, use the data provided in the response to display pull request information on a custom dashboard.

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/scmPullRequests/3372ba3b-013d-4328-9b48-0ef8ec54f48d
```

**Response**:

```json
{
    "data": {
        "type": "scmPullRequests",
        "id": "3372ba3b-013d-4328-9b48-0ef8ec54f48d",
        "attributes": {
            "title": "A sample pull request",
            "number": 123,
            "webUrl": "https://github.com/example-user/example-app/pull/123",
            "sourceRepositoryOwner": "example-user",
            "sourceRepositoryName": "example-app",
            "sourceBranchName": "BRANCH",
            "destinationRepositoryOwner": "example-user",
            "destinationRepositoryName": "example-app",
            "destinationBranchName": "main",
            "isClosed": false,
            "isCrossRepository": false
        },
        "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/scmPullRequests/3372ba3b-013d-4328-9b48-0ef8ec54f48d"
        }
    },
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/scmPullRequests/3372ba3b-013d-4328-9b48-0ef8ec54f48d"
    }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/scmPullRequests/{id}`

## Parameters

- `fields[scmPullRequests]` ([string]): Additional fields to include for the Pull Requests resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `fields[scmRepositories]` ([string])


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-scmpullrequests-_id_)*