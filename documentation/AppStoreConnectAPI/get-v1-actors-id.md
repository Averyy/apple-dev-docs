# Read Actor Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific actor.

**Availability**:
- App Store Connect API 2.4+

#### Discussion

##### Example Request and Response

**Request**:

```None
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

- `fields[actors]` ([string])

## See Also

- [List All Actors](get-v1-actors.md)
  Get a list of actors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-actors-_id_)*