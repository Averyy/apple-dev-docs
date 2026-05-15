# Get Experimental Match Request Time in Queue

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the match requests that a specific queue processes using its experimental rule set.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingQueues/{id}/metrics/experimentMatchmakingRequests`

## Parameters

- `filter[gameCenterDetail]` (string): The fields of the queues to include in the response.
- `filter[result]` (string): The types of match requests to include in the response.
- `granularity` (string) *(required)*: The level of information you want in the response, specified as a time interval for the data collection, using the ISO 8601 format for durations.
- `groupBy` ([string]): Group match requests by result.
- `limit` (integer): The maximum number of match requests to include.
- `sort` ([string]): Sort sizes by the specified order. For example, `count` sorts the results by decreasing number of players that Game Center finds.

## See Also

- [Get Queue Size](get-v1-gamecentermatchmakingqueues-_id_-metrics-matchmakingqueuesizes.md)
  Get the time that match requests are in a specific queue.
- [Get Experimental Queue Size](get-v1-gamecentermatchmakingqueues-_id_-metrics-experimentmatchmakingqueuesizes.md)
  Get the number of match requests that the queue processes using its experimental rule set.
- [Get Match Request Time in Queue](get-v1-gamecentermatchmakingqueues-_id_-metrics-matchmakingrequests.md)
  Get the match requests that a specific queue processes.
- [Get Queue Session Information](get-v1-gamecentermatchmakingqueues-_id_-metrics-matchmakingsessions.md)
  Get session information on a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecentermatchmakingqueues-_id_-metrics-experimentmatchmakingrequests)*