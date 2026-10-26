# forbidLocalReferenceToLocal

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A local asset shouldn’t follow references to local media data stored outside its container file.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
static var forbidLocalReferenceToLocal: AVAssetReferenceRestrictions { get }
```

```c
AVAssetReferenceRestrictionForbidLocalReferenceToLocal
```

## See Also

### Reference restrictions
- [static var forbidAll: AVAssetReferenceRestrictions](./forbidall.md)
  The asset can only reference media stored within its container file.
- [static var forbidRemoteReferenceToLocal: AVAssetReferenceRestrictions](./forbidremotereferencetolocal.md)
  A remote asset shouldn’t follow references to local media.
- [static var forbidLocalReferenceToRemote: AVAssetReferenceRestrictions](./forbidlocalreferencetoremote.md)
  A local asset shouldn’t follow references to remote media.
- [static var forbidCrossSiteReference: AVAssetReferenceRestrictions](./forbidcrosssitereference.md)
  A remote asset shouldn’t follow references to remote media data stored at a different host.
- [static var defaultPolicy: AVAssetReferenceRestrictions](./defaultpolicy.md)
  The asset should use the default reference restrictions policy.
- [AVAssetReferenceRestrictionForbidNone](./avassetreferencerestrictionforbidnone.md)
  The asset should follow all media references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/forbidlocalreferencetolocal)*