# Creating an alternative app marketplace

**Framework**: MarketplaceKit

Enable the distribution of other third-party apps from within your marketplace app.

#### Overview

An  is an app from which someone can install other third-party apps. To create a marketplace, fill out a webform that outlines the qualifications. If approved, Apple enables a code-signing entitlement on your account to distribute your marketplace app on the web. Apple also provides you with a framework that facilitates the secure installation of apps that your marketplace distributes.

The architecture of an alternative marketplace includes an app, a webpage from which people download your app, and a web server that stores app data it regularly receives from App Store Connect. When people download an app through your alternative app marketplace, your web server communicates with the device’s operating system directly by providing authentication services, app licenses, and app data to facilitate a secure app installation experience.

![A diagram that depicts development requirements for an alternative app marketplace, which consists of a client marketplace app, an app webpage, and an app web server.](https://docs-assets.developer.apple.com/published/8e1b1493239f806f33d7346f00dad26c/creating-an-alternative-app-marketplace-3%402x.png)

> ❗ **Important**: To develop an alternative app marketplace, request approval to use the marketplace entitlement ([`com.apple.developer.marketplace.app-installation`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.marketplace.app-installation)). The request process varies by geographic region. For more information and to request the entitlement, see [`Participating in alternative distribution for specific regions`](participating-in-alternative-distribution-for-specific-regions.md).

#### Design a Marketplace App

For an alternative app marketplace:

- Build a new app; only new bundle IDs qualify for marketplace provisioning.
- Add a code-signing configuration that the system requires to launch your app on devices. Marketplace apps require the [`com.apple.developer.marketplace.app-installation`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.marketplace.app-installation) entitlement, which is a . To provision managed entitlements, see [`Provisioning with managed capabilities`](https://developer.apple.comhttps://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/).
- Build with Xcode 15.3 or later, to accommodate [`MarketplaceKit`](MarketplaceKit.md) framework availability. MarketplaceKit lets people install apps from an alternative marketplace on supported devices.
- Help provide an age-rating appropriate browsing experience by checking the maximum allowed age rating for the device. Honor any exceptions that a parent or guardian makes for specific apps. See [`Providing age-rating appropriate content`](providing-age-rating-appropriate-content.md).
- Use APIs that vary from App Store apps. Specifically, use [`AdAttributionKit`](https://developer.apple.com/documentation/AdAttributionKit) for ads, and [`Background Assets`](https://developer.apple.com/documentation/BackgroundAssets) to download large files. Use a custom e-commerce solution. API that rely on Apple’s App Store, such as [`In-App Purchase`](https://developer.apple.com/documentation/StoreKit/in-app-purchase) and [`On Demand Resources`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/), don’t support alternative app marketplaces.

#### Add the Required Target Property

If your app offers the purchase of digital goods or services, add the [`MKSellsDigitalGoods`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information-property-list/mksellsdigitalgoods) property to your app’s target configuration in Xcode with a value of `YES`. Also, report each offered purchase to Apple using the [`TransactionReporting`](transactionreporting.md) API. For more information, see [`Reporting transactions for the Core Technology Commission`](reporting-transactions-for-core-technology-commission.md).

If your app doesn’t sell digital goods or services, you still need to add the [`MKSellsDigitalGoods`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information-property-list/mksellsdigitalgoods) property to your app’s target configuration with a value of `NO`.

#### Set Up Your Marketplace App for Alternative Distribution

To set up a marketplace, provide your web domain and a distribution key to App Store Connect, which facilitates the secure distribution of your app over the web.

The domain ensures that your marketplace app installs only from your website, and the :

- Regularly verifies the agreement, or relationship, you make with other developers that distribute their app on your marketplace.
- Signs a token that the system uses to verify each installation request of your app, or the apps that your marketplace distributes.

For more information, see [`Distributing your app from your website`](distributing-your-app-from-your-website.md).

#### Facilitate the Life Cycle of Your Apps

When a developer prepares to distribute their app on your marketplace, provide them a . They upload the token in App Store Connect, which enables them to choose your marketplace as a distributor. The process of generating and exchanging the token occurs between just your app marketplace and the inquring app developer. For more information, see [`Creating keys and establishing alternative marketplace connections`](https://developer.apple.com/documentation/AppStoreConnectAPI/creating-keys-and-establishing-alternative-marketplace-connections).

To handle other regular requests, implement a web server that:

- Manages available apps by communicating with App Store Connect. When an app that your maketplace distributes completes Notarization, App Store Connect sends the app to your server. App Store Connect also notifies your server when a developer removes an app from sale or when Apple issues an app take-down request. To receive notifications and perform the actions they require, see [`Processing alternative app marketplace notifications`](processing-alternative-marketplace-notifications.md).
- Provides apps and app licenses to a person’s device. When a person attempts to download an app from your marketplace, the system requests a license from your server, followed by the app itself. The system calls various endpoints that you publish on your server to process license requests and app requests. For more information, see [`Installing apps from an alternative marketplace`](installing-apps-from-an-alternative-marketplace.md).

![A diagram that represents the relationships described in the preceding list. When a developer requests distribution by an alternative marketplace, they send a request to that marketplace, the marketplace provides a key to the developer, the developer uploads a unique key to App Store Connect, then App Store Connect sends the app to the alternative marketplace for distribution. When a person requests an app installation from the alternative marketplace, the marketplace authenticates the request and determines whether to provide a license to the operating system, the operating system then downloads and installs the app from the alternative marketplace.](https://docs-assets.developer.apple.com/published/1122da563715c7341ee4d63683f933cc/creating-an-alternative-app-marketplace-5%402x.png)

Although you store apps on — and serve apps from — your web server, people install the apps only from within your alternative app marketplace app, not your website.

> 💡 **Tip**: People can find an app on your alternative app marketplace using Spotlight search if you maintain a list of available apps and upload it to a location known to Apple. For more information, see [`Marketplace Search Configurations`](https://developer.apple.com/documentation/AppStoreConnectAPI/marketplace-search-configurations).

#### Test the App During Development

App marketplace development can occur anywhere in the world, as Xcode allows running a development-signed or Ad-Hoc signed app marketplace on Simulator and all supported physical devices. Through the development build, apps that the marketplace distributes can also install and run.

However, workflows that involve submission to App Store Connect, such as beta testing your app through internal TestFlight and web distribution of your marketplace app, need to occur on a device in the supported region, signed in with an Apple Account configured with a matching supported country or region.

You can test the installation of the apps that your marketplace distributes on a physical device when:

- A relationship exists with the app in App Store Connect. See [`Manage distribution on an alternative app marketplace`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/distributing-apps-in-the-european-union/manage-distribution-on-an-alternative-app-marketplace).
- The developer manually sends you an alternative distribution package for the app that they retrieve from App Store Connect or your webhook receives a notification from App Store Connect. See [`Processing alternative app marketplace notifications`](processing-alternative-marketplace-notifications.md).
- Your marketplace server ingests the app’s alternative distribution package; see [`Ingesting an alternative distribution package`](ingesting-an-alternative-distribution-package.md).

To test distribution over the web, ensure:

- Your marketplace app completes Notarization in App Store Connect; see [`Create a marketplace app`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/distributing-apps-in-the-european-union/create-an-marketplace-app).
- Your webpage contains a properly formatted download link to your app’s alternative distribution package; see [`Design a webpage suitable for app download`](https://developer.apple.comhttps://docs.devpubs.apple.com/releases/rainbowe-rc/documentation/appdistribution/creating-an-alternative-app-marketplace#Design-a-webpage-suitable-for-app-download).

> **Note**: To test system-wide search, upload your app catalog. Apple ingests the upload and enables its contents to show up in Lookup, Safari, and Spotlight search on a device within 24 hours. For more information, see [`Building a searchable catalog for your marketplace app for inclusion in Spotlight`](https://developer.apple.com/documentation/AppStoreConnectAPI/building-a-searchable-catalog-for-your-marketplace-app-for-inclusion-in-spotlight).

## See Also

- [Distributing your app from your website](distributing-your-app-from-your-website.md)
  Configure your app and website to enable people to install your app on their devices from your website.
- [Distributing your app on an alternative app marketplace](distributing-your-app-on-an-alternative-marketplace.md)
  Design your app for alternative distribution from an alternative app marketplace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/creating-an-alternative-app-marketplace)*