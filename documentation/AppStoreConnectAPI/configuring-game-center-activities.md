# Configuring Game center activities

**Framework**: App Store Connect API

Setup and configure a way for players to compete on a specific task or part of your game.

#### Overview

Use the activities API to create and configure ways to link players directly to content in your game. Once you create an activity you can link it to a challenge. To learn more about challenges, see [`Configuring Game Center challenges`](configuring-game-center-challenges.md).

Activities provide a way to link players directly to your content. By describing your gameplay with activities, you can link the player to that part of your game when they engage with the activity. For example, when a player wants to complete your daily puzzle, you can send the player directly to that part of your game. To learn more about deep links, see [`Creating activities for your game`](https://developer.apple.comhttps://developer.apple.com/documentation/gamekit/creating-activities-for-your-game#Add-universal-link-support).

Before you begin creating your activities, you need these items:

- Game center enable in your binary
- Game Center detail enabled

##### Create the Activity

Begin creating the activity by using the [`Create an activity`](post-v1-gamecenteractivities.md) endpoint. Provide these attributes in your payload:

Additionally provide a relationship to a `gameCenterDetail` or a `gameCenterGroup`. If your leaderboard is in a Game Center group, use `gameCenterGroup`. If you’re relating this activity to a Game Center group, you need to use the `grp.` prefix.

When you create an activity you use a payload like this:

```json
{
  "data": {
    "type": "gameCenterActivities",
    "attributes": {
      "referenceName": "string",
      "vendorIdentifier": "string",
      "minimumPlayersCount": 1,
      "maximumPlayersCount": 8,
      "supportsPartyCode": false
    },
    "relationships": {
      "gameCenterDetail": {
        "data": {
          "type": "gameCenterDetails",
          "id": "string"
        }
      }
    }
  }
}
```

In the response you get an `id` in the top-level data object. This `id` represents the Game Center activity. You can find this `id` at anytime using [`List all activities for a Game Center detail`](get-v1-gamecenterdetails-_id_-gamecenteractivities.md) or [`List all activities for a Game Center group`](get-v1-gamecentergroups-_id_-gamecenteractivities.md) for a grouped app.

##### Create the Activity Version

You next need to create a version for your Game center activity. The version is the parent object for localizations, the `fallbackUrl` and the activity image. Create the activity version using [`Create an activity version`](post-v1-gamecenteractivityversions.md). The `fallbackUrl` is what the system uses to support operating systems before iOS 26, macOS 26, and tvOS 26, to direct a player to an invitation page on the web. To learn more about deep links and `fallbackUrl`, see [`Creating activities for your game`](https://developer.apple.comhttps://developer.apple.com/documentation/gamekit/creating-activities-for-your-game#Add-universal-link-support).

```json
{
  "data": {
    "type": "gameCenterActivityVersions",
    "attributes": {
      "fallbackUrl": "string"
    },
    "relationships": {
      "activity": {
        "data": {
          "type": "gameCenterActivities",
          "id": "string"
        }
      }
    }
  }
}
```

> **Note**: The system uses the activity version `id` in this response in the version localization, so this `id` is  a possible relationship to the activity image.

##### Add an Activity Version Localization

You next add an activity version localization by using [`Add an activity localization`](post-v1-gamecenteractivitylocalizations.md). The `locale` and `name` attributes are required. The `name` represent the label shown for the activity inside the Games app. For a list of possible `locale` values, see [`Managing metadata in your app by using locale shortcodes`](managing-metadata-in-your-app-by-using-locale-shortcodes.md). The `description` attribute is optional but can help a player better understand the activity. The localization requires a relationship to its parent activity version. At minimum, one activity version localization is required for submission to review.

Use a payload like this:

```json
{
"data": {
  "type": "gameCenterActivityLocalizations",
  "attributes": {
    "locale": "string",
    "name": "string",
    "description": "string"
  },
  "relationships": {
    "version": {
      "data": {
        "type": "gameCenterActivityVersions",
        "id": "string"
      }
    }
  }
}
}
```

##### Add the Activity Version Image

Adding a default activity image is very similar to adding an app store screenshot or app review image. You can associate the activity version default image with an activity version or an activity localization. When you create a new activity version, the default image is inherited. At minimum, a default image is required for submission to review.

Start by using [`Create an activity image`](post-v1-gamecenteractivityimages.md) with a payload that looks like this:

```json
{
  "data": {
    "type": "gameCenterActivityImages",
    "attributes": {
      "fileSize": 0,
      "fileName": "string"
    },
    "relationships": {
      "version": {
        "data": {
          "type": "gameCenterActivityVersions",
          "id": "string"
        }
      }
    }
  }
}
```

The response includes one or more `PUT` requests; use these URL’s to upload your image.

After uploading, use [`Commit an image for an activity`](patch-v1-gamecenteractivityimages-_id_.md) to commit your image to the related resource with a payload like this:

```json
{
  "data": {
    "type": "gameCenterActivityImages",
    "id": "string",
    "attributes": {
      "uploaded": true
    }
  }
}
```

To learn more uploading images, see [`Uploading Assets to App Store Connect`](uploading-assets-to-app-store-connect.md).

##### Relate Your Activity to a Leaderboard

If your activity is not a multiplayer activity, it must be have a relationship to a leaderboard. If you don’t have an existing or appropriate leaderboard for your activity, you can create one using [`Create a leaderboard`](post-v1-gamecenterleaderboards.md). A multiplayer activity, using the `supportsPartyCode` attribute, can be used as a lobby for a group game session.  When you’re ready to relate your activity to your leaderboard, use [`PATCH /v1/gameCenterLeaderboards/{id}/relationships/activity`](patch-v1-gamecenterleaderboards-_id_-relationships-activity.md) with the Game Center leaderboard `id` in the request URL and with a payload like this:

```json
{
  "data": {
    "type": "gameCenterActivities",
    "id": "string"
  }
}
```

##### Submit Your Activity Version for Review

> **Note**: One localization and a default image are required for submission.

Now, you’re ready to submit your activity version for review. Use [`Add an activity version release`](post-v1-gamecenteractivityversionreleases.md) to attach your activity version to a `gameCenterDetail`. To find the `gameCenterDetail` id, use [`Read the state of Game Center for an app`](get-v1-apps-_id_-gamecenterdetail.md). Then, use [`Create a review submission`](post-v1-reviewsubmissions.md) to send the `appStoreVersion`, and your associated activity version to app review.

Use a payload like this:

```json
{
  "data": {
    "type": "gameCenterActivityVersionReleases",
    "relationships": {
      "gameCenterDetail": {
        "data": {
          "type": "gameCenterDetails",
          "id": "string"
        }
      },
      "version": {
        "data": {
          "type": "gameCenterActivityVersions",
          "id": "string"
        }
      }
    }
  }
}
```

> 💡 **Tip**: Read a list of the past activity version releases using [`Get activity releases for a Game Center detail`](get-v1-gamecenterdetails-_id_-activityreleases.md). Use the optional include `version` to get more details and to read the `id` of the Game Center activity version that is currently `LIVE`.

## See Also

- [Game Center activities](game-center-activities.md)
  Manage Game Center activities for your apps.
- [Game Center activity versions](game-center-activity-versions.md)
  Manage versions for your Game Center activities.
- [Game Center activity version releases](game-center-activity-version-releases.md)
  Manage version releases for your Game Center activities.
- [Game Center activity localizations](game-center-activity-localizations.md)
  Manage localizations for your Game Center activities.
- [Game Center activity images](game-center-activity-images.md)
  Manage images for your Game Center activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/configuring-game-center-activities)*