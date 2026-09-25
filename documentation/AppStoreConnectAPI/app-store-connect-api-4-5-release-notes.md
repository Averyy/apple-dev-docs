# App Store Connect API 4.5 release notes

**Framework**: App Store Connect API

Update your server-side code to use new features, and test your code against API changes.

#### Overview

App Store Connect API version 4.5 provides resources that enable you to automate actions you take in App Store Connect.

#### Added

- Evaluate your app’s performance before you release an update. Use [`Get the performance overview for an app`](get-v1-apps-_id_-performanceoverviews.md) to read the aggregated performance overview data for an app, including the metrics Xcode surfaces in its performance reports.
- Offer subscriptions to organizations. The `marketSettings` and `multiSeatStatus` attributes on [`Subscription`](subscription.md) indicate the markets where a subscription is available — the App Store, Apple School Manager, or Apple Business Manager — and whether the subscription supports multiple seats.
- Moderate Game Center leaderboard scores and the players who submit them. Use [`List Score Moderations for a Leaderboard`](get-v2-gamecenterleaderboards-_id_-gamecenterscoremoderations.md) to review the scores submitted to a leaderboard and [`Modify a Game Center Score Moderation`](patch-v1-gamecenterscoremoderations-_id_.md) to block a score. Read the players a game blocks with [`List Blocked Players`](get-v1-gamecenterdetails-_id_-blockedplayers.md), and block or unblock an individual player with [`Modify a Game Center Detail Player`](patch-v1-gamecenterdetailplayers-_id_.md).
- Align your app with Korea’s age-rating classifications. Use the `ALL` and `TWELVE_PLUS` values in the `koreaAgeRatingOverride` attribute of [`AgeRatingDeclaration`](ageratingdeclaration.md) to set the most accurate age-rating classification.

#### Deprecated

- The `territories` relationship on app tags is now deprecated, along with the [`List Territories for an App Tag`](get-v1-apptags-_id_-territories.md) and [`List territory IDs for an app tag`](get-v1-apptags-_id_-relationships-territories.md) endpoints. On [`List App Tags`](get-v1-apps-_id_-apptags.md), the `include`, `fields[appTags]`, `fields[territories]`, and `limit[territories]` parameters no longer accept `territories` values.

## See Also

- [App Store Connect API 4.4.1 release notes](app-store-connect-api-4-4-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.4 release notes](app-store-connect-api-4-4-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.3.1 release notes](app-store-connect-api-4-3-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.3 release notes](app-store-connect-api-4-3-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-4-5-release-notes)*