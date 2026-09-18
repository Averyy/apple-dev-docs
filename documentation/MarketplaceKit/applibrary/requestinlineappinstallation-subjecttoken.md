# requestInlineAppInstallation(_:subjectToken:)

**Framework**: MarketplaceKit  
**Kind**: method

Requests the installation of a web-distributed app that you also distribute.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)

## Declaration

```swift
nonisolated
final func requestInlineAppInstallation(_ request: AppLibrary.InstallationRequest, subjectToken: String?) async throws
```

## Mentions

- [Distributing your app from your website](distributing-your-app-from-your-website.md)

#### Discussion

The system verifies that the app to install meets the following requirements:

- From the same developer account as the app that calls the method.
- Approved for web distribution. For information about the approval process, see [`Participating in alternative distribution for specific regions`](participating-in-alternative-distribution-for-specific-regions.md).

If the app fails to meet these criteria, the system throws [`MarketplaceKitError`](marketplacekiterror.md).

If the app meets the criteria, the system presents a sheet that prompts the person to approve the installation. When the person gives their approval, the system proceeds with the installation using the [`AppLibrary.InstallationRequest`](applibrary/installationrequest.md) you provide and an optional authentication token. If the installation request fails (for example, if your web server doesn’t provide the app) or the person declines the prompt, the method throws [`MarketplaceKitError`](marketplacekiterror.md).

> ❗ **Important**: The `requestInlineAppInstallation(_:subjectToken:)` method is for use in the European Union. Only call this method to install an app owned and controlled by you.

## Parameters

- `request`: An installation request that describes the alternative distribution package URL, account, and install verification token for the app to install.
- `subjectToken`: An optional authentication token equivalent to the [`MarketplaceKitURIScheme`](marketplacekiturischeme.md) `token` parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/requestinlineappinstallation(_:subjecttoken:))*