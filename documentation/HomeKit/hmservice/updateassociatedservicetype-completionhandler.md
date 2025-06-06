# updateAssociatedServiceType(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Associates the service type of the plugged-in device with a switch or an outlet service.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func updateAssociatedServiceType(_ serviceType: String?) async throws
```

#### Discussion

This method is only valid for services of type [`HMServiceTypeOutlet`](hmservicetypeoutlet.md) or [`HMServiceTypeSwitch`](hmservicetypeswitch.md). See [`associatedServiceType`](hmservice/associatedservicetype.md) for details of associated service types.

## Parameters

- `serviceType`: The service type of the device that is hooked up to the switch or outlet.
- `completion`: The block executed after the request is processed.

## See Also

- [var associatedServiceType: String?](hmservice/associatedservicetype.md)
  The type of the service associated with an outlet or a switch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmservice/updateassociatedservicetype(_:completionhandler:))*