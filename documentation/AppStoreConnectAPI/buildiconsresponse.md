# BuildIconsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of icon images for a build.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object BuildIconsResponse
```

## Properties

- `data` ([BuildIcon]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object BuildIcon](buildicon.md)
  A PNG icon image extracted from a build, used for display in App Store Connect and TestFlight.
- [object BuildIconsWithoutIncludesResponse](buildiconswithoutincludesresponse.md)
  A response containing a list of build icons, without related resources.
- [object ImageAsset](imageasset.md)
  An image asset, including its height, width, and template URL.
- [type IconAssetType](iconassettype.md)
  String that represents the type of icon contained in the build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/buildiconsresponse)*