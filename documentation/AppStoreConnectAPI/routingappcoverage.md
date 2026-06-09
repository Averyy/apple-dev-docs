# RoutingAppCoverage

**Framework**: App Store Connect API  
**Kind**: dictionary

A GeoJSON file defining the geographic coverage area of a turn-by-turn navigation app, required for App Store submission.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object RoutingAppCoverage
```

## Topics

### Objects
- [object RoutingAppCoverage.Attributes](routingappcoverage/attributes-data.dictionary.md)
  Attributes that describe a Routing App Coverages resource.
- [object RoutingAppCoverage.Relationships](routingappcoverage/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (RoutingAppCoverage.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (RoutingAppCoverage.Relationships)
- `type` (string) *(required)*

## See Also

- [object RoutingAppCoverageCreateRequest](routingappcoveragecreaterequest.md)
  The request body you use to create a Routing App Coverage.
- [object RoutingAppCoverageResponse](routingappcoverageresponse.md)
  The response body for endpoints that read or modify the routing app coverage file for an app version.
- [object RoutingAppCoverageUpdateRequest](routingappcoverageupdaterequest.md)
  The request body you use to update a Routing App Coverage.
- [object AppMediaStateError](appmediastateerror.md)
  An error code and description.
- [object AppMediaAssetState](appmediaassetstate.md)
  The state of an app or media upload, including any errors and warnings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/routingappcoverage)*