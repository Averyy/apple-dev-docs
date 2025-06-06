# name

**Framework**: HomeKit  
**Kind**: property

The name of the service group.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var name: String { get }
```

#### Discussion

Service group names must be unique within a home.

## See Also

- [HomeKit Developer Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/HomeKitDeveloperGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40015050)
- [var uniqueIdentifier: UUID](hmservicegroup/uniqueidentifier.md)
  The unique identifier for the service group.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](hmservicegroup/updatename(_:completionhandler:).md)
  Updates the name of the service group.
- [var services: [HMService]](hmservicegroup/services.md)
  Array of the services in the service group.
- [func addService(HMService, completionHandler: ((any Error)?) -> Void)](hmservicegroup/addservice(_:completionhandler:).md)
  Adds a new service to the service group.
- [func removeService(HMService, completionHandler: ((any Error)?) -> Void)](hmservicegroup/removeservice(_:completionhandler:).md)
  Removes a service from the service group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmservicegroup/name)*