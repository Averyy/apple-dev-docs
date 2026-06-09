# CiBuildRunCreateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to start a new Xcode Cloud build.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiBuildRunCreateRequest
```

## Topics

### Objects
- [object CiBuildRunCreateRequest.Data](cibuildruncreaterequest/data-data.dictionary.md)
  The data element of the request you use to start a new Xcode Cloud build.

## Properties

- `data` (CiBuildRunCreateRequest.Data) *(required)*: The resource data.

## See Also

- [object CiBuildRun](cibuildrun.md)
  A single execution of an Xcode Cloud workflow, capturing the trigger, commit, status, and artifacts produced.
- [object CiBuildRunResponse](cibuildrunresponse.md)
  The response body for endpoints that start or read a single Xcode Cloud build run.
- [object CiBuildActionsResponse](cibuildactionsresponse.md)
  The response body for endpoints that list actions for an Xcode Cloud build run.
- [object CiBuildRunActionsLinkagesResponse](cibuildrunactionslinkagesresponse.md)
- [object CiBuildRunBuildsLinkagesResponse](cibuildrunbuildslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibuildruncreaterequest)*