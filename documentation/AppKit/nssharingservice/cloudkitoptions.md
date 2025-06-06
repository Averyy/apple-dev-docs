# NSSharingService.CloudKitOptions

**Framework**: AppKit  
**Kind**: struct

Constants that describe how a participant can configure a CloudKit share.

**Availability**:
- macOS 10.12+

## Declaration

```swift
struct CloudKitOptions
```

## Topics

### Creating CloudKit Options
- [init(rawValue: UInt)](nssharingservice/cloudkitoptions/init(rawvalue:).md)
  Creates a set of CloudKit options using the specified raw value.
### CloudKit Options
- [static var allowPrivate: NSSharingService.CloudKitOptions](nssharingservice/cloudkitoptions/allowprivate.md)
  An option that allows the participant to privately distribute the share to other iCloud users.
- [static var allowPublic: NSSharingService.CloudKitOptions](nssharingservice/cloudkitoptions/allowpublic.md)
  An option that allows the participant to publicly distribute the share to other iCloud users.
- [static var allowReadOnly: NSSharingService.CloudKitOptions](nssharingservice/cloudkitoptions/allowreadonly.md)
  An option that allows the participant to grant other participants read-only permissions.
- [static var allowReadWrite: NSSharingService.CloudKitOptions](nssharingservice/cloudkitoptions/allowreadwrite.md)
  An option that allows the participant to grant other participants read-write permissions.
- [static var standard: NSSharingService.CloudKitOptions](nssharingservice/cloudkitoptions/standard.md)
  An option that allows the participant to configure the share with a standard set of options.

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

- [func sharingService(NSSharingService, didCompleteForItems: [Any], error: (any Error)?)](nscloudsharingservicedelegate/sharingservice(_:didcompleteforitems:error:).md)
  Tells the delegate when the cloud-sharing service completes.
- [func sharingService(NSSharingService, didSave: CKShare)](nscloudsharingservicedelegate/sharingservice(_:didsave:).md)
  Tells the delegate when the cloud-sharing service saves the CloudKit share.
- [func sharingService(NSSharingService, didStopSharing: CKShare)](nscloudsharingservicedelegate/sharingservice(_:didstopsharing:).md)
  Tells the delegate when the user stops sharing the CloudKit share.
- [func options(for: NSSharingService, share: NSItemProvider) -> NSSharingService.CloudKitOptions](nscloudsharingservicedelegate/options(for:share:).md)
  Asks the delegate for the participant options for the cloud-sharing service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/cloudkitoptions)*