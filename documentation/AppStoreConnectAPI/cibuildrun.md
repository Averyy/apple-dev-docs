# CiBuildRun

**Framework**: App Store Connect API  
**Kind**: dictionary

A single execution of an Xcode Cloud workflow, capturing the trigger, commit, status, and artifacts produced.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiBuildRun
```

## Topics

### Objects
- [object CiBuildRun.Attributes](cibuildrun/attributes-data.dictionary.md)
  The attributes that describe a Build Runs resource.
- [object CiBuildRun.Relationships](cibuildrun/relationships-data.dictionary.md)
  The relationships of the Build Runs resource you included in the request and those on which you can operate.

## Properties

- `attributes` (CiBuildRun.Attributes): The attributes that describe the Build Runs resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies a Build Runs resource.
- `links` (ResourceLinks): The navigational links that include the self-link.
- `relationships` (CiBuildRun.Relationships): The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [object CiBuildRunCreateRequest](cibuildruncreaterequest.md)
  The request body you use to start a new Xcode Cloud build.
- [object CiBuildRunResponse](cibuildrunresponse.md)
  The response body for endpoints that start or read a single Xcode Cloud build run.
- [object CiBuildActionsResponse](cibuildactionsresponse.md)
  The response body for endpoints that list actions for an Xcode Cloud build run.
- [object CiBuildRunActionsLinkagesResponse](cibuildrunactionslinkagesresponse.md)
- [object CiBuildRunBuildsLinkagesResponse](cibuildrunbuildslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibuildrun)*