# AppUpdateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes whose values you’re changing as part of the update request.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```
object AppUpdateRequest.Data.Attributes
```

## Mentions

- [App Store Connect API 1.6 release notes](../../app-store-connect-api-1-6-release-notes.md)

## Properties

- `bundleId` (string)
- `contentRightsDeclaration` (string): **Allowed Values**: `DOES_NOT_USE_THIRD_PARTY_CONTENT`, `USES_THIRD_PARTY_CONTENT`
- `primaryLocale` (string)
- `subscriptionStatusUrl` (uri)
- `subscriptionStatusUrlForSandbox` (uri)
- `subscriptionStatusUrlVersion` (SubscriptionStatusUrlVersion)
- `subscriptionStatusUrlVersionForSandbox` (SubscriptionStatusUrlVersion)
- `groupPurchaseInvitationMode` (string): Who hosts the seat invitations for multiseat subscription purchases that customers make in your app on the App Store. Use APPLE_HOSTED for Apple to send invitations and manage how members accept them, or DEVELOPER_HOSTED for your app to host its own invitation and seat acceptance flow. The default is APPLE_HOSTED.

  **Allowed Values**: `APPLE_HOSTED`, `DEVELOPER_HOSTED`
- `accessibilityUrl` (uri)
- `streamlinedPurchasingEnabled` (boolean)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appupdaterequest/data-data.dictionary/attributes-data.dictionary)*