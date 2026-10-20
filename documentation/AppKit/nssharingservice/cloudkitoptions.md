# NSSharingService.CloudKitOptions

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that describe how a participant can configure a CloudKit share.

**Availability**:
- macOS 10.12+

## Declaration

```swift
struct CloudKitOptions
```

```c
enum NSCloudKitSharingServiceOptions : NSUInteger;
```

## Topics

### Creating CloudKit Options
- [init(rawValue: UInt)](./cloudkitoptions/init%28rawvalue%29.md)
  Creates a set of CloudKit options using the specified raw value.
### CloudKit Options
- [static var allowPrivate: NSSharingService.CloudKitOptions](./cloudkitoptions/allowprivate.md)
  An option that allows the participant to privately distribute the share to other iCloud users.
- [static var allowPublic: NSSharingService.CloudKitOptions](./cloudkitoptions/allowpublic.md)
  An option that allows the participant to publicly distribute the share to other iCloud users.
- [static var allowReadOnly: NSSharingService.CloudKitOptions](./cloudkitoptions/allowreadonly.md)
  An option that allows the participant to grant other participants read-only permissions.
- [static var allowReadWrite: NSSharingService.CloudKitOptions](./cloudkitoptions/allowreadwrite.md)
  An option that allows the participant to grant other participants read-write permissions.
- [static var standard: NSSharingService.CloudKitOptions](./cloudkitoptions/standard.md)
  An option that allows the participant to configure the share with a standard set of options.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Managing the Cloud-Sharing Service
- [func sharingService(NSSharingService, didCompleteForItems: [Any], error: (any Error)?)](../nscloudsharingservicedelegate/sharingservice%28_,didcompleteforitems,error%29.md)
  Tells the delegate when the cloud-sharing service completes.
- [func sharingService(NSSharingService, didSave: CKShare)](../nscloudsharingservicedelegate/sharingservice%28_,didsave%29.md)
  Tells the delegate when the cloud-sharing service saves the CloudKit share.
- [func sharingService(NSSharingService, didStopSharing: CKShare)](../nscloudsharingservicedelegate/sharingservice%28_,didstopsharing%29.md)
  Tells the delegate when the user stops sharing the CloudKit share.
- [func options(for: NSSharingService, share: NSItemProvider) -> NSSharingService.CloudKitOptions](../nscloudsharingservicedelegate/options%28for,share%29.md)
  Asks the delegate for the participant options for the cloud-sharing service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/cloudkitoptions)*