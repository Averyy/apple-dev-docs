# App License Delivery SDK

**Framework**: Applicensedeliverysdk  
**Kind**: module

Secure the installation of alternative distribution apps on iOS or iPadOS devices by vending licenses from your web server.

## Mentions

- [Licensing alternative distribution apps](licensing-alternative-distribution-apps.md)
- [Configuring your app licensing environment](configuring-the-app-licensing-environment.md)

#### Overview

This Swift SDK enables  (DRM) for alternative distribution apps. Use this SDK to generate licenses for alternative app marketplaces you build with [`MarketplaceKit`](https://developer.apple.com/documentation/MarketplaceKit) or other apps that you distribute from your website. Alternative app marketplaces use this SDK to generate a license for each app that developers distribute on the marketplace. By licensing each download individually, you provide a secure installation experience similar to the App Store.

Use this SDK’s framework to implement a license server on your website back end that’s capable of running compiled Swift code. Then, publish endpoints for your license server in a standard location that the device’s operating system expects. On an as-needed basis, the system retrieves licenses from your endpoints when a person downloads:

- An alternative app marketplace from your website
- An app that developers distribute on your alternative app marketplace
- An app that you develop and distribute on your website

![A flow diagram that consists of two boxes stacked. The title of the upper box reads App web server and the title of the lower box reads The device’s OS. The flow begins with a stage at left in the lower box that reads Install request. A line extends to its right to a stage that reads Checks licensing endpoint. The diagram flow continues with an arrow upward into the upper-box to a stage that reads Provides licensing endpoint. Flow returns to the prior stage in the lower box and then continues to the right to a stage that reads Requests app license. Flow continues with an arrow upward to a stage in the upper box that reads Swift licenseing endpoint, which contains another box within it that reads Generates app license. A callout extends from the inner stage that reads App License Delivery SDK. Flow returns to the prior stage in the lower box and then continues to the right to a stage that reads Downloads app.](https://docs-assets.developer.apple.com/published/c876327122638bd2bbab73f72fab6637/app-license-delivery-hero%402x.png)

You can download this SDK from [`Downloads`](https://developer.apple.comhttps://developer.apple.com/download/all/) if your developer account qualifies to distribute apps from your website. For more information, see  [`Distributing your app from your website`](https://developer.apple.com/documentation/appdistribution/distributing-your-app-from-your-website).

> **Note**:  Apple silicon Macs, Intel Macs, macOS 13.5+, select Linux versions on x86_64, and Xcode 15+ (including the macOS 14 SDK).

## Topics

### Essentials
- [Configuring your app licensing environment](configuring-the-app-licensing-environment.md)
  Create your account-level signing assets and build the SDK for your target platform.
### App licensing
- [Licensing alternative distribution apps](licensing-alternative-distribution-apps.md)
  Build a license server that supports the installation of your apps and the apps available in your marketplace.
- [Renewing and revoking app licenses](renewing-and-revoking-app-licenses.md)
  Determine whether an app for which you issue a license launches.
- [struct ALDAppKey](aldappkey.md)
  A structure that identifies an app and a key that’s required to decrypt the app’s license request.
- [struct ALDLicenseAttribute](aldlicenseattribute.md)
  A structure that defines the requested license type for the session.
- [class ALDProvider](aldprovider.md)
  An object that creates a session with the alternative app marketplace’s signing assets.
- [class ALDSession](aldsession.md)
  A structure that contains the details of a license request and methods to generate license responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppLicenseDeliverySDK)*