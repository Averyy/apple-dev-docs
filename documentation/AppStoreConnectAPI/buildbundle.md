# BuildBundle

**Framework**: App Store Connect API  
**Kind**: dictionary

A specific binary bundle within a build, such as an app extension, App Clip, or nested app target.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```swift
object BuildBundle
```

## Topics

### Objects
- [object BuildBundle.Attributes](buildbundle/attributes-data.dictionary.md)
  The attributes that describe a Build Bundles resource.
- [object BuildBundle.Relationships](buildbundle/relationships-data.dictionary.md)
  The relationships of the Build Bundles resource you included in the request and those on which you can operate.

## Properties

- `attributes` (BuildBundle.Attributes): The attributes that describe the Build Bundles resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies a Build Bundles resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `relationships` (BuildBundle.Relationships): The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

## See Also

- [type BuildBundleType](buildbundletype.md)
  A string that represents the possible components of a build bundle.
- [object AppClipDomainStatus](appclipdomainstatus.md)
  The validation status of the associated domains configured for an App Clip, indicating whether each domain is reachable and correctly set up.
- [object BuildBundleFileSize](buildbundlefilesize.md)
  The estimated and actual download and install sizes for a build bundle, broken down by device type.
- [object AppClipDomainStatusResponse](appclipdomainstatusresponse.md)
  A response containing the validation status of associated domains configured for an App Clip.
- [object BetaAppClipInvocationsResponse](betaappclipinvocationsresponse.md)
  A response containing a list of TestFlight App Clip invocations for a beta build.
- [object BuildBundleFileSizesResponse](buildbundlefilesizesresponse.md)
  A response containing a list of download and install size estimates for a build’s bundles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/buildbundle)*