# CiBuildAction

**Framework**: App Store Connect API  
**Kind**: dictionary

The execution result of a specific action step within an Xcode Cloud build run, including its status and issues.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiBuildAction
```

## Topics

### Objects
- [object CiBuildAction.Attributes](cibuildaction/attributes-data.dictionary.md)
  The attributes that describe a Build Actions resource.
- [object CiBuildAction.Relationships](cibuildaction/relationships-data.dictionary.md)
  The relationships of the Build Actions resource you included in the request and those on which you can operate.

## Properties

- `attributes` (CiBuildAction.Attributes): The attributes that describe the Build Actions resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies a Build Actions resource.
- `links` (ResourceLinks): The navigational links that include the self-link.
- `relationships` (CiBuildAction.Relationships): The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object CiArtifactsResponse](ciartifactsresponse.md)
  The response body for endpoints that list artifacts produced by an Xcode Cloud build action.
- [object CiBuildActionResponse](cibuildactionresponse.md)
  The response body for endpoints that read a single Xcode Cloud build action.
- [object CiIssuesResponse](ciissuesresponse.md)
  The response body for endpoints that list issues from an Xcode Cloud build action.
- [object CiTestResultsResponse](citestresultsresponse.md)
  The response body for endpoints that list test results from an Xcode Cloud build action.
- [object CiBuildActionArtifactsLinkagesResponse](cibuildactionartifactslinkagesresponse.md)
- [object CiBuildActionBuildRunLinkageResponse](cibuildactionbuildrunlinkageresponse.md)
- [object CiBuildActionIssuesLinkagesResponse](cibuildactionissueslinkagesresponse.md)
- [object CiBuildActionTestResultsLinkagesResponse](cibuildactiontestresultslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibuildaction)*