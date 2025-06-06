# removeService(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Removes a service from the service group.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func removeService(_ service: HMService) async throws
```

## Parameters

- `service`: The service to remove.
- `completion`: The block executed after the request is processed.

## See Also

- [var name: String](hmservicegroup/name.md)
  The name of the service group.
- [var uniqueIdentifier: UUID](hmservicegroup/uniqueidentifier.md)
  The unique identifier for the service group.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](hmservicegroup/updatename(_:completionhandler:).md)
  Updates the name of the service group.
- [var services: [HMService]](hmservicegroup/services.md)
  Array of the services in the service group.
- [func addService(HMService, completionHandler: ((any Error)?) -> Void)](hmservicegroup/addservice(_:completionhandler:).md)
  Adds a new service to the service group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmservicegroup/removeservice(_:completionhandler:))*