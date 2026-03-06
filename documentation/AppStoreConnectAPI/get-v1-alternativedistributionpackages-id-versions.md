# Read version information for an alternative distribution package

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

- `fields[alternativeDistributionPackageDeltas]` ([string])
- `fields[alternativeDistributionPackageVariants]` ([string])
- `fields[alternativeDistributionPackageVersions]` ([string])
- `fields[alternativeDistributionPackages]` ([string])
- `filter[state]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[deltas]` (integer)
- `limit[variants]` (integer)

## See Also

- [Creating alternative distribution packages](creating-alternative-distribution-packages.md)
  Create distribution packages for your apps that you distribute on alternative marketplaces or on the web.
- [Read alternative distribution package information](get-v1-alternativedistributionpackages-_id_.md)
  Get information about a specific alternative distribution package.
- [Create an alternative distribution package](post-v1-alternativedistributionpackages.md)
  Create an alternative distribution package for an app store version.
- [Read an App Store version’s alternative distribution package](get-v1-appstoreversions-_id_-alternativedistributionpackage.md)
  Read the alternative distribution package for a specific App Store version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-alternativedistributionpackages-_id_-versions)*