# AppStoreVersionReleaseRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

A request to manually release an App Store version that was set to manual release after review approval.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object AppStoreVersionReleaseRequest
```

## Properties

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `type` (string) *(required)*: The resource type.

## See Also

- [object AppStoreVersionReleaseRequestCreateRequest](appstoreversionreleaserequestcreaterequest.md)
  The request body you use to manually release an App Store approved version of your app.
- [object AppStoreVersionReleaseRequestResponse](appstoreversionreleaserequestresponse.md)
  A response containing a single manual release request for an App Store version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appstoreversionreleaserequest)*