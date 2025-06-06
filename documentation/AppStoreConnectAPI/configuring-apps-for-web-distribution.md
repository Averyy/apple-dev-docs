# Configuring apps for web distribution

**Framework**: App Store Connect API

Set up your app for direct installation.

#### Overview

You can distribute approved apps in eligible regions from your company website. Use this API to setup your app for web distribution.

##### Establish an Alternative Distribution Key

Begin making your app eligible for download from your website by selecting your existing app record, or making a new one in App Store Connect. Next, create a public and private key pair to associate with your app for web distribution. For more information, see [`Creating and configuring keys for web distribution`](creating-and-configuring-keys-for-web-distribution.md).

##### Add an Alternative Distribution Domain

[`Add an alternative distribution domain`](post-v1-alternativedistributiondomains.md) to represent your app’s base web domain, from which all traffic must flow. This domain is where people can download and install your web distribution app. This domain is enabled for all apps on your account.

##### Obtain and Distribute Your Alternative Distribution Package

Next, you need to obtain the alternative distribution package ID.

If your web distribution app is already approved, you need to generate an alternative distribution package by using the [`Create an alternative distribution package`](post-v1-alternativedistributionpackages.md) endpoint.

If your web distribution app is not in one of the following states (all of which are after approval by App Review): `Pending Developer Release, Pending Apple Release,` or `Ready for Distribution,` the alternative distribution package is automatically created after approval.

After the alternative distribution package is created, you can ingest and process the provided files. For more information, see [`Ingesting an alternative distribution package`](https://developer.apple.com/documentation/appdistribution/ingesting-an-alternative-distribution-package).

Finally, you set up your web server to allow users to get your app. For more information, see [`Distributing your app from your website`](https://developer.apple.com/documentation/appdistribution/distributing-your-app-from-your-website).

## See Also

- [Configuring alternative marketplaces and alternative marketplace apps](configuring-alternative-marketplaces-and-alternative-marketplace-apps.md)
  Establish a connection between a marketplace and a marketplace app and configure marketplace settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/configuring-apps-for-web-distribution)*