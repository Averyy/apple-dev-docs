# Read Version Information for an Alternative Distribution Package

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get version detail information about a specific alternative distribution package.

**Availability**:
- App Store Connect API 3.3+

## Mentions

- [Creating alternative distribution packages](creating-alternative-distribution-packages.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages/e651dbc7-a7a7-4e84-a1ae-2afcd92ec6cb/versions
```

**Response**:

```json
{
  "data": [
    {
      "type": "alternativeDistributionPackageVersions",
      "id": "d1663e24-4360-4f7f-a661-8e616e3b3c3b",
      "attributes": {
        "url": "https://iosapps.itunes.apple.com/itunes-assets/SWDistributionArtifacts123/v4/0f/8a/35/0f8a3516-32b0-2f72-86be-733c19d4feea/alternative-distribution-package.zip?accessKey=1711771761_1717860025327843395_oB%2B2%2Byn1erOvfVXfBIpIIPCgXnTiWMKVVgUYXQQ47LvEaartEJzuzMGd0YTc%2Bj8I0hv%2BAbs9mxSDNwPAUaZo2Y87710jMkxjdSeU7RmVU%2FDxFd14QumlGQiNwMBtuFntiagJpz2oZ1m7JoKTpkKkkIfL2wdlLYGvo8rElWc7F0uz%2B8NjVBbniKXxiLCkCFfUavdvw%2FPi6IY4MxVP8lg0tfWJP9haaemTO4Db%2BevBzH0%3D",
        "urlExpirationDate": "2024-03-29T21:09:21-07:00",
        "version": "1",
        "state": "COMPLETED"
      },
      "relationships": {
        "variants": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackageVersions/d1663e24-4360-4f7f-a661-8e616e3b3c3b/relationships/variants",
            "related": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackageVersions/d1663e24-4360-4f7f-a661-8e616e3b3c3b/variants"
          }
        },
        "deltas": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackageVersions/d1663e24-4360-4f7f-a661-8e616e3b3c3b/relationships/deltas",
            "related": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackageVersions/d1663e24-4360-4f7f-a661-8e616e3b3c3b/deltas"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackageVersions/d1663e24-4360-4f7f-a661-8e616e3b3c3b"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages/e651dbc7-a7a7-4e84-a1ae-2afcd92ec6cb/versions"
  },
  "meta": {
    "paging": {
      "total": 1,
      "limit": 50
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackages/{id}/versions`

## Parameters

- `fields[alternativeDistributionPackageDeltas]` ([string]): Additional fields to include for each Alternative Distribution Package Deltas resource returned by the response.
- `fields[alternativeDistributionPackageVariants]` ([string]): Additional fields to include for each Alternative Distribution Package Variants resource returned by the response.
- `fields[alternativeDistributionPackageVersions]` ([string]): Additional fields to include for each Alternative Distribution Package Versions resource returned by the response.
- `fields[alternativeDistributionPackages]` ([string]): Additional fields to include for each Alternative Distribution Packages resource returned by the response.
- `filter[state]` ([string]): Filter the returned versions by state.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of alternative distribution package version resources to return.
- `limit[deltas]` (integer): The maximum number of related delta resources to return.
- `limit[variants]` (integer): The maximum number of related variant resources to return.

## See Also

- [Creating alternative distribution packages](creating-alternative-distribution-packages.md)
  Create distribution packages for your apps that you distribute on alternative marketplaces or on the web.
- [Read Alternative Distribution Package Information](get-v1-alternativedistributionpackages-_id_.md)
  Get information about a specific alternative distribution package.
- [Create an Alternative Distribution Package](post-v1-alternativedistributionpackages.md)
  Create an alternative distribution package for an App Store version.
- [Read an app store version’s alternative distribution package](get-v1-appstoreversions-_id_-alternativedistributionpackage.md)
  Read the alternative distribution package for a specific App Store version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-alternativedistributionpackages-_id_-versions)*