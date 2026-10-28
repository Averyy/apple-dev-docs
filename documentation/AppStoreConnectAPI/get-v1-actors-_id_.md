# Read actor information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific actor.

**Availability**:
- App Store Connect API 2.4+

## Discussion

### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/actors/USER:2cd2a1ef-cb74-411c-a078-0ebe119ade73
```

**Response**:

```json
{
  “data” : {
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
  },
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/actors/USER%3A2cd2a1ef-cb74-411c-a078-0ebe119ade73”
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/actors/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`Read Review Submission Information`](./get-v1-reviewsubmissions-_id_.md) response with the include [`ReviewSubmission.Relationships.SubmittedByActor`](./reviewsubmission/relationships-data.dictionary/submittedbyactor-data.dictionary.md).

### Query Parameters

- `fields[actors]` ([string]): Additional fields to include for each actors resource returned by the response.

  **Allowed Values**: `actorType`, `userFirstName`, `userLastName`, `userEmail`, `apiKeyId`

## Responses

- `200` OK (`ActorResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading actor information
- [List all actors](./get-v1-actors.md)
  Get a list of actors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-actors-_id_)*