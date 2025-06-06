# Create an alternative distribution package

**Framework**: App Store Connect API  
**Kind**: httpRequest

Create an alternative distribution package for an app store version.

**Availability**:
- App Store Connect API 3.3+

## Mentions

- [Creating alternative distribution packages](creating-alternative-distribution-packages.md)
- [Configuring alternative marketplaces and alternative marketplace apps](configuring-alternative-marketplaces-and-alternative-marketplace-apps.md)
- [Configuring apps for web distribution](configuring-apps-for-web-distribution.md)

#### Discussion

> 💡 **Tip**:  This endpoint requires the `appStoreVersion` in the payload. Obtain the `appStoreVersion` resource ID from the [`List All App Store Versions for an App`](get-v1-apps-_id_-appstoreversions.md) response.

 This endpoint requires the `appStoreVersion` in the payload. Obtain the `appStoreVersion` resource ID from the [`List All App Store Versions for an App`](get-v1-apps-_id_-appstoreversions.md) response.

##### Example Request and Response

## See Also

- [Creating alternative distribution packages](creating-alternative-distribution-packages.md)
  Create distribution packages for your apps that you distribute on alternative marketplaces or on the web.
- [Read alternative distribution package information](get-v1-alternativedistributionpackages-_id_.md)
  Get information about a specific alternative distribution package.
- [Read an App Store version’s alternative distribution package](get-v1-appstoreversions-_id_-alternativedistributionpackage.md)
  Read the alternative distribution package for a specific App Store version.
- [Read version information for an alternative distribution package](get-v1-alternativedistributionpackages-_id_-versions.md)
  Get version detail information about a specific alternative distribution package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-alternativedistributionpackages)*