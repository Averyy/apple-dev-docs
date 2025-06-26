# Configuring Game Center challenges

**Framework**: App Store Connect API

Setup and configure social experiences around leaderboards for friendly competition.

#### Overview

Use the challenges API to create and configure ways to link players directly to your content in your game. Once you create a challenge, you can link it an activity, by relating the activity to the challenge’s leaderboard. To learn more about activities, see [`Configuring Game center activities`](configuring-game-center-activities.md).

Challenges encourage your players to invite their friends into your game for friendly competitions in score-based rounds. Players will see challenges promoted throughout the Games app and other places around the OS as suggestions for enjoying their games with friends. They can invite their Game Center friends and anyone from their contacts, see scores appear in real-time, get notified at key moments until a winner is crowned, and have a rematch. Challenges are built on top of leaderboards, turning single-player game activities into a social experience players can share with their friends.

Before you begin creating your challenges, you need these items:

- An approved or draft leaderboard for your game
- Game Center enabled in your binary
- Game Center detail enabled

##### Create the Challenge

Begin creating the challenge by using the [`Create a challenge`](post-v1-gamecenterchallenges.md) endpoint. Provide these attributes in your payload:

Additionally provide:

- A relationship to a `leaderboard` - Obtain the leaderboard resource ID from the [`List leaderboards`](get-v1-gamecenterdetails-_id_-relationships-gamecenterleaderboards.md) or [`Read the leaderboards in a group`](get-v1-gamecentergroups-_id_-relationships-gamecenterleaderboards.md) response.
- A relationship to a `gameCenterDetail` or a `gameCenterGroup` - If your leaderboard is in a Game Center group, use `gameCenterGroup`.
- If you’re relating this challenge to a Game Center group, you need to use the `grp.` prefix.

When you create a challenge you use a payload like this:

```json
{
  "data": {
    "type": "gameCenterChallenges",
    "attributes": {
      "referenceName": "string",
      "vendorIdentifier": "string",
      "allowedDurations": [
        "ONE_DAY","THREE_DAYS","ONE_WEEK"
      ],
      "challengeType": "LEADERBOARD",
      "repeatable": false
    },
    "relationships": {
      "gameCenterDetail": {
        "data": {
          "type": "gameCenterDetails",
          "id": "string"
        }
      },
      "leaderboard": {
        "data": {
          "type": "gameCenterLeaderboards",
          "id": "string"
        }
      }
    }
  }
}
```

In the response you get an `id` in the top-level data object. This `id` represents the Game Center challenge. You can find this `id` at anytime using [`Read the challenges for a Game Center detail`](get-v1-gamecenterdetails-_id_-gamecenterchallenges.md).

##### Create the Challenge Version

Next, you need to create a version for your Game Center challenge. The version is the parent object for localizations and the challenge default image. Create the challenge version using [`Create a challenge version`](post-v1-gamecenterchallengeversions.md).

```json
{
  "data": {
    "type": "gameCenterChallengeVersions",
    "relationships": {
      "challenge": {
        "data": {
          "type": "gameCenterChallenges",
          "id": "string"
        }
      }
    }
  }
}
```

> **Note**: The system uses the challenge version `id` in this response in the version localization, so this `id` is a possible relationship to the challenge image.

##### Add a Challenge Version Localization

You next add a challenge version localization by using [`Add a challenge localization`](post-v1-gamecenterchallengelocalizations.md). The `locale` and `name` attributes are required. The `name` represent the label shown for the activity inside the Games app. For a list of possible `locale` values, see [`Managing metadata in your app by using locale shortcodes`](managing-metadata-in-your-app-by-using-locale-shortcodes.md). The `description` attribute is optional but can help a player better understand the challenge. The localization requires a relationship to its parent challenge version. At minimum, one challenge version localization is required for submission to review.

Use a payload like this:

```json
{
  "data": {
    "type": "gameCenterChallengeLocalizations",
    "attributes": {
      "locale": "string",
      "name": "string",
      "description": "string"
    },
    "relationships": {
      "version": {
        "data": {
          "type": "gameCenterChallengeVersions",
          "id": "string"
        }
      }
    }
  }
}
```

##### Add the Challenge Version Image

Adding a default challenge image is very similar to adding an app store screenshot or app review image. You can associate the challenge version default image with a challenge version or a challenge localization. When you create a new challenge version the default image is inherited. At minimum, one challenge version image is required for submission to review.

Start by using [`Create a challenge image`](post-v1-gamecenterchallengeimages.md) with a payload that looks like this:

```json
{
  "data": {
    "type": "gameCenterChallengeImages",
    "attributes": {
      "fileSize": 0,
      "fileName": "string"
    },
    "relationships": {
      "version": {
        "data": {
          "type": "gameCenterChallengeVersions",
          "id": "string"
        }
      }
    }
  }
}
```

The response includes one or more `PUT` requests; use these URL’s to upload your image.

After uploading, use [`Commit an image for a challenge`](patch-v1-gamecenterchallengeimages-_id_.md) to commit your image to the related resource with a payload like this:

```json
{
  "data": {
    "type": "gameCenterChallengeImages",
    "id": "string",
    "attributes": {
      "uploaded": true
    }
  }
}
```

To learn more uploading images, see [`Uploading Assets to App Store Connect`](uploading-assets-to-app-store-connect.md).

##### Submit Your Challenge Version for Review

> **Note**: One localization and a default image are required for submission.

Now, you’re ready to submit your challenge version for review. Use [`Add a challenge version release`](post-v1-gamecenterchallengeversionreleases.md) to attach your challenge version to a `gameCenterDetail`. To find the `gameCenterDetail` id, use [`Read the state of Game Center for an app`](get-v1-apps-_id_-gamecenterdetail.md). Then, use [`Create a review submission`](post-v1-reviewsubmissions.md) to send the `appStoreVersion`, and your associated challenge version to app review.

Use a payload like this:

```json
{
  "data": {
    "type": "gameCenterChallengeVersionReleases",
    "relationships": {
      "gameCenterDetail": {
        "data": {
          "type": "gameCenterDetails",
          "id": "string"
        }
      },
      "version": {
        "data": {
          "type": "gameCenterChallengeVersions",
          "id": "string"
        }
      }
    }
  }
}
```

> 💡 **Tip**: You can read a list of the past challenge version releases and their states using [`Get challenge releases for a Game Center detail`](get-v1-gamecenterdetails-_id_-challengereleases.md). Use the optional include `version` to get more details and to read the `id` of the Game Center challenge version that is currently `LIVE`.

## See Also

- [Game Center challenges](game-center-challenges.md)
  Manage Game Center challenges for your apps.
- [Game Center challenge versions](game-center-challenges-versions.md)
  Manage compatible Game Center challenge versions.
- [Game Center challenge version releases](game-center-challenges-version-releases.md)
  Manage compatible Game Center challenge version releases.
- [Game Center challenges localizations](game-center-challenges-localizations.md)
  Manage compatible Game Center-enabled versions.
- [Game Center challenge images](game-center-challenge-images.md)
  Manage image assets for your Game Center challenges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/configuring-game-center-challenges)*