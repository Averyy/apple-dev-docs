# Read information for an alternative distribution package version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get detail information about a specific alternative distribution package version.

**Availability**:
- App Store Connect API 3.3+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackageVersions/d1663e24-4360-4f7f-a661-8e616e3b3c3b
```

**Response**:

```json
{
  "data": {
    "type": "alternativeDistributionPackageVersions",
    "id": "d1663e24-4360-4f7f-a661-8e616e3b3c3b",
    "attributes": {
      "url": "https://iosapps.itunes.apple.com/itunes-assets/SWDistributionArtifacts123/v4/0f/8a/35/0f8a3516-32b0-2f72-86be-733c19d4feea/alternative-distribution-package.zip?accessKey=1711772539_4058138271381390069_MNqOb5cg54HQ8yX%2B%2B2Vdqr2zloVZc%2FhvKpOKC2aMcu2ktV%2BhmRoZquZJg%2BHbxrjbnRRSoqNuLQ07Y59co1q4YT2k8ikLRfUL8ZOjB6SZ4s4W3hfIquIZ6WQNoGHQ4YUwb1xVqAkNzgjgVVjp6Z41Cvuw0dyWtAQr9eJ1Q2tRd%2F5soBjsEiWWmkGI%2BZx2ByMkj5qlk9HXY%2BIkoU2XC9kQO6RyTR1YHv1JdHrw%2FNRj%2FvY%3D",
      "urlExpirationDate": "2024-03-29T21:22:19-07:00",
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
  },
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackageVersions/d1663e24-4360-4f7f-a661-8e616e3b3c3b"
  }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/alternativeDistributionPackageVersions/{id}`

## Parameters

- `fields[alternativeDistributionPackageDeltas]` ([string])
- `fields[alternativeDistributionPackageVariants]` ([string])
- `fields[alternativeDistributionPackageVersions]` ([string])
- `include` ([string])
- `limit[deltas]` (integer)
- `limit[variants]` (integer)

## See Also

- [Read version information for an alternative distribution package](get-v1-alternativedistributionpackages-_id_-versions.md)
  Get version detail information about a specific alternative distribution package.
- [List deltas information](get-v1-alternativedistributionpackageversions-_id_-deltas.md)
  List deltas for a specific alternative distribution package version.
- [List variants information](get-v1-alternativedistributionpackageversions-_id_-variants.md)
  List variants for specific alternative distribution package version.
- [List delta Ids](get-v1-alternativedistributionpackageversions-_id_-relationships-deltas.md)
  List all delta Ids for a specific alternative distribution package version.
- [List variant Ids information](get-v1-alternativedistributionpackageversions-_id_-relationships-variants.md)
  List variant Ids for specific alternative distribution package version.
- [Read version Ids for an alternative distribution package](get-v1-alternativedistributionpackages-_id_-relationships-versions.md)
  Get version IDs about a specific alternative distribution package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-alternativedistributionpackageversions-_id_)*