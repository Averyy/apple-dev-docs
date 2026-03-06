# List All Actors

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of actors.

**Availability**:
- App Store Connect API 2.4+

#### Discussion

This endpoint supports multiple id’s in the filter paramenter.

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/actors?filter%5Bid%5D=USER%3A2cd2a1ef-cb74-411c-a078-0ebe119ade73,USER%3A83f7ddc0-64d6-4e4f-a5d9-51d74a8009a3
```

**Response**:

```json
{  “data” : [ {
    “type” : “actors”,
    “id” : “USER:83f7ddc0-64d6-4e4f-a5d9-51d74a8009a3”,
    “attributes” : {
      “actorType” : “USER”,
      “userFirstName” : “Maria”,
      “userLastName” : “Ruiz”,
      “userEmail” : “mruiz2@icloud.com”,
      “apiKeyId” : null
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/actors/USER%3A83f7ddc0-64d6-4e4f-a5d9-51d74a8009a3”
    }
  }, {
    “type” : “actors”,
    “id” : “USER:2cd2a1ef-cb74-411c-a078-0ebe119ade73”,
    “attributes” : {
      “actorType” : “USER”,
      “userFirstName” : “Bill”,
      “userLastName” : “James”,
      “userEmail” : “billjames2@icloud.com”,
      “apiKeyId” : null
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/actors/USER%3A2cd2a1ef-cb74-411c-a078-0ebe119ade73”
    }
  } ],
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/actors?filter%5Bid%5D=USER%3A2cd2a1ef-cb74-411c-a078-0ebe119ade73%2CUSER%3A83f7ddc0-64d6-4e4f-a5d9-51d74a8009a3”
  },
  “meta” : {
    “paging” : {
      “total” : 2,
      “limit” : 50
    }
  }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/actors`

## Parameters

- `fields[actors]` ([string])
- `filter[id]` ([string]) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`Read review submission information`](get-v1-reviewsubmissions-_id_.md) response with the include [`ReviewSubmission.Relationships.SubmittedByActor`](reviewsubmission/relationships-data.dictionary/submittedbyactor-data.dictionary.md).
- `limit` (integer)

## See Also

- [Read Actor Information](get-v1-actors-_id_.md)
  Get information about a specific actor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-actors)*