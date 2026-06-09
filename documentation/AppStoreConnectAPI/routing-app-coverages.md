# Routing App Coverages

**Framework**: App Store Connect API

Manage geographic coverage files for apps that use location to provide routing information.

#### Overview

Use `routingAppCoverages` to upload, replace, or delete a geographic coverage file for App Review. If your app uses location to provide routing information, you must supply a geographic coverage file before submitting your app to App Review. For more information see [`Upload a geographic coverage file for a routing app (iOS, watchOS)`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/upload-a-geographic-coverage-file).

For information about creating a geographic coverage file, see “Specifying the Geographic Coverage File Contents” in [`Location and Maps Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/ProvidingDirections/ProvidingDirections.html).

## Topics

### Reading and Creating Routing App Coverages
- [Read the routing app coverage information of an app store version](get-v1-appstoreversions-_id_-routingappcoverage.md)
  Get the routing app coverage file that is associated with a specific App Store version
- [Read routing app coverage information](get-v1-routingappcoverages-_id_.md)
  Get information about the routing app coverage file and its upload and processing status.
- [Create a routing app coverage](post-v1-routingappcoverages.md)
  Attach a routing app coverage file to an App Store version.
### Modifying and Deleting Routing App Coverages
- [Modify a routing app coverage](patch-v1-routingappcoverages-_id_.md)
  Commit a routing app coverage file after uploading it.
- [Delete a routing app coverage](delete-v1-routingappcoverages-_id_.md)
  Delete the routing app coverage file that is associated with a version.
### Objects
- [object RoutingAppCoverage](routingappcoverage.md)
  A GeoJSON file defining the geographic coverage area of a turn-by-turn navigation app, required for App Store submission.
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

## See Also

- [App Infos](app-infos.md)
  Manage or read the app metadata that applies across all versions of your app.
- [App Info Localizations](app-info-localizations.md)
  Manage the app metadata that is localized and appears on the App Store.
- [App Store Versions](app-store-versions.md)
  Manage versions of your app that are available in App Store.
- [App Store Version Localizations](app-store-version-localizations.md)
  Create and maintain version-specific App Store metadata that’s localized.
- [App tags](app-tags.md)
  Read or modify Apple created app tags.
- [Accessibility declarations](accessibility-declarations.md)
  Manage accessibility metadata for your apps per device family.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/routing-app-coverages)*