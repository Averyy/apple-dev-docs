# Read Queue Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific queue and its related objects.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingQueues/{id}`

## Parameters

- `fields[gameCenterMatchmakingQueues]` ([string]): The fields of the queue to include in the response.
- `include` ([string]): The type of rule set to include in the response.
- `fields[gameCenterMatchmakingRuleSets]` ([string])

## See Also

- [List All Queues](get-v1-gamecentermatchmakingqueues.md)
  Get information about all queues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecentermatchmakingqueues-_id_)*