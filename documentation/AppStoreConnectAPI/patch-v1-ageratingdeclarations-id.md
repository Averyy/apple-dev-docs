# Modify an Age Rating Declaration

**Framework**: App Store Connect API  
**Kind**: httpRequest

Provide age-related information so the App Store can determine the age rating for your app.

**Availability**:
- App Store Connect API 1.2+

## Mentions

- [App Store Connect API 3.6 release notes](app-store-connect-api-3-6-release-notes.md)

#### Discussion

Every app store version has an age rating declaration. Use this endpoint to edit the declaration and provide app-characteristic information so App Store Connect can determine the appropriate age rating for the app.

Use this endpoint to indicate whether an app is Made for Kids.

When calling this endpoint, only include the attributes that you’re modifying.

> ❗ **Important**:  The `gamblingAndContests` property is deprecated. Use the `contests` or `gambling` properties instead.

 The `gamblingAndContests` property is deprecated. Use the `contests` or `gambling` properties instead.

For example, in an app that has a `FREQUENT_OR_INTENSE` declaration for contests, the age rating for the `AppInfos` is 12+. If you declare a value of true for `gamblingAndContests` instead, the age rating for the `AppInfos` is 17+.

##### Modify an Age Rating Declaration

##### Mark an App As Made for Kids

## Request Body

The request body you use to update an Age Rating Declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-ageratingdeclarations-_id_)*