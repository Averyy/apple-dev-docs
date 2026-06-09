# AlternativeDistributionPackageVersionsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list versions of an alternative distribution package.

**Availability**:
- App Store Connect API 3.3+

## Declaration

```swift
object AlternativeDistributionPackageVersionsResponse
```

#### Discussion

This object is the response that contains a list of alternative distribution package versions. For more information, see [`Read Version Information for an Alternative Distribution Package`](get-v1-alternativedistributionpackages-_id_-versions.md). The schema of the response body is below.

```javascript
{
  "data": [
    {
      "type": "alternativeDistributionPackageVersions",
      "id": "string",
      "attributes": {
        "url": "string",
        "urlExpirationDate": "2025-02-23T06:55:44.288Z",
        "version": "string",
        "state": "COMPLETED"
      },
      "relationships": {
        "variants": {
          "links": {
            "self": "string",
            "related": "string"
          },
          "meta": {
            "paging": {
              "total": 0,
              "limit": 0
            }
          },
          "data": [
            {
              "type": "alternativeDistributionPackageVariants",
              "id": "string"
            }
          ]
        },
        "deltas": {
          "links": {
            "self": "string",
            "related": "string"
          },
          "meta": {
            "paging": {
              "total": 0,
              "limit": 0
            }
          },
          "data": [
            {
              "type": "alternativeDistributionPackageDeltas",
              "id": "string"
            }
          ]
        },
        "alternativeDistributionPackage": {
          "links": {
            "self": "string",
            "related": "string"
          },
          "data": {
            "type": "alternativeDistributionPackages",
            "id": "string"
          }
        }
      },
      "links": {
        "self": "string"
      }
    },
    "included": [
      {
        "type": "alternativeDistributionPackageVariants",
        "id": "string",
        "attributes": {
          "url": "string",
          "urlExpirationDate": "2025-02-23T06:55:44.288Z",
          "alternativeDistributionKeyBlob": "string"
        },
        "links": {
          "self": "string"
        }
      },
      {
        "type": "alternativeDistributionPackageDeltas",
        "id": "string",
        "attributes": {
          "url": "string",
          "urlExpirationDate": "2025-02-23T06:55:44.288Z",
          "alternativeDistributionKeyBlob": "string"
        },
        "links": {
          "self": "string"
        }
      },
      {
        "type": "alternativeDistributionPackages",
        "id": "string",
          "relationships": {
          "versions": {
            "links": {
              "self": "string",
              "related": "string"
            },
            "meta": {
              "paging": {
                "total": 0,
                "limit": 0
              }
            },
            "data": [
              {
                "type": "alternativeDistributionPackageVersions",
                "id": "string"
              }
            ]
          }
        },
        "links": {
          "self": "string"
        }
      }
    ],
    "links": {
      "self": "string",
      "first": "string",
      "next": "string"
    },
    "meta": {
      "paging": {
        "total": 0,
        "limit": 0
      }
    }
  }
}
```

## Properties

- `data` ([AlternativeDistributionPackageVersion]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AlternativeDistributionPackage](alternativedistributionpackage.md)
  The distributable package for an app on an alternative marketplace or web distribution, containing versioned variants and delta updates.
- [object AlternativeDistributionPackageCreateRequest](alternativedistributionpackagecreaterequest.md)
  The request body you use to create an alternative distribution package.
- [object AlternativeDistributionPackageResponse](alternativedistributionpackageresponse.md)
  The response body for endpoints that read a single alternative distribution package.
- [object AlternativeDistributionPackageVersion](alternativedistributionpackageversion.md)
  A versioned snapshot of an alternative distribution package, containing its variants and delta updates.
- [object AlternativeDistributionPackageVersionResponse](alternativedistributionpackageversionresponse.md)
  The response body for endpoints that read a single alternative distribution package version.
- [object AlternativeDistributionPackageDelta](alternativedistributionpackagedelta.md)
  An incremental update package for an alternative distribution app, containing only the changes between two versions to reduce download size.
- [object AlternativeDistributionPackageDeltaResponse](alternativedistributionpackagedeltaresponse.md)
  A response containing a single delta update for an alternative distribution package.
- [object AlternativeDistributionPackageDeltasResponse](alternativedistributionpackagedeltasresponse.md)
  A response containing a list of delta updates available for an alternative distribution package.
- [object AlternativeDistributionPackageVariant](alternativedistributionpackagevariant.md)
  A device-specific file package within an alternative distribution app, targeting a particular device family.
- [object AlternativeDistributionPackageVariantResponse](alternativedistributionpackagevariantresponse.md)
  A response containing a single variant of an alternative distribution package.
- [object AlternativeDistributionPackageVariantsResponse](alternativedistributionpackagevariantsresponse.md)
  A response containing a list of device-specific variants within an alternative distribution package.
- [object AlternativeDistributionPackageVersionDeltasLinkagesResponse](alternativedistributionpackageversiondeltaslinkagesresponse.md)
- [object AlternativeDistributionPackageVersionVariantsLinkagesResponse](alternativedistributionpackageversionvariantslinkagesresponse.md)
- [object AlternativeDistributionPackageVersionsLinkagesResponse](alternativedistributionpackageversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/alternativedistributionpackageversionsresponse)*