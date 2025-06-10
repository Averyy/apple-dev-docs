# Read age rating declaration

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the age rating declaration for the app info.

**Availability**:
- App Store Connect API 1.4+

## Mentions

- [App Store Connect API 4.0 release notes](app-store-connect-api-4-0-release-notes.md)

#### Discussion

Responses for this endpoint include `contests` or `gambling` properties. In an app that has a `FREQUENT_OR_INTENSE` declaration for contests, the age rating for the `AppInfos` is 12+. If you declare a value of true for `gambling`, the age rating for the `AppInfos` is 17+.

##### Read the Age Rating Declaration

## See Also

- [GET /v1/appInfos/{id}/relationships/ageRatingDeclaration](get-v1-appinfos-_id_-relationships-ageratingdeclaration.md)
- [Modify an Age Rating Declaration](patch-v1-ageratingdeclarations-_id_.md)
  Provide age-related information so the App Store can determine the age rating for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_-ageratingdeclaration)*