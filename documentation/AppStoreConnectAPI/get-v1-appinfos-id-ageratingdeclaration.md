# Read age rating declaration

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the age rating declaration for the app info.

**Availability**:
- App Store Connect API 1.4+

#### Discussion

Responses for this endpoint include the `gamblingAndContests` attribute for legacy clients. For new clients, use `contents` or `gambling` properties instead. For example, in an app that has a `FREQUENT_OR_INTENSE` declaration for contests, the age rating for the `AppInfos` is 12+. If you declare a value of true for `gamblingAndContests` instead, the age rating for the `AppInfos` is 17+.

> ❗ **Important**:  The `gamblingAndContests` property is deprecated. Use the `contests` or `gambling` properties instead.

 The `gamblingAndContests` property is deprecated. Use the `contests` or `gambling` properties instead.

##### Read the Age Rating Declaration


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_-ageratingdeclaration)*