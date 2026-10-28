# Troubleshooting matchmaking rules using metrics

**Framework**: GameKit  
**Role**: Article

Investigate issues with Game Center by evaluating your matchmaking rules using metrics endpoints.

## Overview

You can diagnose problems with your matchmaking rules using the metrics endpoints. You can get matchmaking data at different granularities, such as every 15 minutes for 8 hours, hourly over 24 hours, or daily for 30 days. If Game Center takes too long to find matches or fails to find matches, use the metrics APIs to help troubleshoot your rules.

### View match requests on the queue

First, confirm that your game submits requests to the correct queue using the [`Get Match Request Time in Queue`](../AppStoreConnectAPI/get-v1-gamecentermatchmakingqueues-_id_-metrics-matchmakingrequests.md) endpoint. In the query parameters, pass the Game Center details `id` and pass a value for the `granularity` parameter that returns the level of information you want. To get the Game Center detail `id`, use the [`Enable game center for an app`](../AppStoreConnectAPI/post-v1-gamecenterdetails.md) or [`List apps`](../AppStoreConnectAPI/get-v1-apps.md) endpoint.

```other
GET /v1/gameCenterMatchmakingQueues/8fb73d41-1ca1-1cbf-2538-9df424beb10b/metrics/matchmakingRequests?granularity=PT15M
```

Parse the match request data in the response. If the `count` field in the [`GameCenterMatchmakingAppRequestsV1MetricResponse.Data.DataPoints.Values`](../AppStoreConnectAPI/gamecentermatchmakingapprequestsv1metricresponse/data-data.dictionary/datapoints-data.dictionary/values-data.dictionary.md) object isn’t the value you expect, verify that the game submits a [`GKMatchRequest`](./gkmatchrequest.md) object with the correct value for the [`queueName`](./gkmatchrequest/queuename.md) property. Also, check device logs for any errors that may occur when submitting match requests.

```json
{    
      “data”: [    
        {  
          "type": "gameCenterMatchmakingQueueRequests",  
          “dataPoints”: [   
            {  
              “start”: “2023-10-05T04:00:00Z”, 
              “end”: “2023-10-05T04:15:00Z”, 
              “values”: {    
                “averageSecondsInQueue”: 2.9630714285714284, 
                “p95SecondsInQueue”: 3.838, 
                “count”: 14,   
                “p50SecondsInQueue”: 3.36   
              }    
            },
...
```

To organize the match requests by type (`MATCHED`, `CANCELED`, and `EXPIRED`), set the `groupBy` query parameter to `result`.

```other
GET /v1/gameCenterMatchmakingQueues/8fb73d41-1ca1-1cbf-2538-9df424beb10b/metrics/matchmakingRequests?granularity=PT15M&groupBy=result
```

> **Note**:  It’s common for players to cancel a match request by quitting a game or other compatible match requests to arrive too late to fill empty slots. However, if the amount of canceled and expired match requests exceeds the amount of matched requests, investigate whether there’s a problem with your rules.

### View match request errors

Runtime errors can occur when your game submits a match request. If an error occurs while Game Center evaluates a match request, it may reject it and log an error. To view these types of errors, pass the matchmaking rule `id` and pass a `granularity` query parameter to the [`Get Matchmaking Rule Errors`](../AppStoreConnectAPI/get-v1-gamecentermatchmakingrules-_id_-metrics-matchmakingruleerrors.md) endpoint.

```other
GET /v1/gameCenterMatchmakingRules/2b4835c6-d06b-479d-8b0f-dab9d7eb3d11/metrics/matchmakingRuleErrors?granularity=PT15M
```

If errors occur, use the testing` `APIs to reproduce the error. For more information, see [Testing matchmaking rules](./testing-matchmaking-rules.md).

For example, you can verify that the game passes the correct key for game-specific data that your matchmaking rules use in the `GKMatchRequest` [`properties`](./gkmatchrequest/properties.md) and [`recipientProperties`](./gkmatchrequest/recipientproperties.md) properties.

To get the matchmaking rule `id`, use the [`Create a Rule`](../AppStoreConnectAPI/post-v1-gamecentermatchmakingrules.md) endpoint.

### Check if your rules are too restrictive

Your matchmaking rules should strike a balance between finding the best players and reducing wait times. Check whether your rules are too restrictive by getting the frequency that your rules reject candidate matches using the [`Get boolean rule results`](../AppStoreConnectAPI/get-v1-gamecentermatchmakingrules-_id_-metrics-matchmakingbooleanruleresults.md) and [`Get Numeric Rule Results`](../AppStoreConnectAPI/get-v1-gamecentermatchmakingrules-_id_-metrics-matchmakingnumberruleresults.md) endpoints. Pass the matchmaking rule `id,` pass a `granularity` query parameter, and to organize the results by type, set the `groupBy` query parameter to `result`.

```other
GET /v1/gameCenterMatchmakingRules/0f0fcbf9-43b6-429d-8c08-fcaf66a52872/metrics/matchmakingBooleanRuleResults?granularity=PT15M&groupBy=result
```

If your rules are too restrictive, consider relaxing the criteria over time using a match rule with an age function. For more information, see [Finding players with similar skill levels](./finding-players-with-similar-skill-levels.md) and [Expressions](../AppStoreConnectAPI/expressions.md) in App Store Connect API.

### Keep the queues short and responsive

If you submit too many match requests to one queue, the matchmaking algorithm may struggle to keep up with the requests and fail to find candidate matches, even when they exist in the queue. To avoid this problem, monitor the size of your queue using the [`Get Queue Size`](../AppStoreConnectAPI/get-v1-gamecentermatchmakingqueues-_id_-metrics-matchmakingqueuesizes.md) endpoint. Pass the queue `id` and pass a `granularity` query parameter.

```other
GET /v1/gameCenterMatchmakingQueues/532ad9c0-1a28-4536-ad57-33213bcc0a29/metrics/matchmakingQueueSizes?granularity=PT15M
```

If the algorithm fails to find players as the queue size increases, try adding one or more queues and splitting match requests between them. For best results, keep the number of requests in each queue under 100. For more information, see [The matchmaking rules algorithm](./matchmaking-rules.md#The-matchmaking-rules-algorithm).

To get the queue `id`, use the [`Create a Queue`](../AppStoreConnectAPI/post-v1-gamecentermatchmakingqueues.md) endpoint.

## See Also

### Testing
- [Testing matchmaking rules](./testing-matchmaking-rules.md)
  Test your matchmaking rules before you use them in your game.
- [Testing rule sets with player traffic using metrics](./testing-rule-sets-with-player-traffic-using-metrics.md)
  Get metrics on a new rule set with real match requests before releasing it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/troubleshooting-matchmaking-rules-using-metrics)*