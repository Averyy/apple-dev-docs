# BuildIconsWithoutIncludesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of build icons, without related resources.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object BuildIconsWithoutIncludesResponse
```

## Properties

- `data` ([BuildIcon]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object BuildIcon](buildicon.md)
  A PNG icon image extracted from a build, used for display in App Store Connect and TestFlight.
- [object BuildIconsResponse](buildiconsresponse.md)
  A response containing a list of icon images for a build.
- [object ImageAsset](imageasset.md)
  An image asset, including its height, width, and template URL.
- [type IconAssetType](iconassettype.md)
  String that represents the type of icon contained in the build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/buildiconswithoutincludesresponse)*