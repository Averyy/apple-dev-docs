# sharingService(_:didStopSharing:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate when the user stops sharing the CloudKit share.

**Availability**:
- macOS 10.8+

## Declaration

```swift
optional func sharingService(_ sharingService: NSSharingService, didStopSharing share: CKShare)
```

#### Discussion

The cloud-sharing service invokes this method after it deletes the share on the server. The `share` parameter is the most recent state of the share before the service deletes it.

## Parameters

- `sharingService`: The cloud-sharing service that invokes this delegate method.
- `share`: The share the user is no longer sharing.

## See Also

- [func sharingService(NSSharingService, didCompleteForItems: [Any], error: (any Error)?)](nscloudsharingservicedelegate/sharingservice(_:didcompleteforitems:error:).md)
  Tells the delegate when the cloud-sharing service completes.
- [func sharingService(NSSharingService, didSave: CKShare)](nscloudsharingservicedelegate/sharingservice(_:didsave:).md)
  Tells the delegate when the cloud-sharing service saves the CloudKit share.
- [func options(for: NSSharingService, share: NSItemProvider) -> NSSharingService.CloudKitOptions](nscloudsharingservicedelegate/options(for:share:).md)
  Asks the delegate for the participant options for the cloud-sharing service.
- [NSSharingService.CloudKitOptions](nssharingservice/cloudkitoptions.md)
  Constants that describe how a participant can configure a CloudKit share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscloudsharingservicedelegate/sharingservice(_:didstopsharing:))*