# RoutingAppCoverageUpdateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to update a Routing App Coverage.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object RoutingAppCoverageUpdateRequest
```

## Topics

### Objects
- [object RoutingAppCoverageUpdateRequest.Data](routingappcoverageupdaterequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` (RoutingAppCoverageUpdateRequest.Data) *(required)*

## See Also

- [object RoutingAppCoverage](routingappcoverage.md)
  A GeoJSON file defining the geographic coverage area of a turn-by-turn navigation app, required for App Store submission.
- [object RoutingAppCoverageCreateRequest](routingappcoveragecreaterequest.md)
  The request body you use to create a Routing App Coverage.
- [object RoutingAppCoverageResponse](routingappcoverageresponse.md)
  The response body for endpoints that read or modify the routing app coverage file for an app version.
- [object AppMediaStateError](appmediastateerror.md)
  An error code and description.
- [object AppMediaAssetState](appmediaassetstate.md)
  The state of an app or media upload, including any errors and warnings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/routingappcoverageupdaterequest)*