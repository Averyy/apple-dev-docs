# forbidCrossSiteReference

**Framework**: AVFoundation  
**Kind**: property

A remote asset shouldn’t follow references to remote media data stored at a different host.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static var forbidCrossSiteReference: AVAssetReferenceRestrictions { get }
```

## See Also

- [static var forbidAll: AVAssetReferenceRestrictions](avassetreferencerestrictions/forbidall.md)
  The asset can only reference media stored within its container file.
- [static var forbidRemoteReferenceToLocal: AVAssetReferenceRestrictions](avassetreferencerestrictions/forbidremotereferencetolocal.md)
  A remote asset shouldn’t follow references to local media.
- [static var forbidLocalReferenceToRemote: AVAssetReferenceRestrictions](avassetreferencerestrictions/forbidlocalreferencetoremote.md)
  A local asset shouldn’t follow references to remote media.
- [static var forbidLocalReferenceToLocal: AVAssetReferenceRestrictions](avassetreferencerestrictions/forbidlocalreferencetolocal.md)
  A local asset shouldn’t follow references to local media data stored outside its container file.
- [static var defaultPolicy: AVAssetReferenceRestrictions](avassetreferencerestrictions/defaultpolicy.md)
  The asset should use the default reference restrictions policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions/forbidcrosssitereference)*