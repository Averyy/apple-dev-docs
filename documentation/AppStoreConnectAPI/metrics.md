# Metrics

**Framework**: App Store Connect API

Analyze data about matchmaking rules.

#### Overview

Use the Metrics APIs to diagnose performance and other issues with matchmaking rules. For more information, see [`Troubleshooting matchmaking rules using metrics`](https://developer.apple.com/documentation/GameKit/troubleshooting-matchmaking-rules-using-metrics) and [`Testing rule sets with player traffic using metrics`](https://developer.apple.com/documentation/GameKit/testing-rule-sets-with-player-traffic-using-metrics).

## Topics

### Getting match request metrics
- [Get rule-based match requests](get-v1-gamecenterdetails-_id_-metrics-rulebasedmatchmakingrequests.md)
  Get match requests that use matchmaking rules.
- [Get classic match requests](get-v1-gamecenterdetails-_id_-metrics-classicmatchmakingrequests.md)
  Get match requests that don’t use matchmaking rules.
### Getting rule results and errors
- [Get Boolean rule results](get-v1-gamecentermatchmakingrules-_id_-metrics-matchmakingbooleanruleresults.md)
  Get the results of a specific matchmaking rule that returns Boolean values.
- [Get numeric rule results](get-v1-gamecentermatchmakingrules-_id_-metrics-matchmakingnumberruleresults.md)
  Get the results of a specific matchmaking rule that returns numeric values.
- [Get matchmaking rule errors](get-v1-gamecentermatchmakingrules-_id_-metrics-matchmakingruleerrors.md)
  Get errors that occur for a specific matchmaking rule.
### Getting queue information
- [Get queue size](get-v1-gamecentermatchmakingqueues-_id_-metrics-matchmakingqueuesizes.md)
  Get the time that match requests are in a specific queue.
- [Get experimental queue size](get-v1-gamecentermatchmakingqueues-_id_-metrics-experimentmatchmakingqueuesizes.md)
  Get the number of match requests that the queue processes using its experimental rule set.
- [Get match request time in queue](get-v1-gamecentermatchmakingqueues-_id_-metrics-matchmakingrequests.md)
  Get the match requests that a specific queue processes.
- [Get experimental match request time in queue](get-v1-gamecentermatchmakingqueues-_id_-metrics-experimentmatchmakingrequests.md)
  Get the match requests that a specific queue processes using its experimental rule set.
- [Get queue session information](get-v1-gamecentermatchmakingqueues-_id_-metrics-matchmakingsessions.md)
  Get session information on a queue.
### Objects
- [object GameCenterMatchmakingAppRequestsV1MetricResponse](gamecentermatchmakingapprequestsv1metricresponse.md)
  The response body for fetching a match request.
- [object GameCenterMatchmakingBooleanRuleResultsV1MetricResponse](gamecentermatchmakingbooleanruleresultsv1metricresponse.md)
  The response body for fetching the results of applying Boolean rules.
- [object GameCenterMatchmakingNumberRuleResultsV1MetricResponse](gamecentermatchmakingnumberruleresultsv1metricresponse.md)
  The response body for fetching the results of applying numeric rules.
- [object GameCenterMatchmakingRuleErrorsV1MetricResponse](gamecentermatchmakingruleerrorsv1metricresponse.md)
  The response body for fetching the rule errors.
- [object GameCenterMatchmakingQueueSizesV1MetricResponse](gamecentermatchmakingqueuesizesv1metricresponse.md)
  The response body for fetching the queue sizes.
- [object GameCenterMatchmakingQueueRequestsV1MetricResponse](gamecentermatchmakingqueuerequestsv1metricresponse.md)
  The response body for match requests in a queue.
- [object GameCenterMatchmakingSessionsV1MetricResponse](gamecentermatchmakingsessionsv1metricresponse.md)
  The response body for information about a successful matchmaking session.

## See Also

- [Rules](rules.md)
  Manage the matchmaking rules that Game Center uses to find players.
- [Expressions](expressions.md)
  Write expressions that query the match requests in a queue to find the best players for a match.
- [Rule sets](rule-sets.md)
  Manage the rule sets that you add matchmaking rules and teams to.
- [Queues](queues.md)
  Manage the queues that contain matchmaking rule sets and that you submit match requests to.
- [Teams](teams.md)
  Manage the teams that you add to matchmaking rule sets.
- [Testing](testing.md)
  Test matchmaking rules using sample data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/metrics)*