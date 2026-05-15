# Get Review Submissions for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of review submissions associated with a specific app.

**Availability**:
- App Store Connect API 1.7+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/6446998023/reviewSubmissions
```

**Response**:

```json
{
    "data": [
        {
            "type": "reviewSubmissions",
            "id": "fda9bd85-170b-4a1c-8d78-c2b445527542",
            "attributes": {
                "platform": "IOS",
                "submittedDate": null,
                "state": "READY_FOR_REVIEW"
            },
            "relationships": {
                "items": {
                    "links": {
                        "self": "https://api.appstoreconnect.apple.com/v1/reviewSubmissions/fda9bd85-170b-4a1c-8d78-c2b445527542/relationships/items",
                        "related": "https://api.appstoreconnect.apple.com/v1/reviewSubmissions/fda9bd85-170b-4a1c-8d78-c2b445527542/items"
                    }
                }
            },
            "links": {
                "self": "https://api.appstoreconnect.apple.com/v1/reviewSubmissions/fda9bd85-170b-4a1c-8d78-c2b445527542"
            }
        }
    ],
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/reviewSubmissions"
    },
    "meta": {
        "paging": {
            "total": 1,
            "limit": 50
        }
    }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/reviewSubmissions`

## Parameters

- `fields[reviewSubmissionItems]` ([string])
- `fields[reviewSubmissions]` ([string])
- `filter[platform]` ([string])
- `filter[state]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[items]` (integer)
- `fields[appStoreVersions]` ([string])
- `fields[apps]` ([string])
- `fields[actors]` ([string])

## See Also

- [List Review Submission IDs](get-v1-apps-_id_-relationships-reviewsubmissions.md)
  Get the list of review submission IDs for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-reviewsubmissions)*