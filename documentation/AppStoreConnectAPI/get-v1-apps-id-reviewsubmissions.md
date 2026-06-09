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

- `fields[reviewSubmissionItems]` ([string]): Additional fields to include for each review submission item resource returned by the response.
- `fields[reviewSubmissions]` ([string]): Additional fields to include for each review submission resource returned by the response.
- `filter[platform]` ([string]): Filter the returned review submissions by platform.
- `filter[state]` ([string]): Filter the returned review submissions by state.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of review submission resources to return.
- `limit[items]` (integer): The maximum number of related items resources to return.
- `fields[appStoreVersions]` ([string]): Additional fields to include for each App Store version resource returned by the response.
- `fields[apps]` ([string]): Additional fields to include for each app resource returned by the response.
- `fields[actors]` ([string]): Additional fields to include for each actor resource returned by the response.

## See Also

- [List review submission IDs](get-v1-apps-_id_-relationships-reviewsubmissions.md)
  Get the list of review submission IDs for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-reviewsubmissions)*