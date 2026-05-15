# List All Queues

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about all queues.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingQueues`

## Parameters

- `fields[gameCenterMatchmakingQueues]` ([string]): The fields of the queues to include in the response.
- `fields[gameCenterMatchmakingRuleSets]` ([string])
- `include` ([string]): The type of rule set to include in the response.
- `limit` (integer): The maximum number of queues to fetch.

## See Also

- [Read Queue Information](get-v1-gamecentermatchmakingqueues-_id_.md)
  Get information about a specific queue and its related objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecentermatchmakingqueues)*