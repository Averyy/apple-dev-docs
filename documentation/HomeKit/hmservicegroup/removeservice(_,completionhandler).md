# removeService(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Removes a service from the service group.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func removeService(_ service: HMService, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func removeService(_ service: HMService) async throws
```

```objc
- (void) removeService:(HMService *) service completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `service`: The service to remove.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Managing Service Groups
- [var name: String](./name.md)
  The name of the service group.
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  The unique identifier for the service group.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](./updatename%28_,completionhandler%29.md)
  Updates the name of the service group.
- [var services: [HMService]](./services.md)
  Array of the services in the service group.
- [func addService(HMService, completionHandler: ((any Error)?) -> Void)](./addservice%28_,completionhandler%29.md)
  Adds a new service to the service group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmservicegroup/removeservice(_:completionhandler:))*