# sharingService(_:didCompleteForItems:error:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the cloud-sharing service completes.

**Availability**:
- macOS 10.8+

## Declaration

```swift
optional func sharingService(_ sharingService: NSSharingService, didCompleteForItems items: [Any], error: (any Error)?)
```

```objc
- (void) sharingService:(NSSharingService *) sharingService didCompleteForItems:(NSArray *) items error:(NSError *) error;
```

#### Discussion

The cloud-sharing service invokes this method when the user finishes sharing or dismisses the service’s view controller. If you implement this method, the service calls it instead of the [`sharingService(_:didFailToShareItems:error:)`](../nssharingservicedelegate/sharingservice%28_,didfailtoshareitems,error%29.md) and [`sharingService(_:didShareItems:)`](../nssharingservicedelegate/sharingservice%28_,didshareitems%29.md) methods.

## Parameters

- `sharingService`: The cloud-sharing service that invokes this delegate method.
- `items`: The items the service is sharing.
- `error`: If the service can’t share the items, an error that provides information about the failure; otherwise, [`nil`](../../ObjectiveC/nil-227m0.md).

## See Also

### Managing the Cloud-Sharing Service
- [func sharingService(NSSharingService, didSave: CKShare)](./sharingservice%28_,didsave%29.md)
  Tells the delegate when the cloud-sharing service saves the CloudKit share.
- [func sharingService(NSSharingService, didStopSharing: CKShare)](./sharingservice%28_,didstopsharing%29.md)
  Tells the delegate when the user stops sharing the CloudKit share.
- [func options(for: NSSharingService, share: NSItemProvider) -> NSSharingService.CloudKitOptions](./options%28for,share%29.md)
  Asks the delegate for the participant options for the cloud-sharing service.
- [NSSharingService.CloudKitOptions](../nssharingservice/cloudkitoptions.md)
  Constants that describe how a participant can configure a CloudKit share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscloudsharingservicedelegate/sharingservice(_:didcompleteforitems:error:))*