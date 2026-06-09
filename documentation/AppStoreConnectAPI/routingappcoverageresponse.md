# RoutingAppCoverageResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that read or modify the routing app coverage file for an app version.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object RoutingAppCoverageResponse
```

## Properties

- `data` (RoutingAppCoverage) *(required)*
- `links` (DocumentLinks) *(required)*
- `included` ([AppStoreVersion])

## See Also

- [object RoutingAppCoverage](routingappcoverage.md)
  A GeoJSON file defining the geographic coverage area of a turn-by-turn navigation app, required for App Store submission.
- [object RoutingAppCoverageCreateRequest](routingappcoveragecreaterequest.md)
  The request body you use to create a Routing App Coverage.
- [object RoutingAppCoverageUpdateRequest](routingappcoverageupdaterequest.md)
  The request body you use to update a Routing App Coverage.
- [object AppMediaStateError](appmediastateerror.md)
  An error code and description.
- [object AppMediaAssetState](appmediaassetstate.md)
  The state of an app or media upload, including any errors and warnings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/routingappcoverageresponse)*