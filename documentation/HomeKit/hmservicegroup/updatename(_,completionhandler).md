# updateName(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Updates the name of the service group.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func updateName(_ name: String, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func updateName(_ name: String) async throws
```

```objc
- (void) updateName:(NSString *) name completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `name`: The new name; must not be `nil`.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Managing Service Groups
- [var name: String](./name.md)
  The name of the service group.
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  The unique identifier for the service group.
- [var services: [HMService]](./services.md)
  Array of the services in the service group.
- [func addService(HMService, completionHandler: ((any Error)?) -> Void)](./addservice%28_,completionhandler%29.md)
  Adds a new service to the service group.
- [func removeService(HMService, completionHandler: ((any Error)?) -> Void)](./removeservice%28_,completionhandler%29.md)
  Removes a service from the service group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmservicegroup/updatename(_:completionhandler:))*