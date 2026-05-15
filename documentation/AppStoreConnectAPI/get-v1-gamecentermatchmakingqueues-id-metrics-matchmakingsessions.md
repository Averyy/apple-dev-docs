# Get Queue Session Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get session information on a queue.

**Availability**:
- App Store Connect API 3.1+

#### Discussion

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingQueues/0df9ae63-0328-4060-9afc-53e848e8c386/metrics/matchmakingSessions?granularity=PT15M
```

**Response**:

```json
{
  "data": [
    {
      "type": "gameCenterMatchmakingSessions",
      "dataPoints": [
        {
          "start": "2023-10-10T23:30:00Z",
          "end": "2023-10-10T23:45:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T23:15:00Z",
          "end": "2023-10-10T23:30:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T23:00:00Z",
          "end": "2023-10-10T23:15:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T22:45:00Z",
          "end": "2023-10-10T23:00:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T22:30:00Z",
          "end": "2023-10-10T22:45:00Z",
          "values": {
            "count": 1,
            "p50PlayerCount": 2,
            "averagePlayerCount": 2,
            "p95PlayerCount": 2
          }
        },
        {
          "start": "2023-10-10T22:15:00Z",
          "end": "2023-10-10T22:30:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T22:00:00Z",
          "end": "2023-10-10T22:15:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T21:45:00Z",
          "end": "2023-10-10T22:00:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T21:30:00Z",
          "end": "2023-10-10T21:45:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T21:15:00Z",
          "end": "2023-10-10T21:30:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T21:00:00Z",
          "end": "2023-10-10T21:15:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T20:45:00Z",
          "end": "2023-10-10T21:00:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T20:30:00Z",
          "end": "2023-10-10T20:45:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T20:15:00Z",
          "end": "2023-10-10T20:30:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T20:00:00Z",
          "end": "2023-10-10T20:15:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T19:45:00Z",
          "end": "2023-10-10T20:00:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T19:30:00Z",
          "end": "2023-10-10T19:45:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T19:15:00Z",
          "end": "2023-10-10T19:30:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T19:00:00Z",
          "end": "2023-10-10T19:15:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T18:45:00Z",
          "end": "2023-10-10T19:00:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T18:30:00Z",
          "end": "2023-10-10T18:45:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T18:15:00Z",
          "end": "2023-10-10T18:30:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T18:00:00Z",
          "end": "2023-10-10T18:15:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T17:45:00Z",
          "end": "2023-10-10T18:00:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T17:30:00Z",
          "end": "2023-10-10T17:45:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T17:15:00Z",
          "end": "2023-10-10T17:30:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T17:00:00Z",
          "end": "2023-10-10T17:15:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T16:45:00Z",
          "end": "2023-10-10T17:00:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T16:30:00Z",
          "end": "2023-10-10T16:45:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T16:15:00Z",
          "end": "2023-10-10T16:30:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T16:00:00Z",
          "end": "2023-10-10T16:15:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        },
        {
          "start": "2023-10-10T15:45:00Z",
          "end": "2023-10-10T16:00:00Z",
          "values": {
            "count": 0,
            "p50PlayerCount": 0,
            "averagePlayerCount": 0,
            "p95PlayerCount": 0
          }
        }
      ],
      "granularity": 900
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingQueues/0df9ae63-0328-4060-9afc-53e848e8c386/metrics/matchmakingSessions?granularity=PT15M"
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

`GET https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingQueues/{id}/metrics/matchmakingSessions`

## Parameters

- `granularity` (string) *(required)*: The level of information you want in the response, specified as a time interval for the data collection, using the ISO 8601 format for durations.
- `limit` (integer): The maximum number of sessions to include.
- `sort` ([string]): Sort sizes by the specified order. For example, `count` sorts the results by decreasing number of players that Game Center finds.

## See Also

- [Get Queue Size](get-v1-gamecentermatchmakingqueues-_id_-metrics-matchmakingqueuesizes.md)
  Get the time that match requests are in a specific queue.
- [Get Experimental Queue Size](get-v1-gamecentermatchmakingqueues-_id_-metrics-experimentmatchmakingqueuesizes.md)
  Get the number of match requests that the queue processes using its experimental rule set.
- [Get Match Request Time in Queue](get-v1-gamecentermatchmakingqueues-_id_-metrics-matchmakingrequests.md)
  Get the match requests that a specific queue processes.
- [Get Experimental Match Request Time in Queue](get-v1-gamecentermatchmakingqueues-_id_-metrics-experimentmatchmakingrequests.md)
  Get the match requests that a specific queue processes using its experimental rule set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecentermatchmakingqueues-_id_-metrics-matchmakingsessions)*