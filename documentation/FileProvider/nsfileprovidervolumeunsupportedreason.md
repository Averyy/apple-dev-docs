# NSFileProviderVolumeUnsupportedReason

**Framework**: File Provider  
**Kind**: struct

Constants that describe why an external volume might not be eligible for storing a domain.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct NSFileProviderVolumeUnsupportedReason
```

## Topics

### Reasons
- [static var unknown: NSFileProviderVolumeUnsupportedReason](nsfileprovidervolumeunsupportedreason/unknown.md)
- [static var nonEncrypted: NSFileProviderVolumeUnsupportedReason](nsfileprovidervolumeunsupportedreason/nonencrypted.md)
- [static var readOnly: NSFileProviderVolumeUnsupportedReason](nsfileprovidervolumeunsupportedreason/readonly.md)
- [static var network: NSFileProviderVolumeUnsupportedReason](nsfileprovidervolumeunsupportedreason/network.md)
- [static var quarantined: NSFileProviderVolumeUnsupportedReason](nsfileprovidervolumeunsupportedreason/quarantined.md)
### Initializers
- [init(rawValue: UInt)](nsfileprovidervolumeunsupportedreason/init(rawvalue:).md)
### Type Properties
- [static var nonAPFS: NSFileProviderVolumeUnsupportedReason](nsfileprovidervolumeunsupportedreason/nonapfs.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [NSFileProviderManager.EligibilityResult.eligible](nsfileprovidermanager/eligibilityresult/eligible.md)
- [NSFileProviderManager.EligibilityResult.ineligible(_:)](nsfileprovidermanager/eligibilityresult/ineligible(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidervolumeunsupportedreason)*