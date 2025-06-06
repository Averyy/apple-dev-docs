# init(title:image:alternateImage:handler:)

**Framework**: AppKit  
**Kind**: init

Creates a custom sharing service object.

**Availability**:
- macOS 10.8+

## Declaration

```swift
init(title: String, image: NSImage, alternateImage: NSImage?, handler block: @escaping () -> Void)
```

#### Return Value

An instance of the custom sharing object.

#### Discussion

Custom sharing services can be added to the [`NSSharingServicePicker`](nssharingservicepicker.md) with the [`sharingServicePicker(_:sharingServicesForItems:proposedSharingServices:)`](nssharingservicepickerdelegate/sharingservicepicker(_:sharingservicesforitems:proposedsharingservices:).md) delegate method.

When implementing this method, consider subclassing `NSSharingService` so the [`canPerform(withItems:)`](nssharingservice/canperform(withitems:).md) and [`sharingServices(forItems:)`](nssharingservice/sharingservices(foritems:).md) can provide accurate results.

## Parameters

- `title`: The custom sharing service name.
- `image`: The image that represents the sharing service
- `alternateImage`: The alternate image that represents the sharing service
- `block`: The block that actually interacts with the service.

## See Also

- [init?(named: NSSharingService.Name)](nssharingservice/init(named:).md)
  Returns a sharing service instance representing the specified service name.
- [NSSharingService.Name](nssharingservice/name.md)
  Constants that describe the sharing services that macOS supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/init(title:image:alternateimage:handler:))*