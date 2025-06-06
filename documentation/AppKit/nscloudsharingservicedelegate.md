# NSCloudSharingServiceDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of methods for responding to the life cycle events of the cloud-sharing service.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSCloudSharingServiceDelegate : NSSharingServiceDelegate
```

#### Overview

CloudKit allows a user to share a hierarchy of records with other iCloud users. In macOS, you use [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) and [`NSSharingService`](nssharingservice.md) to facilitate sharing. Register an instance of [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) with an item provider, and then use a sharing service to present it to the user. You must initialize the service with the [`cloudSharing`](nssharingservice/name/cloudsharing.md) service name. If the share is new, the user can configure the share and invite other iCloud users to participate. Otherwise, they can use the service to manage the share’s participants and their permissions.

This protocol defines methods that the sharing service calls when it saves changes to a share, or deletes it. The service also asks its delegate to provide the preferred sharing options when creating a new share. Set the service’s [`delegate`](nssharingservice/delegate.md) property to an object that implements this protocol. Use your implementation to provide any appropriate behavior, such as deleting a share you cache locally when the service deletes it from the server.

For more information about CloudKit sharing, see [`Shared Records`](https://developer.apple.com/documentation/CloudKit/shared-records).

## Topics

### Managing the Cloud-Sharing Service
- [func sharingService(NSSharingService, didCompleteForItems: [Any], error: (any Error)?)](nscloudsharingservicedelegate/sharingservice(_:didcompleteforitems:error:).md)
  Tells the delegate when the cloud-sharing service completes.
- [func sharingService(NSSharingService, didSave: CKShare)](nscloudsharingservicedelegate/sharingservice(_:didsave:).md)
  Tells the delegate when the cloud-sharing service saves the CloudKit share.
- [func sharingService(NSSharingService, didStopSharing: CKShare)](nscloudsharingservicedelegate/sharingservice(_:didstopsharing:).md)
  Tells the delegate when the user stops sharing the CloudKit share.
- [func options(for: NSSharingService, share: NSItemProvider) -> NSSharingService.CloudKitOptions](nscloudsharingservicedelegate/options(for:share:).md)
  Asks the delegate for the participant options for the cloud-sharing service.
- [NSSharingService.CloudKitOptions](nssharingservice/cloudkitoptions.md)
  Constants that describe how a participant can configure a CloudKit share.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSharingServiceDelegate](nssharingservicedelegate.md)

## See Also

- [class NSSharingService](nssharingservice.md)
  An object that facilitates the sharing of content with social media services, or with apps like Mail or Safari.
- [class NSSharingServicePicker](nssharingservicepicker.md)
  A list of sharing services that the user can choose from.
- [protocol NSPreviewRepresentableActivityItem](nspreviewrepresentableactivityitem.md)
  An interface you adopt in custom objects that you want to share using the macOS share sheet.
- [class NSSharingServicePickerToolbarItem](nssharingservicepickertoolbaritem.md)
  A toolbar item that displays the macOS share sheet.
- [protocol NSServicesMenuRequestor](nsservicesmenurequestor.md)
  A set of methods that support interaction with items users can share through a sharing service.
- [Services Functions](services-functions.md)
  Configure the contents of your app’s Services menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscloudsharingservicedelegate)*