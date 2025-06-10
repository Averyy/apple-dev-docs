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
- [Read the versions for an activity](get-v1-gamecenteractivities-_id_-versions.md)
  Get a list of versions for a specific Game Center activity.
- [GET /v1/gameCenterActivities/{id}/relationships/versions](get-v1-gamecenteractivities-_id_-relationships-versions.md)
- [Read activity version information](get-v1-gamecenteractivityversions-_id_.md)
  Get information for a specific Game Center activity version.
- [Read default image information for an activity version](get-v1-gamecenteractivityversions-_id_-defaultimage.md)
  Get details about the default image for a specific Game Center activity version.
- [GET /v1/gameCenterActivityVersions/{id}/relationships/defaultImage](get-v1-gamecenteractivityversions-_id_-relationships-defaultimage.md)
- [List all localizations for an activity version](get-v1-gamecenteractivityversions-_id_-localizations.md)
  Get details about the default localization for a specific Game Center activity version.
- [GET /v1/gameCenterActivityVersions/{id}/relationships/localizations](get-v1-gamecenteractivityversions-_id_-relationships-localizations.md)
- [Add an activity version release](post-v1-gamecenteractivityversionreleases.md)
  Add a version release for a specific Game Center activity.
- [Create an activity version](post-v1-gamecenteractivityversions.md)
  Add an activity to a Game Center detail, group, or leaderboard.
- [Modify an activity version](patch-v1-gamecenteractivityversions-_id_.md)
  Update a specific activity version.
### Objects
- [object GameCenterActivityVersion](gamecenteractivityversion.md)
  The data structure that represents an activity version resource.
- [object GameCenterActivityVersionCreateRequest](gamecenteractivityversioncreaterequest.md)
  The request body you use to create an activity version resource.
- [object GameCenterActivityVersionResponse](gamecenteractivityversionresponse.md)
  A response that contains a single activity version resource.
- [object GameCenterActivityVersionUpdateRequest](gamecenteractivityversionupdaterequest.md)
  The request body you use to update an activity version version.
- [object GameCenterActivityVersionsResponse](gamecenteractivityversionsresponse.md)
  A response that contains a list of activity version resources.
- [object GameCenterActivityVersionDefaultImageLinkageResponse](gamecenteractivityversiondefaultimagelinkageresponse.md)
- [object GameCenterActivityVersionLocalizationsLinkagesResponse](gamecenteractivityversionlocalizationslinkagesresponse.md)
- [object GameCenterActivityVersionUpdateRequest](gamecenteractivityversionupdaterequest.md)
  The request body you use to update an activity version version.
- [object GameCenterActivityVersionsLinkagesResponse](gamecenteractivityversionslinkagesresponse.md)
  A response that contains a list of Ids of related resources.
- [object GameCenterActivityVersionsResponse](gamecenteractivityversionsresponse.md)
  A response that contains a list of activity version resources.

## See Also

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