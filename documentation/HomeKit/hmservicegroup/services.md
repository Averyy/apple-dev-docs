# services

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

Array of the services in the service group.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var services: [HMService] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<HMService *> * services;
```

## See Also

### Managing Service Groups
- [var name: String](./name.md)
  The name of the service group.
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  The unique identifier for the service group.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](./updatename%28_,completionhandler%29.md)
  Updates the name of the service group.
- [func addService(HMService, completionHandler: ((any Error)?) -> Void)](./addservice%28_,completionhandler%29.md)
  Adds a new service to the service group.
- [func removeService(HMService, completionHandler: ((any Error)?) -> Void)](./removeservice%28_,completionhandler%29.md)
  Removes a service from the service group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmservicegroup/services)*