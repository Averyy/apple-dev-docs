# Participating in alternative distribution for specific regions

**Framework**: MarketplaceKit

Develop your app for alternative distribution according to the varying features that specific geographic regions support.

#### Overview

Participating in alternative distribution has different requirements depending on the geographic region, including entitlement requests, supported devices or features, and availability of specific API. Review the differences for the regions in which you expect to offer your app, and plan for them in development.

An alternative app marketplace can reference [`catalogRegion`](applibrary/catalogregion.md) and adjust the apps the marketplace offers for installation according to the country in which the device resides.

#### Develop for Alternative Distribution in Japan

In Japan, you can distribute your app on an alternative app marketplace—or create one—according to the following region-specific criteria.

To distribute your app from an alternative app marketplace in Japan, review and sign the latest [`Developer Program License Agreement`](https://developer.apple.comhttps://developer.apple.com/programs/apple-developer-program-license-agreement). Apps that reside on alternative marketplaces need to support iPhone.

To create an alternative app marketplace, request approval to use the marketplace entitlement by [`Getting started as an alternative app marketplace in Japan`](https://developer.apple.comhttps://developer.apple.com/support/alternative-app-marketplace-jp/). Alternative app marketplaces support iPhone and are available in Xcode 15.3, iOS 26.2 and later. For information on SDK versions and deployment targets, see [`Xcode support`](https://developer.apple.comhttps://developer.apple.com/support/xcode).

Only alternative app marketplaces install from a website. When you receive approval to develop an alternative app marketplace, it also grants your ability to distribute it over the web.

#### Develop for Alternative Distribution in the European Union

In the European Union, you can distribute your app on an alternative app marketplace, create a marketplace, or distribute an app from your website according to the following region-specific criteria.

Review and sign the [`Alternative EU Terms Addendum`](https://developer.apple.comhttps://developer.apple.com/contact/request/alternative-eu-terms-addendum/) to the [`Developer Program License Agreement`](https://developer.apple.comhttps://developer.apple.com/programs/apple-developer-program-license-agreement). Apps that reside on alternative marketplaces can support iPhone, iPad, or both.

To create an alternative app marketplace, request approval to use the marketplace entitlement by [`Getting started as an alternative app marketplace in the European Union`](https://developer.apple.comhttps://developer.apple.com/support/alternative-app-marketplace-in-the-eu/). When you receive approval to develop an alternative app marketplace, it also grants your ability to distribute it over the web. Alternative app marketplaces support iPhone and iPad, and are available in Xcode 15.3, iOS 17.4 and later, and iPadOS 18.0 and later. For information on SDK versions and deployment targets, see [`Xcode support`](https://developer.apple.comhttps://developer.apple.com/support/xcode).

In the EU, you can also distribute approved apps that aren’t marketplaces from your website. To distribute an app that’s not a marketplace from your website, see [`Getting started with Web Distribution in the EU`](https://developer.apple.comhttps://developer.apple.com/support/web-distribution-eu/).

In iOS 18.2 or iPadOS 18.2 and later, development builds of browser apps with the default browser entitlement ([`com.apple.developer.web-browser`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.web-browser)) can test the installation of app marketplaces and other apps that distribute over the web.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/participating-in-alternative-distribution-for-specific-regions)*