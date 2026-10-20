# init(_:)

**Framework**: Accessory Live Activities  
**Kind**: init  
**Role**: Initializer

Creates an object you use to manage Live Activity forwarding for your accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
init(_ handlerFactory: @escaping @Sendable () -> any LiveActivityForwarding.AccessoryLiveActivitiesHandler)
```

#### Overview

The system calls the handler factory closure once for each Live Activity session and creates a new corresponding handler instance that receives updates for the life cycle of the Live Activity session.

## Parameters

- `handlerFactory`: A closure that creates one new [`LiveActivityForwarding.AccessoryLiveActivitiesHandler`](./accessoryliveactivitieshandler.md) instance for each new Live Activity session.

## See Also

### Requesting Live Activity forwarding
- [static func authorization(forAccessory: ASAccessory) async throws -> AccessoryAuthorizationResult](./authorization%28foraccessory%29.md)
  Checks whether someone permits the system to forward Live Activities to the given accessory.
- [static func presentAuthorizationSheet(forAccessory: ASAccessory) async throws -> AccessoryAuthorizationResult](./presentauthorizationsheet%28foraccessory%29.md)
  Presents the system UI that allows people to manage their permission to forward Live Activities to an accessory.
- [static let featureID: String](./featureid.md)
  A constant you use to configure your data provider extension’s capability to forward Live Activities to your accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/liveactivityforwarding/init(_:))*