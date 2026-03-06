# List All Test Results for an Xcode Cloud Test Action

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all test results for a specific test action Xcode Cloud performed as part of a build.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below lists the test results for an Xcode Cloud build that performed a test action. Use the information provided in the response to display test results on a dashboard, create a new task for a failing test in your issue tracker, and so on.

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/ciBuildActions/d871dabb-2c2c-4012-aff5-abb427bcb3a3/testResults
```

**Response**:

```json
{
"data": [
        {
            "type": "ciTestResults",
            "id": "87f8a597-bea9-49d8-ba8b-6a643de66903",
            "attributes": {
                "className": "TestClass",
                "name": "TestName",
                "status": "SUCCESS",
                "fileSource": {
                    "path": "path",
                    "lineNumber": 100
                },
                "message": null,
                "destinationTestResults": [
                    {
                        "uuid": "8d1bff05-2b9c-4cc4-9225-e2cd41dee260",
                        "deviceName": "iPhone X",
                        "osVersion": "11.4.1",
                        "status": "SUCCESS",
                        "duration": 6.600471973
                    }
                ]
            },
            "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/ciTestResults/87f8a597-bea9-49d8-ba8b-6a643de66903"
            }
        }
    ],
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/ciBuildActions/d871dabb-2c2c-4012-aff5-abb427bcb3a3/testResults"
    },
    "meta": {
        "paging": {
            "limit": 50
        }
    }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciBuildActions/{id}/testResults`

## Parameters

- `fields[ciTestResults]` ([string]): Additional fields to include for each Test Results resource returned by the response.
- `limit` (integer): The number of Test Results resources to return.

## See Also

- [Read Build Action Information](get-v1-cibuildactions-_id_.md)
  Get information about a specific action Xcode Cloud performed as part of a build.
- [List All Artifacts for a Build Action](get-v1-cibuildactions-_id_-artifacts.md)
  List all artifacts Xcode Cloud created when it performed an action.
- [Read the Xcode Cloud Build Information for a Build Action](get-v1-cibuildactions-_id_-buildrun.md)
  Get Xcode Cloud build information for a given build action.
- [List All Issues for a Build Action](get-v1-cibuildactions-_id_-issues.md)
  List all issues that occurred for a specific action that Xcode Cloud performed as part of a build.
- [GET /v1/ciBuildActions/{id}/relationships/artifacts](get-v1-cibuildactions-_id_-relationships-artifacts.md)
- [GET /v1/ciBuildActions/{id}/relationships/buildRun](get-v1-cibuildactions-_id_-relationships-buildrun.md)
- [GET /v1/ciBuildActions/{id}/relationships/issues](get-v1-cibuildactions-_id_-relationships-issues.md)
- [GET /v1/ciBuildActions/{id}/relationships/testResults](get-v1-cibuildactions-_id_-relationships-testresults.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-cibuildactions-_id_-testresults)*