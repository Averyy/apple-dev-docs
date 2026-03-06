# Read Xcode Cloud Issue Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific issue that occurred when Xcode Cloud performed a build.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below retrieves information about a specific issue Xcode Cloud encountered when it performed a build. Use the information provided to display issues on a dashboard, create reports, and so on.

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/ciIssues/61473b34-2ecd-498d-9e2b-94216b7e8fb4
```

**Response**:

```json
{
    "data": {
        "type": "ciIssues",
        "id": "61473b34-2ecd-498d-9e2b-94216b7e8fb4",
        "attributes": {
            "issueType": "ERROR",
            "message": "A message describing the issue.",
            "fileSource": {
                "path": "/the/path/to/the/file/with/the/issue",
                "lineNumber": 42
            },
            "category": null
        },
        "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/ciIssues/61473b34-2ecd-498d-9e2b-94216b7e8fb4"
        }
    },
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/ciIssues/61473b34-2ecd-498d-9e2b-94216b7e8fb4"
    }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciIssues/{id}`

## Parameters

- `fields[ciIssues]` ([string]): Additional fields to include for the Issues resource returned by the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-ciissues-_id_)*