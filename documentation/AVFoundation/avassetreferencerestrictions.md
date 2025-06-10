# AVAssetReferenceRestrictions

**Framework**: AVFoundation  
**Kind**: struct

Restrictions to use when resolving references to external media data.

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
struct AVAssetReferenceRestrictions
```

## Topics

### Reference Restrictions
- [static var forbidAll: AVAssetReferenceRestrictions](avassetreferencerestrictions/forbidall.md)
  The asset can only reference media stored within its container file.
- [static var forbidRemoteReferenceToLocal: AVAssetReferenceRestrictions](avassetreferencerestrictions/forbidremotereferencetolocal.md)
  A remote asset shouldn’t follow references to local media.
- [static var forbidLocalReferenceToRemote: AVAssetReferenceRestrictions](avassetreferencerestrictions/forbidlocalreferencetoremote.md)
  A local asset shouldn’t follow references to remote media.
- [static var forbidCrossSiteReference: AVAssetReferenceRestrictions](avassetreferencerestrictions/forbidcrosssitereference.md)
  A remote asset shouldn’t follow references to remote media data stored at a different host.
- [static var forbidLocalReferenceToLocal: AVAssetReferenceRestrictions](avassetreferencerestrictions/forbidlocalreferencetolocal.md)
  A local asset shouldn’t follow references to local media data stored outside its container file.
- [static var defaultPolicy: AVAssetReferenceRestrictions](avassetreferencerestrictions/defaultpolicy.md)
  The asset should use the default reference restrictions policy.
### Initializers
- [init(rawValue: UInt)](avassetreferencerestrictions/init(rawvalue:).md)
  Creates reference restrictions with an integer value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var referenceRestrictions: AVAssetReferenceRestrictions](avasset/referencerestrictions.md)
  The restrictions that an asset places on how it resolves references to external media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreferencerestrictions)*