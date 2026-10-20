# BetaGroupUpdateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes whose values you’re changing as part of the beta group update request.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaGroupUpdateRequest.Data.Attributes
```

## Mentions

- [App Store Connect API 1.6 release notes](app-store-connect-api-1-6-release-notes.md)

## Properties

- `name` (string): The name for the beta group.
- `publicLinkEnabled` (boolean): Only applicable to external groups. A Boolean value that indicates whether a public link is enabled. Enable a link to invite anyone outside of your team to beta test your app. When you share this link, testers can install the beta version of your app on their devices in TestFlight and share the link with others.
- `publicLinkLimit` (integer): Only applicable to external groups. The maximum number of testers that can join this beta group using the public link. Values must be between 1 and 10,000.
- `publicLinkLimitEnabled` (boolean): Only applicable to external groups.  A Boolean value that limits the number of testers who can join the beta group using the public link.
- `feedbackEnabled` (boolean)
- `iosBuildsAvailableForAppleSiliconMac` (boolean)
- `iosBuildsAvailableForAppleVision` (boolean)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betagroupupdaterequest/data-data.dictionary/attributes-data.dictionary)*