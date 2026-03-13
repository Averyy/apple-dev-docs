# App Store Connect API 4.3 release notes

**Framework**: App Store Connect API

Update your server-side code to use new features, and test your code against API changes.

#### Overview

App Store Connect API version 4.3 provides resources that enable you to automate actions you take in App Store Connect.

##### New Features

- To get the size usage of a background asset, reference the `usedBytes` attribute on [`BackgroundAsset.Attributes`](backgroundasset/attributes-data.dictionary.md).
- To specify the initial `gameCenterChallengeVersion` when creating a challenge, call [`Create a challenge`](post-v1-gamecenterchallenges.md) using [`GameCenterChallengeVersionInlineCreate`](gamecenterchallengeversioninlinecreate.md).
- To specify the initial `gameCenterActivityVersion` when creating an activity, call [`Create an activity`](post-v1-gamecenteractivities.md) using [`GameCenterActivityVersionInlineCreate`](gamecenteractivityversioninlinecreate.md). You can also specify a `fallbackUrl` for the initial activity version during the operation.
- Use the `preReleased` attribute with [`Add a player's score`](post-v1-gamecenterplayerachievementsubmissions.md) and [`Add a score to a leaderbaord`](post-v1-gamecenterleaderboardentrysubmissions.md) to indicate whether the requested change applies to the game’s release version or its prerelease version.

##### Deprecations

- The user role permission `ACCESS_TO_REPORTS` for App Store Connect API is deprecated.  See [`UserRole`](userrole.md) for available alternatives.

##### Removals

- Removed the endpoints `GET /v1/appStoreVersions/{id}/relationships/ageRatingDeclaration` and `GET /v1/appStoreVersions/{id}/ageRatingDeclaration`. Use [`Read age rating declaration`](get-v1-appinfos-_id_-ageratingdeclaration.md) instead.

## See Also

- [App Store Connect API 4.2 release notes](app-store-connect-api-4-2-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.1 release notes](app-store-connect-api-4-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.0 release notes](app-store-connect-api-4-0-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.8 release notes](app-store-connect-api-3-8-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.7 release notes](app-store-connect-api-3-7-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.6 release notes](app-store-connect-api-3-6-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.5 release notes](app-store-connect-api-3-5-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.4 release notes](app-store-connect-api-3-4-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.3 release notes](app-store-connect-api-3-3-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.2 release notes](app-store-connect-api-3-2-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.1 release notes](app-store-connect-api-3-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.0 release notes](app-store-connect-api-3-0-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 2.4 release notes](app-store-connect-api-2-4-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 2.3 release notes](app-store-connect-api-2-3-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 2.2 release notes](app-store-connect-api-2-2-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-4-3-release-notes)*