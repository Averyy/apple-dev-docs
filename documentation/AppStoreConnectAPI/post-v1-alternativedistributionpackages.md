# Create an Alternative Distribution Package

**Framework**: App Store Connect API  
**Kind**: httpRequest

Create an alternative distribution package for an App Store version.

**Availability**:
- App Store Connect API 3.3+

## Mentions

- [Creating alternative distribution packages](creating-alternative-distribution-packages.md)
- [Configuring alternative marketplaces and alternative marketplace apps](configuring-alternative-marketplaces-and-alternative-marketplace-apps.md)
- [Configuring apps for web distribution](configuring-apps-for-web-distribution.md)

#### Discussion

> 💡 **Tip**:  This endpoint requires the `appStoreVersion` in the payload. Obtain the `appStoreVersion` resource ID from the [`List All App Store Versions for an App`](get-v1-apps-_id_-appstoreversions.md) response.

##### Example Request and Response

**Request**:

```None
POST https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages
{
  "data": {
    "type": "alternativeDistributionPackages",
    "relationships": {
      "appStoreVersion": {
        "data": {
          "type": "appStoreVersions",
          "id": "3fb74833-4bf4-4c34-9cfd-f9dc4978ea45"
        }
      }
    }
  }
}
```

**Response**:

```json
{
  "data": {
    "type": "alternativeDistributionPackages",
    "id": "f3190601-974c-45ee-aa24-35db2090c260",
    "relationships": {
      "versions": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages/f3190601-974c-45ee-aa24-35db2090c260/relationships/versions",
          "related": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages/f3190601-974c-45ee-aa24-35db2090c260/versions"
        }
      }
    },
    "links": {
      "self": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages/f3190601-974c-45ee-aa24-35db2090c260"
    }
  },
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages"
  }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages`

## See Also

- [Creating alternative distribution packages](creating-alternative-distribution-packages.md)
  Create distribution packages for your apps that you distribute on alternative marketplaces or on the web.
- [Read Alternative Distribution Package Information](get-v1-alternativedistributionpackages-_id_.md)
  Get information about a specific alternative distribution package.
- [Read an App Store Version’s Alternative Distribution Package](get-v1-appstoreversions-_id_-alternativedistributionpackage.md)
  Read the alternative distribution package for a specific App Store version.
- [Read Version Information for an Alternative Distribution Package](get-v1-alternativedistributionpackages-_id_-versions.md)
  Get version detail information about a specific alternative distribution package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-alternativedistributionpackages)*