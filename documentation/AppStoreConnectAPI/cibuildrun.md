# CiBuildRun

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents a Build Runs resource.

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
  A response that contains a single Build Runs resource.
- [object CiBuildActionsResponse](cibuildactionsresponse.md)
  A response that contains a list of Build Actions resources.
- [object CiBuildRunActionsLinkagesResponse](cibuildrunactionslinkagesresponse.md)
- [object CiBuildRunBuildsLinkagesResponse](cibuildrunbuildslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibuildrun)*