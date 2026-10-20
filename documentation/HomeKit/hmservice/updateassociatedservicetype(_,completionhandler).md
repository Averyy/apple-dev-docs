# updateAssociatedServiceType(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Associates the service type of the plugged-in device with a switch or an outlet service.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func updateAssociatedServiceType(_ serviceType: String?, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func updateAssociatedServiceType(_ serviceType: String?) async throws
```

```objc
- (void) updateAssociatedServiceType:(NSString *) serviceType completionHandler:(void (^)(NSError *error)) completion;
```

#### Discussion

This method is only valid for services of type [`HMServiceTypeOutlet`](../hmservicetypeoutlet.md) or [`HMServiceTypeSwitch`](../hmservicetypeswitch.md). See [`associatedServiceType`](./associatedservicetype.md) for details of associated service types.

## Parameters

- `serviceType`: The service type of the device that is hooked up to the switch or outlet.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Associating a secondary service
- [var associatedServiceType: String?](./associatedservicetype.md)
  The type of the service associated with an outlet or a switch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmservice/updateassociatedservicetype(_:completionhandler:))*