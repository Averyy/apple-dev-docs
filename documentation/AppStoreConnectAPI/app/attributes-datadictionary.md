# App.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe an Apps resource.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object App.Attributes
```

## Mentions

- [App Store Connect API 1.6 release notes](app-store-connect-api-1-6-release-notes.md)
- [App Store Connect API 4.0 release notes](app-store-connect-api-4-0-release-notes.md)
- [App Store Connect API 4.1 release notes](app-store-connect-api-4-1-release-notes.md)

## Properties

- `bundleId` (string): The bundle ID for your app. This ID must match the one you use in Xcode. The bundle ID cannot be changed after you upload your first build.
- `name` (string): The name of your app as it will appear in the App Store. The maximum length is 30 characters.
- `primaryLocale` (string): The primary locale for your app. If localized app information isn’t available in an App Store territory, the information from your primary language is used instead.
- `sku` (string): A unique ID for your app that is not visible on the App Store.
- `contentRightsDeclaration` (string)
- `isOrEverWasMadeForKids` (boolean)
- `subscriptionStatusUrl` (uri)
- `subscriptionStatusUrlForSandbox` (uri)
- `subscriptionStatusUrlVersion` (SubscriptionStatusUrlVersion)
- `subscriptionStatusUrlVersionForSandbox` (SubscriptionStatusUrlVersion)
- `accessibilityUrl` (uri)
- `streamlinedPurchasingEnabled` (boolean): The default value is `true`.

## See Also

- [Apps](apps.md)
  Manage your apps in App Store Connect.
- [object App.Relationships](app/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app/attributes-data.dictionary)*