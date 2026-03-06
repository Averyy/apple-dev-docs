# Read alternative distribution package information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific alternative distribution package.

**Availability**:
- App Store Connect API 3.3+

## Mentions

- [App Store Connect API 4.2 release notes](app-store-connect-api-4-2-release-notes.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages/c925443b-7dfb-4cc5-8b1a-0074eb7d5fe9
```

**Response**:

```json


{
  "data" : {
    "type" : "alternativeDistributionPackages",
    "id" : "c925443b-7dfb-4cc5-8b1a-0074eb7d5fe9",
    "relationships" : {
      "versions" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages/c925443b-7dfb-4cc5-8b1a-0074eb7d5fe9/relationships/versions",
          "related" : "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages/c925443b-7dfb-4cc5-8b1a-0074eb7d5fe9/versions"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages/c925443b-7dfb-4cc5-8b1a-0074eb7d5fe9"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages/c925443b-7dfb-4cc5-8b1a-0074eb7d5fe9"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages/{id}`

## Parameters

- `fields[alternativeDistributionPackageVersions]` ([string])
- `fields[alternativeDistributionPackages]` ([string])
- `include` ([string])
- `limit[versions]` (integer)

## See Also

- [Creating alternative distribution packages](creating-alternative-distribution-packages.md)
  Create distribution packages for your apps that you distribute on alternative marketplaces or on the web.
- [Create an alternative distribution package](post-v1-alternativedistributionpackages.md)
  Create an alternative distribution package for an app store version.
- [Read an App Store version’s alternative distribution package](get-v1-appstoreversions-_id_-alternativedistributionpackage.md)
  Read the alternative distribution package for a specific App Store version.
- [Read version information for an alternative distribution package](get-v1-alternativedistributionpackages-_id_-versions.md)
  Get version detail information about a specific alternative distribution package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-alternativedistributionpackages-_id_)*