# CiIssuesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list issues from an Xcode Cloud build action.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiIssuesResponse
```

## Properties

- `data` ([CiIssue]) *(required)*: The resource data.
- `links` (PagedDocumentLinks) *(required)*: The navigational links that include the self-link.
- `meta` (PagingInformation): The paging information.

## See Also

- [object CiBuildAction](cibuildaction.md)
  The execution result of a specific action step within an Xcode Cloud build run, including its status and issues.
- [object CiArtifactsResponse](ciartifactsresponse.md)
  The response body for endpoints that list artifacts produced by an Xcode Cloud build action.
- [object CiBuildActionResponse](cibuildactionresponse.md)
  The response body for endpoints that read a single Xcode Cloud build action.
- [object CiTestResultsResponse](citestresultsresponse.md)
  The response body for endpoints that list test results from an Xcode Cloud build action.
- [object CiBuildActionArtifactsLinkagesResponse](cibuildactionartifactslinkagesresponse.md)
- [object CiBuildActionBuildRunLinkageResponse](cibuildactionbuildrunlinkageresponse.md)
- [object CiBuildActionIssuesLinkagesResponse](cibuildactionissueslinkagesresponse.md)
- [object CiBuildActionTestResultsLinkagesResponse](cibuildactiontestresultslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciissuesresponse)*