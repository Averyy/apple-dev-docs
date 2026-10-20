# sharingService(_:didStopSharing:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the user stops sharing the CloudKit share.

**Availability**:
- macOS 10.8+

## Declaration

```swift
optional func sharingService(_ sharingService: NSSharingService, didStopSharing share: CKShare)
```

```objc
- (void) sharingService:(NSSharingService *) sharingService didStopSharing:(CKShare *) share;
```

#### Discussion

The cloud-sharing service invokes this method after it deletes the share on the server. The `share` parameter is the most recent state of the share before the service deletes it.

## Parameters

- `sharingService`: The cloud-sharing service that invokes this delegate method.
- `share`: The share the user is no longer sharing.

## See Also

### Managing the Cloud-Sharing Service
- [func sharingService(NSSharingService, didCompleteForItems: [Any], error: (any Error)?)](./sharingservice%28_,didcompleteforitems,error%29.md)
  Tells the delegate when the cloud-sharing service completes.
- [func sharingService(NSSharingService, didSave: CKShare)](./sharingservice%28_,didsave%29.md)
  Tells the delegate when the cloud-sharing service saves the CloudKit share.
- [func options(for: NSSharingService, share: NSItemProvider) -> NSSharingService.CloudKitOptions](./options%28for,share%29.md)
  Asks the delegate for the participant options for the cloud-sharing service.
- [NSSharingService.CloudKitOptions](../nssharingservice/cloudkitoptions.md)
  Constants that describe how a participant can configure a CloudKit share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscloudsharingservicedelegate/sharingservice(_:didstopsharing:))*