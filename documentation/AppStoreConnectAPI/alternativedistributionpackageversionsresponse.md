# AlternativeDistributionPackageVersionsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains a list of alternative distribution package version resources.

**Availability**:
- App Store Connect API 3.3+

## Declaration

```swift
object AlternativeDistributionPackageVersionsResponse
```

#### Discussion

This object is the response that contains a list of alternative distribution package versions. For more information, see [`Read version information for an alternative distribution package`](get-v1-alternativedistributionpackages-_id_-versions.md). The schema of the response body is below.

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

## See Also

- [object AlternativeDistributionPackage](alternativedistributionpackage.md)
  The data structure that represents an alternative distribution package resource.
- [object AlternativeDistributionPackageCreateRequest](alternativedistributionpackagecreaterequest.md)
  The request body you use to create an alternative distribution package.
- [object AlternativeDistributionPackageResponse](alternativedistributionpackageresponse.md)
  A response that contains a single alternative distribution package resource.
- [object AlternativeDistributionPackageVersion](alternativedistributionpackageversion.md)
  The data structure that represents an alternative distribution package version resource.
- [object AlternativeDistributionPackageVersionResponse](alternativedistributionpackageversionresponse.md)
  A response that contains a single alternative distribution package version resource.
- [object AlternativeDistributionPackageDelta](alternativedistributionpackagedelta.md)
  The data structure that represents an alternative distribution package delta resource.
- [object AlternativeDistributionPackageDeltaResponse](alternativedistributionpackagedeltaresponse.md)
  A response that contains a single alternative distribution package delta resource.
- [object AlternativeDistributionPackageDeltasResponse](alternativedistributionpackagedeltasresponse.md)
  A response that contains a list of alternative distribution package delta resources.
- [object AlternativeDistributionPackageVariant](alternativedistributionpackagevariant.md)
  The data structure that represents an alternative distribution package variant resource.
- [object AlternativeDistributionPackageVariantResponse](alternativedistributionpackagevariantresponse.md)
  A response that contains a single alternative distribution package variant resource.
- [object AlternativeDistributionPackageVariantsResponse](alternativedistributionpackagevariantsresponse.md)
  A response that contains a list of alternative distribution package variant resources.
- [object AlternativeDistributionPackageVersionDeltasLinkagesResponse](alternativedistributionpackageversiondeltaslinkagesresponse.md)
- [object AlternativeDistributionPackageVersionVariantsLinkagesResponse](alternativedistributionpackageversionvariantslinkagesresponse.md)
- [object AlternativeDistributionPackageVersionsLinkagesResponse](alternativedistributionpackageversionslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/alternativedistributionpackageversionsresponse)*