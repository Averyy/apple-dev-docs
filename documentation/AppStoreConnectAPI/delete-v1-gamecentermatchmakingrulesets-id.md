# Delete a Rule Set

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a rule set along with its matchmaking rules and teams.

**Availability**:
- App Store Connect API 3.1+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/gameCenterMatchmakingRuleSets/{id}`

## Parameters

- `id` (string) *(required)*: A unique identifier for the rule set.

## See Also

- [Create a Rule Set](post-v1-gamecentermatchmakingrulesets.md)
  Create a rule set to contain matchmaking rules and teams.
- [Modify a Rule Set](patch-v1-gamecentermatchmakingrulesets-_id_.md)
  Update the attributes of a rule set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-gamecentermatchmakingrulesets-_id_)*