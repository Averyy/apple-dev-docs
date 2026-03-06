# CiBuildAction

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents a Build Actions resource.

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
  A response that contains a list of Artifacts resources.
- [object CiBuildActionResponse](cibuildactionresponse.md)
  A response that contains a single Build Actions resource.
- [object CiIssuesResponse](ciissuesresponse.md)
  A response that contains a list of Issues resources.
- [object CiTestResultsResponse](citestresultsresponse.md)
  A response that contains a list of Test Results resources.
- [object CiBuildActionArtifactsLinkagesResponse](cibuildactionartifactslinkagesresponse.md)
- [object CiBuildActionBuildRunLinkageResponse](cibuildactionbuildrunlinkageresponse.md)
- [object CiBuildActionIssuesLinkagesResponse](cibuildactionissueslinkagesresponse.md)
- [object CiBuildActionTestResultsLinkagesResponse](cibuildactiontestresultslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibuildaction)*