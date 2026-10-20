# BuildBundle.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationships of the Build Bundles resource you included in the request and those on which you can operate.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```
object BuildBundle.Relationships
```

## Topics

### Objects
- [object BuildBundle.Relationships.AppClipDomainCacheStatus](./relationships-data.dictionary/appclipdomaincachestatus-data.dictionary.md)
  The data and links that describe the relationship between the Build Bundles and the App Clip Domain Cache Statuses resources.
- [object BuildBundle.Relationships.AppClipDomainDebugStatus](./relationships-data.dictionary/appclipdomaindebugstatus-data.dictionary.md)
  The data and links that describe the relationship between the Build Bundles and the App Clip Domain Debug Statuses resources.
- [object BuildBundle.Relationships.BetaAppClipInvocations](./relationships-data.dictionary/betaappclipinvocations-data.dictionary.md)
  The data, links, and paging information that describe the relationship between the Build Bundles and the Beta App Clip Invocations resources.
- [object BuildBundle.Relationships.BuildBundleFileSizes](./relationships-data.dictionary/buildbundlefilesizes-data.dictionary.md)
  The data, links, and paging information that describe the relationship between the Build Bundles and the Build Bundle File Sizes resources.

## Properties

- `appClipDomainCacheStatus` (BuildBundle.Relationships.AppClipDomainCacheStatus): The related App Clip Domain Cache Statuses resource.
- `appClipDomainDebugStatus` (BuildBundle.Relationships.AppClipDomainDebugStatus): The related App Clip Domain Debug Statuses resource.
- `betaAppClipInvocations` (BuildBundle.Relationships.BetaAppClipInvocations): The related Beta App Clip Invocations resource.
- `buildBundleFileSizes` (BuildBundle.Relationships.BuildBundleFileSizes): The related Build Bundle File Sizes resource.

## See Also

### Objects
- [object BuildBundle.Attributes](./attributes-data.dictionary.md)
  The attributes that describe a Build Bundles resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/buildbundle/relationships-data.dictionary)*