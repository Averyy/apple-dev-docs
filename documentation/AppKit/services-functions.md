# Services Functions

**Framework**: AppKit

Configure the contents of your app’s Services menu.

## Topics

### Registering Services
- [func NSRegisterServicesProvider(Any?, NSServiceProviderName)](nsregisterservicesprovider(_:_:).md)
  Registers a service provider.
- [func NSUnregisterServicesProvider(NSServiceProviderName)](nsunregisterservicesprovider(_:).md)
  Unregisters a service provider.
- [func NSUpdateDynamicServices()](nsupdatedynamicservices().md)
  Causes the services information for the system to be updated.
- [typealias NSServiceProviderName](nsserviceprovidername.md)
### Performing Services
- [func NSPerformService(String, NSPasteboard?) -> Bool](nsperformservice(_:_:).md)
  Programmatically invokes a Services menu service.

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
- [protocol NSCloudSharingServiceDelegate](nscloudsharingservicedelegate.md)
  A set of methods for responding to the life cycle events of the cloud-sharing service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/services-functions)*