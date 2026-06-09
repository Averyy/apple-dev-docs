# CiBuildRunResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that start or read a single Xcode Cloud build run.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiBuildRunResponse
```

## Properties

- `data` (CiBuildRun) *(required)*: The resource data.
- `included` ([*]): The requested relationship data.
- `links` (DocumentLinks) *(required)*: The navigational links that include the self-link.

## See Also

- [object CiBuildRun](cibuildrun.md)
  A single execution of an Xcode Cloud workflow, capturing the trigger, commit, status, and artifacts produced.
- [object CiBuildRunCreateRequest](cibuildruncreaterequest.md)
  The request body you use to start a new Xcode Cloud build.
- [object CiBuildActionsResponse](cibuildactionsresponse.md)
  The response body for endpoints that list actions for an Xcode Cloud build run.
- [object CiBuildRunActionsLinkagesResponse](cibuildrunactionslinkagesresponse.md)
- [object CiBuildRunBuildsLinkagesResponse](cibuildrunbuildslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibuildrunresponse)*