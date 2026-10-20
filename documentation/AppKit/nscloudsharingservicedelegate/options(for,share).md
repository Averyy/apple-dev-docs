# options(for:share:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the participant options for the cloud-sharing service.

**Availability**:
- macOS 10.12+

## Declaration

```swift
optional func options(for cloudKitSharingService: NSSharingService, share provider: NSItemProvider) -> NSSharingService.CloudKitOptions
```

```objc
- (NSCloudKitSharingServiceOptions) optionsForSharingService:(NSSharingService *) cloudKitSharingService shareProvider:(NSItemProvider *) provider;
```

#### Discussion

Use this method to specify whether the share is public or private. The options you return also determine any permissions that the share’s participants have. If you don’t implement this method, the cloud-sharing service uses the [`standard`](../nssharingservice/cloudkitoptions/standard.md) options.

## Parameters

- `cloudKitSharingService`: The cloud-sharing service that invokes this delegate method.
- `provider`: The item provider that supplies the share to the service.

## See Also

### Managing the Cloud-Sharing Service
- [func sharingService(NSSharingService, didCompleteForItems: [Any], error: (any Error)?)](./sharingservice%28_,didcompleteforitems,error%29.md)
  Tells the delegate when the cloud-sharing service completes.
- [func sharingService(NSSharingService, didSave: CKShare)](./sharingservice%28_,didsave%29.md)
  Tells the delegate when the cloud-sharing service saves the CloudKit share.
- [func sharingService(NSSharingService, didStopSharing: CKShare)](./sharingservice%28_,didstopsharing%29.md)
  Tells the delegate when the user stops sharing the CloudKit share.
- [NSSharingService.CloudKitOptions](../nssharingservice/cloudkitoptions.md)
  Constants that describe how a participant can configure a CloudKit share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscloudsharingservicedelegate/options(for:share:))*