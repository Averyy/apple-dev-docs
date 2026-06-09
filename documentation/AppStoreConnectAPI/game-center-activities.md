# Game Center activities

**Framework**: App Store Connect API

Manage Game Center activities for your apps.

#### Overview

Use the activities API to create and configure ways to link players directly to your content in your game. Once you create an activity you can link it to a challenge and a leaderboard. To learn more about challenges, see [`Configuring Game Center challenges`](configuring-game-center-challenges.md).

Activities provide a way to link players directly to your content. By describing your gameplay with activities, you can link the player to that part of your game when they engage with the activity. For example, when a player wants to complete your daily puzzle, you can send the player directly to that part of your game. To learn more about deep links and integrating activites in your game, see [Creating activities for your game] (https://developer.apple.com/documentation/gamekit/creating-activities-for-your-game).

To manage activities, be sure you have one of the following user roles:

- `ADMIN`
- `APP MANAGER`
- `MARKETING`

## Topics

### Managing Game Center activities
- [Create an Activity](post-v1-gamecenteractivities.md)
  Create an activity for your Game Center detail or Game Center group.
- [Add an Achievement to a Game Center Activity](post-v1-gamecenteractivities-_id_-relationships-achievementsv2.md)
  Add an achievement to a Game Center activity.
- [Add a Leaderboard to a Game Center Activity](post-v1-gamecenteractivities-_id_-relationships-leaderboardsv2.md)
  Add a leaderboard to a Game Center activity.
- [Modify the achievements for a game center activity](post-v1-gamecenteractivities-_id_-relationships-achievements.md)
  Update the relationship between achievements and a specific Game Center activity.
- [Modify the leaderboards for a game center activity](post-v1-gamecenteractivities-_id_-relationships-leaderboards.md)
  Update the relationship between a leaderboard and a specific Game Center activity.
- [Read Activity Information](get-v1-gamecenteractivities-_id_.md)
  Get information for a specific Game Center activity.
- [Read the Versions for an Activity](get-v1-gamecenteractivities-_id_-versions.md)
  Get a list of versions for a specific Game Center activity.
- [List version IDs for a Game Center activity](get-v1-gamecenteractivities-_id_-relationships-versions.md)
- [List all activities for a game center detail](get-v1-gamecenterdetails-_id_-gamecenteractivities.md)
  Get activity release information for a specific Game Center detail.
- [List Game Center activity IDs for a Game Center detail](get-v1-gamecenterdetails-_id_-relationships-gamecenteractivities.md)
- [List all activities for a game center group](get-v1-gamecentergroups-_id_-gamecenteractivities.md)
  Get a list of all activities for a Game Center group.
- [List activity IDs for a Game Center group](get-v1-gamecentergroups-_id_-relationships-gamecenteractivities.md)
  Get a list of activity IDs for a specific Game Center group.
- [Modify an Activity](patch-v1-gamecenteractivities-_id_.md)
  Update details for a specific Game Center activity.
- [Delete an Activity](delete-v1-gamecenteractivities-_id_.md)
  Remove a specific Game Center activity.
- [Remove an Achievement](delete-v1-gamecenteractivities-_id_-relationships-achievementsv2.md)
  Remove an achievement from a Game Center activity.
- [Remove a Leaderboard](delete-v1-gamecenteractivities-_id_-relationships-leaderboardsv2.md)
  Remove a leaderboard from a Game Center activity.
- [Remove an Achievement From an Activity](delete-v1-gamecenteractivities-_id_-relationships-achievements.md)
  Remove the relationship between an achievement and a Game Center activity.
- [Remove a Leaderboard From an Activity](delete-v1-gamecenteractivities-_id_-relationships-leaderboards.md)
  Remove the relationship between a leaderboard and a Game Center activity.
### Objects
- [object GameCenterActivitiesResponse](gamecenteractivitiesresponse.md)
  A response containing a list of Game Center activities configured for an app.
- [object GameCenterActivity](gamecenteractivity.md)
  A social or competitive event in Game Center that players can participate in, such as a leaderboard challenge.
- [object GameCenterActivityAchievementsV2LinkagesRequest](gamecenteractivityachievementsv2linkagesrequest.md)
  The data structure that represents a Game Center activity achievement linkage request resource.
- [object GameCenterActivityLeaderboardsV2LinkagesRequest](gamecenteractivityleaderboardsv2linkagesrequest.md)
  The data structure that represents a Game Center activity leaderboard linkage request resource.
- [object GameCenterActivityAchievementsLinkagesRequest](gamecenteractivityachievementslinkagesrequest.md)
  The request body for updating the list of achievements linked to a Game Center activity.
- [object GameCenterActivityLeaderboardsLinkagesRequest](gamecenteractivityleaderboardslinkagesrequest.md)
  The request body for updating the list of leaderboards linked to a Game Center activity.
- [object GameCenterActivityCreateRequest](gamecenteractivitycreaterequest.md)
  The request body for creating a new Game Center activity.
- [object GameCenterActivityVersionInlineCreate](gamecenteractivityversioninlinecreate.md)
  The data structure you use to configure an activity version while creating an activity.
- [object GameCenterActivityResponse](gamecenteractivityresponse.md)
  A response containing a single Game Center activity with its configuration.
- [object GameCenterActivityUpdateRequest](gamecenteractivityupdaterequest.md)
  The request body you use to update an activity.
- [object GameCenterActivityVersion](gamecenteractivityversion.md)
  A versioned configuration of a Game Center activity, containing its localizations and release status.
- [object GameCenterActivityVersionCreateRequest](gamecenteractivityversioncreaterequest.md)
  The request body for creating a version of a Game Center activity.
- [object GameCenterActivityLocalizationImageLinkageResponse](gamecenteractivitylocalizationimagelinkageresponse.md)
- [object StringToStringMap](stringtostringmap.md)
  A dictionary object mapping arbitrary string keys to string values, used for flexible key-value metadata.

## See Also

- [Configuring Game center activities](configuring-game-center-activities.md)
  Setup and configure a way for players to compete on a specific task or part of your game.
- [Game Center activity versions](game-center-activity-versions.md)
  Manage versions for your Game Center activities.
- [Game Center activity version releases](game-center-activity-version-releases.md)
  Manage version releases for your Game Center activities.
- [Game Center activity localizations](game-center-activity-localizations.md)
  Manage localizations for your Game Center activities.
- [Game Center activity images](game-center-activity-images.md)
  Manage images for your Game Center activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-activities)*