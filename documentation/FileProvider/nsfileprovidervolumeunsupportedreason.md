# NSFileProviderVolumeUnsupportedReason

**Framework**: File Provider  
**Kind**: struct  
**Role**: Structure

Constants that describe why an external volume might not be eligible for storing a domain.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct NSFileProviderVolumeUnsupportedReason
```

```c
enum NSFileProviderVolumeUnsupportedReason : NSUInteger;
```

## Topics

### Reasons
- [static var unknown: NSFileProviderVolumeUnsupportedReason](./nsfileprovidervolumeunsupportedreason/unknown.md)
- [static var nonEncrypted: NSFileProviderVolumeUnsupportedReason](./nsfileprovidervolumeunsupportedreason/nonencrypted.md)
- [static var readOnly: NSFileProviderVolumeUnsupportedReason](./nsfileprovidervolumeunsupportedreason/readonly.md)
- [static var network: NSFileProviderVolumeUnsupportedReason](./nsfileprovidervolumeunsupportedreason/network.md)
- [static var quarantined: NSFileProviderVolumeUnsupportedReason](./nsfileprovidervolumeunsupportedreason/quarantined.md)
### Initializers
- [init(rawValue: UInt)](./nsfileprovidervolumeunsupportedreason/init%28rawvalue%29.md)
### Type Properties
- [static var nonAPFS: NSFileProviderVolumeUnsupportedReason](./nsfileprovidervolumeunsupportedreason/nonapfs.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Determining eligibility
- [NSFileProviderManager.EligibilityResult.eligible](./nsfileprovidermanager/eligibilityresult/eligible.md)
- [NSFileProviderManager.EligibilityResult.ineligible(_:)](./nsfileprovidermanager/eligibilityresult/ineligible%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidervolumeunsupportedreason)*