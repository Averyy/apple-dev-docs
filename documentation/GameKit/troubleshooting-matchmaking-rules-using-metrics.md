# Troubleshooting matchmaking rules using metrics

**Framework**: GameKit

Investigate issues with Game Center by evaluating your matchmaking rules using metrics endpoints.

#### Overview

You can diagnose problems with your matchmaking rules using the metrics endpoints. You can get matchmaking data at different granularities, such as every 15 minutes for 8 hours, hourly over 24 hours, or daily for 30 days. If Game Center takes too long to find matches or fails to find matches, use the metrics APIs to help troubleshoot your rules.

##### View Match Requests on the Queue

First, confirm that your game submits requests to the correct queue using the [`Get match request time in queue`](https://developer.apple.com/documentation/AppStoreConnectAPI/GET-v1-gameCenterMatchmakingQueues-_id_-metrics-matchmakingRequests) endpoint. In the query parameters, pass the Game Center details `id` and pass a value for the `granularity` parameter that returns the level of information you want. To get the Game Center detail `id`, use the [`Enable Game Center for an app`](https://developer.apple.com/documentation/AppStoreConnectAPI/POST-v1-gameCenterDetails) or [`List Apps`](https://developer.apple.com/documentation/AppStoreConnectAPI/GET-v1-apps) endpoint.

```other
GET /v1/gameCenterMatchmakingQueues/8fb73d41-1ca1-1cbf-2538-9df424beb10b/metrics/matchmakingRequests?granularity=PT15M
```

Parse the match request data in the response. If the `count` field in the [`GameCenterMatchmakingAppRequestsV1MetricResponse.Data.DataPoints.Values`](https://developer.apple.com/documentation/AppStoreConnectAPI/GameCenterMatchmakingAppRequestsV1MetricResponse/Data-data.dictionary/DataPoints-data.dictionary/Values-data.dictionary) object isn’t the value you expect, verify that the game submits a [`GKMatchRequest`](gkmatchrequest.md) object with the correct value for the [`queueName`](gkmatchrequest/queuename.md) property. Also, check device logs for any errors that may occur when submitting match requests.

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

 It’s common for players to cancel a match request by quitting a game or other compatible match requests to arrive too late to fill empty slots. However, if the amount of canceled and expired match requests exceeds the amount of matched requests, investigate whether there’s a problem with your rules.

##### View Match Request Errors

Runtime errors can occur when your game submits a match request. If an error occurs while Game Center evaluates a match request, it may reject it and log an error. To view these types of errors, pass the matchmaking rule `id` and pass a `granularity` query parameter to the [`Get matchmaking rule errors`](https://developer.apple.com/documentation/AppStoreConnectAPI/GET-v1-gameCenterMatchmakingRules-_id_-metrics-matchmakingRuleErrors) endpoint.

```other
GET /v1/gameCenterMatchmakingRules/2b4835c6-d06b-479d-8b0f-dab9d7eb3d11/metrics/matchmakingRuleErrors?granularity=PT15M
```

If errors occur, use the testing` `APIs to reproduce the error. For more information, see [`Testing matchmaking rules`](testing-matchmaking-rules.md).

For example, you can verify that the game passes the correct key for game-specific data that your matchmaking rules use in the `GKMatchRequest` [`properties`](gkmatchrequest/properties.md) and [`recipientProperties`](gkmatchrequest/recipientproperties.md) properties.

To get the matchmaking rule `id`, use the [`Create a rule`](https://developer.apple.com/documentation/AppStoreConnectAPI/POST-v1-gameCenterMatchmakingRules) endpoint.

##### Check If Your Rules Are Too Restrictive

Your matchmaking rules should strike a balance between finding the best players and reducing wait times. Check whether your rules are too restrictive by getting the frequency that your rules reject candidate matches using the [`Get Boolean rule results`](https://developer.apple.com/documentation/AppStoreConnectAPI/GET-v1-gameCenterMatchmakingRules-_id_-metrics-matchmakingBooleanRuleResults) and [`Get numeric rule results`](https://developer.apple.com/documentation/AppStoreConnectAPI/GET-v1-gameCenterMatchmakingRules-_id_-metrics-matchmakingNumberRuleResults) endpoints. Pass the matchmaking rule `id,` pass a `granularity` query parameter, and to organize the results by type, set the `groupBy` query parameter to `result`.

```other
GET /v1/gameCenterMatchmakingRules/0f0fcbf9-43b6-429d-8c08-fcaf66a52872/metrics/matchmakingBooleanRuleResults?granularity=PT15M&groupBy=result
```

If your rules are too restrictive, consider relaxing the criteria over time using a match rule with an age function. For more information, see [`Finding players with similar skill levels`](finding-players-with-similar-skill-levels.md) and [`Expressions`](https://developer.apple.com/documentation/AppStoreConnectAPI/expressions) in App Store Connect API.

##### Keep the Queues Short and Responsive

If you submit too many match requests to one queue, the matchmaking algorithm may struggle to keep up with the requests and fail to find candidate matches, even when they exist in the queue. To avoid this problem, monitor the size of your queue using the [`Get queue size`](https://developer.apple.com/documentation/AppStoreConnectAPI/GET-v1-gameCenterMatchmakingQueues-_id_-metrics-matchmakingQueueSizes) endpoint. Pass the queue `id` and pass a `granularity` query parameter.

```other
GET /v1/gameCenterMatchmakingQueues/532ad9c0-1a28-4536-ad57-33213bcc0a29/metrics/matchmakingQueueSizes?granularity=PT15M
```

If the algorithm fails to find players as the queue size increases, try adding one or more queues and splitting match requests between them. For best results, keep the number of requests in each queue under 100. For more information, see [`The matchmaking rules algorithm`](matchmaking-rules#The-matchmaking-rules-algorithm.md).

To get the queue `id`, use the [`Create a queue`](https://developer.apple.com/documentation/AppStoreConnectAPI/POST-v1-gameCenterMatchmakingQueues) endpoint.

## See Also

- [Testing matchmaking rules](testing-matchmaking-rules.md)
  Test your matchmaking rules before you use them in your game.
- [Testing rule sets with player traffic using metrics](testing-rule-sets-with-player-traffic-using-metrics.md)
  Get metrics on a new rule set with real match requests before releasing it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/troubleshooting-matchmaking-rules-using-metrics)*