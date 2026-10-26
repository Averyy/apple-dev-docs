# BAErrorDomain

**Framework**: Background Assets  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
let BAErrorDomain: String
```

```c
extern NSString * const BAErrorDomain;
```

## See Also

### Errors
- [enum ManagedBackgroundAssetsError](./managedbackgroundassetserror.md)
  An error for a managed asset pack.
- [enum BAErrorCode](./baerrorcode.md)
- [AssetPackManager.LocalAvailabilityError](./assetpackmanager/localavailabilityerror.md)
  An error that provides information about local asset pack availability, distinguishing between successes and failures.
- [BAAssetPackIdentifierErrorKey](./baassetpackidentifiererrorkey.md)
  The `-[NSError userInfo]` key for an asset pack’s identifier.
- [BAManagedErrorDomain](./bamanagederrordomain.md)
  The error domain for managed asset packs.
- [BAManagedErrorCode](./bamanagederrorcode.md)
  An error code for a managed asset pack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baerrordomain)*