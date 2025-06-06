# Expressions

**Framework**: App Store Connect API

Write expressions that query the match requests in a queue to find the best players for a match.

#### Overview

An  is a [`JMESPath`](https://developer.apple.comhttps://jmespath.org/) formatted string with additional matchmaking rule functions. Game Center uses the expression to query a collection of match requests represented as JSON. The expression needs to evaluate to either a Boolean or number value according to the rule type.

To create a matchmaking rule in Game Center, you pass an expression to the [`Create a rule`](post-v1-gamecentermatchmakingrules.md) endpoint. Set the `expression` and `type` fields of the [`GameCenterMatchmakingRuleCreateRequest.Data.Attributes`](gamecentermatchmakingrulecreaterequest/data-data.dictionary/attributes-data.dictionary.md) object that you pass in the request.

For example, if players can only join matches that run the same version of your game, add a compatible rule that compares the app versions. If you set the rule’s `type` field to `COMPATIBLE`, the `requests` array in the JSON input to the expression contains two match requests to compare. In the expression, use the `areCompatibleAppVersions()` function that returns `true` if the app versions are compatible.

```other
areCompatibleAppVersions(requests[0], requests[1])
```

You can improve the game experience by prioritizing matches between players who are geographically close, resulting in lower latency when sending messages between devices. If you set the rule’s `type` field to `DISTANCE`, the `requests` array in the expression contains two match requests to compare. In the expression, use the `geoLatency()` function that returns a range between `0.0` and `1.0`, where `0.0` is in the local area:

```other
geoLatency(requests[0], requests[1])
```

The JSON input to an expression contains the following arrays, that you can use in expressions, depending on the rule type:

| Array | Description |
| --- | --- |
| `players` | An array of [`Player`](player.md) objects representing the players associated with the requests.  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Available in all types of rule expressions. |
| `requests` | An array of [`Request`](request.md) objects representing the match requests that you compare in an expression.  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Available in all types of rule expressions. In compatible and distance rules, contains two items for comparison. In match and team rules, contains two or more items. |
| `teams` | An array of [`Team`](team.md) objects representing the teams that you add to a rule set, including the players assigned to the teams.  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Available only in team rule expressions. |

## Topics

### Comparison functions
- [Comparing app versions](comparing-app-versions.md)
  Return a Boolean value that indicates whether two match requests are from compatible app versions.
### Distance functions
- [Getting geographic distance](getting-geographic-distance.md)
  Return the relative geographic distance between two match requests.
### Match functions
- [Getting value based on age](getting-value-based-on-age.md)
  Return a value that changes in regular steps as a function of the age of the requests.
- [Getting value based on age using an array](getting-value-based-on-age-using-an-array.md)
  Return a value that changes according to an array of values as a function of the age of the requests.
### Team functions
- [Keeping invited players on the same team](keeping-invited-players-on-the-same-team.md)
  Return a Boolean value that indicates whether players in the same match requests are on the same team.
### Boolean functions
- [Evaluating a Boolean value](evaluating-a-boolean-value.md)
  Return given values for true and false results of a conditional.
### Numeric functions
- [Dividing numbers](dividing-numbers.md)
  Return the result of dividing one number into another.
- [Subtracting numbers](subtracting-numbers.md)
  Return the result of subtracting two numbers.
### Array functions
- [Converting arrays to sets](converting-arrays-to-sets.md)
  Return the content of a list, with duplicates removed and sorted, so that you can compare it to another set.
- [Computing numeric differences](computing-numeric-differences.md)
  Return the absolute difference between the maximum and minimum numerical values in an array.
- [Intersecting sets](intersecting-sets.md)
  Return the intersection of two or more arrays treated as sets.
### Objects
- [Request](request.md)
  An object that represents a match request in a queue.
- [Player](player.md)
  An object that represents a player associated with a match request.
- [Team](team.md)
  A team that you add to a rule set.

## See Also

- [Rules](rules.md)
  Manage the matchmaking rules that Game Center uses to find players.
- [Rule sets](rule-sets.md)
  Manage the rule sets that you add matchmaking rules and teams to.
- [Queues](queues.md)
  Manage the queues that contain matchmaking rule sets and that you submit match requests to.
- [Teams](teams.md)
  Manage the teams that you add to matchmaking rule sets.
- [Testing](testing.md)
  Test matchmaking rules using sample data.
- [Metrics](metrics.md)
  Analyze data about matchmaking rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/expressions)*