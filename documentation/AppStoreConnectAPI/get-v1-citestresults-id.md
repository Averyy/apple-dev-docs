# Read test result information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a specific test result Xcode Cloud created when it performed a build with a test action.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below retrieves result information for a test Xcode Cloud performed. Use the data provided in the response to display test result information on a dashboard, create reports, or create a new issue in your issue tracker for a failing test.

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/ciTestResults/5ecb25ea-ce31-4b50-b88c-f1bf64c698ae
```

**Response**:

```json
{
    "data": {
        "type": "ciTestResults",
        "id": "5ecb25ea-ce31-4b50-b88c-f1bf64c698ae",
        "attributes": {
            "className": "TestClass",
            "name": "TestName",
            "status": "SUCCESS",
            "fileSource": null,
            "message": null,
            "destinationTestResults": [
                {
                    "uuid": "e456c6a3-37a3-42c7-8299-33dad720f6b7",
                    "deviceName": "iPhone X",
                    "osVersion": "11.4.1",
                    "status": "SUCCESS",
                    "duration": 6.600471973
                }
            ]
        },
        "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/ciTestResults/5ecb25ea-ce31-4b50-b88c-f1bf64c698ae"
        }
    },
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/ciTestResults/5ecb25ea-ce31-4b50-b88c-f1bf64c698ae"
    }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciTestResults/{id}`

## Parameters

- `fields[ciTestResults]` ([string]): Additional fields to include for the Test Results resource returned by the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-citestresults-_id_)*