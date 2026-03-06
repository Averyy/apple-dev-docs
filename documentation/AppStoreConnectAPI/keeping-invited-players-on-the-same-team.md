# Keeping invited players on the same team

**Framework**: App Store Connect API

Return a Boolean value that indicates whether players in the same match requests are on the same team.

##### Declaration

```other
boolean hasInvitedPlayersOnSameTeam(array[object] $teams, array[object] $players)
```

##### Parameters

- **`teams`**: The teams in the rule set. Pass the `teams` array that’s available in team rule expressions.
- **`players`**: The players that the rule applies to. Pass the `players` array that’s available in team rule expressions.

##### Return Value

`true` if the players in the same match requests are on the same team; otherwise, `false`. The players in a match request include the local player and any recipients or other players that the local player invites.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/keeping-invited-players-on-the-same-team)*