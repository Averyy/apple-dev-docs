# Game Center activity versions

**Framework**: App Store Connect API

Manage versions for your Game Center activities.

#### Overview

To manage Game Center activity versions, be sure you have one of the following user roles:

- `ADMIN`
- `APP MANAGER`
- `MARKETING`

## Topics

### Read, create, and update Game Center activity versions
- [Read the Versions for an Activity](get-v1-gamecenteractivities-_id_-versions.md)
  Get a list of versions for a specific Game Center activity.
- [List version IDs for a Game Center activity](get-v1-gamecenteractivities-_id_-relationships-versions.md)
- [Read Activity Version Information](get-v1-gamecenteractivityversions-_id_.md)
  Get information for a specific Game Center activity version.
- [Read Default Image Information for an Activity Version](get-v1-gamecenteractivityversions-_id_-defaultimage.md)
  Get details about the default image for a specific Game Center activity version.
- [Get the default image ID for a Game Center activity version](get-v1-gamecenteractivityversions-_id_-relationships-defaultimage.md)
- [List All Localizations for an Activity Version](get-v1-gamecenteractivityversions-_id_-localizations.md)
  Get details about the default localization for a specific Game Center activity version.
- [List localization IDs for a Game Center activity version](get-v1-gamecenteractivityversions-_id_-relationships-localizations.md)
- [Add an Activity Version Release](post-v1-gamecenteractivityversionreleases.md)
  Add a version release for a specific Game Center activity.
- [Create an Activity Version](post-v1-gamecenteractivityversions.md)
  Add an activity to a Game Center detail, group, or leaderboard.
- [Modify an Activity Version](patch-v1-gamecenteractivityversions-_id_.md)
  Update a specific activity version.
### Objects
- [object GameCenterActivityVersion](gamecenteractivityversion.md)
  A versioned configuration of a Game Center activity, containing its localizations and release status.
- [object GameCenterActivityVersionCreateRequest](gamecenteractivityversioncreaterequest.md)
  The request body for creating a version of a Game Center activity.
- [object GameCenterActivityVersionResponse](gamecenteractivityversionresponse.md)
  A response containing a single version of a Game Center activity.
- [object GameCenterActivityVersionUpdateRequest](gamecenteractivityversionupdaterequest.md)
  The request body you use to update an activity version version.
- [object GameCenterActivityVersionsResponse](gamecenteractivityversionsresponse.md)
  A response containing a list of versions for a Game Center activity.
- [object GameCenterActivityVersionDefaultImageLinkageResponse](gamecenteractivityversiondefaultimagelinkageresponse.md)
- [object GameCenterActivityVersionLocalizationsLinkagesResponse](gamecenteractivityversionlocalizationslinkagesresponse.md)
- [object GameCenterActivityVersionUpdateRequest](gamecenteractivityversionupdaterequest.md)
  The request body you use to update an activity version version.
- [object GameCenterActivityVersionsLinkagesResponse](gamecenteractivityversionslinkagesresponse.md)
  A response containing the resource identifiers of versions for a Game Center activity.
- [object GameCenterActivityVersionsResponse](gamecenteractivityversionsresponse.md)
  A response containing a list of versions for a Game Center activity.

## See Also

- [Configuring Game center activities](configuring-game-center-activities.md)
  Setup and configure a way for players to compete on a specific task or part of your game.
- [Game Center activities](game-center-activities.md)
  Manage Game Center activities for your apps.
- [Game Center activity version releases](game-center-activity-version-releases.md)
  Manage version releases for your Game Center activities.
- [Game Center activity localizations](game-center-activity-localizations.md)
  Manage localizations for your Game Center activities.
- [Game Center activity images](game-center-activity-images.md)
  Manage images for your Game Center activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/game-center-activity-versions)*