# List All Issues for a Build Action

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all issues that occurred for a specific action that Xcode Cloud performed as part of a build.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below lists all issues Xcode Cloud encountered when it performed a build. Use the information provided in the response to display issue information on a dashboard, generate reports, automatically create tasks in your issue tracker, and so on.

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/ciBuildActions/2488c5ec-ee0c-425e-902b-41c1e88208ca/issues
```

**Response**:

```json
{
"data": [
        {
            "type": "ciIssues",
            "id": "b5ed3706-96e4-4111-be17-049fb365b72e",
            "attributes": {
                "issueType": "ERROR",
                "message": "An example message.",
                "fileSource": {
                    "path": "/path/to/the/file/that/contains/the/issue",
                    "lineNumber": 42
                },
                "category": null
            },
            "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/ciIssues/b5ed3706-96e4-4111-be17-049fb365b72e"
            }
        }
    ],
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/2488c5ec-ee0c-425e-902b-41c1e88208ca/issues"
    },
    "meta": {
        "paging": {
            "limit": 50
        }
    }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciBuildActions/{id}/issues`

## Parameters

- `fields[ciIssues]` ([string]): Additional fields to include for each Issues resource returned by the response.
- `limit` (integer): The number of Issues resources to return.

## See Also

- [Read Build Action Information](get-v1-cibuildactions-_id_.md)
  Get information about a specific action Xcode Cloud performed as part of a build.
- [List All Artifacts for a Build Action](get-v1-cibuildactions-_id_-artifacts.md)
  List all artifacts Xcode Cloud created when it performed an action.
- [Read the Xcode Cloud Build Information for a Build Action](get-v1-cibuildactions-_id_-buildrun.md)
  Get Xcode Cloud build information for a given build action.
- [List All Test Results for an Xcode Cloud Test Action](get-v1-cibuildactions-_id_-testresults.md)
  List all test results for a specific test action Xcode Cloud performed as part of a build.
- [GET /v1/ciBuildActions/{id}/relationships/artifacts](get-v1-cibuildactions-_id_-relationships-artifacts.md)
- [GET /v1/ciBuildActions/{id}/relationships/buildRun](get-v1-cibuildactions-_id_-relationships-buildrun.md)
- [GET /v1/ciBuildActions/{id}/relationships/issues](get-v1-cibuildactions-_id_-relationships-issues.md)
- [GET /v1/ciBuildActions/{id}/relationships/testResults](get-v1-cibuildactions-_id_-relationships-testresults.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cibuildactions-_id_-issues)*