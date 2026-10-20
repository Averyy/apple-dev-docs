# BuildIcon

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A PNG icon image extracted from a build, used for display in App Store Connect and TestFlight.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```
object BuildIcon
```

## Topics

### Objects
- [object BuildIcon.Attributes](./buildicon/attributes-data.dictionary.md)
  Attributes that describe a Build Icons resource.

## Properties

- `attributes` (BuildIcon.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `type` (string) *(required)*: **Allowed Values**: `buildIcons`

## See Also

### Objects and types
- [object BuildIconsResponse](./buildiconsresponse.md)
  A response containing a list of icon images for a build.
- [object BuildIconsWithoutIncludesResponse](./buildiconswithoutincludesresponse.md)
  A response containing a list of build icons, without related resources.
- [object ImageAsset](./imageasset.md)
  An image asset, including its height, width, and template URL.
- [type IconAssetType](./iconassettype.md)
  String that represents the type of icon contained in the build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/buildicon)*