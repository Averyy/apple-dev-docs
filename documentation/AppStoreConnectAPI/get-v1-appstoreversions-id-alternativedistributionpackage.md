# Read an app store version’s alternative distribution package

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read the alternative distribution package for a specific App Store version.

**Availability**:
- App Store Connect API 3.3+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appStoreVersions/f6586f8b-12db-4861-818e-b5cbe0d1736f/alternativeDistributionPackage
```

**Response**:

```json
{
  "data": {
    "type": "alternativeDistributionPackages",
    "id": "e651dbc7-a7a7-4e84-a1ae-2afcd92ec6cb",
    "relationships": {
      "versions": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages/e651dbc7-a7a7-4e84-a1ae-2afcd92ec6cb/relationships/versions",
          "related": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages/e651dbc7-a7a7-4e84-a1ae-2afcd92ec6cb/versions"
        }
      }
    },
    "links": {
      "self": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages/e651dbc7-a7a7-4e84-a1ae-2afcd92ec6cb"
    }
  },
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/f6586f8b-12db-4861-818e-b5cbe0d1736f/alternativeDistributionPackage"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersions/{id}/alternativeDistributionPackage`

## Parameters

- `fields[alternativeDistributionPackageVersions]` ([string]): Additional fields to include for each alternative distribution package version resource returned by the response.
- `fields[alternativeDistributionPackages]` ([string]): Additional fields to include for each alternative distribution package resource returned by the response.
- `include` ([string]): The relationship data to include in the response.
- `limit[versions]` (integer): The maximum number of related versions resources to return.

## See Also

- [Creating alternative distribution packages](creating-alternative-distribution-packages.md)
  Create distribution packages for your apps that you distribute on alternative marketplaces or on the web.
- [Read Alternative Distribution Package Information](get-v1-alternativedistributionpackages-_id_.md)
  Get information about a specific alternative distribution package.
- [Create an Alternative Distribution Package](post-v1-alternativedistributionpackages.md)
  Create an alternative distribution package for an App Store version.
- [Read Version Information for an Alternative Distribution Package](get-v1-alternativedistributionpackages-_id_-versions.md)
  Get version detail information about a specific alternative distribution package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversions-_id_-alternativedistributionpackage)*