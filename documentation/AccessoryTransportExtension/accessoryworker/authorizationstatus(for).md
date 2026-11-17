# authorizationStatus(for:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Type Method

Returns the feature’s current authorization status for an accessory.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
static func authorizationStatus(for accessory: ASAccessory) async throws -> AccessoryFeatureAuthorizationStatus
```

## Mentions

- [Sending data to an accessory in the background](../sending-data-to-an-accessory-in-the-background.md)

## Discussion

This method is asynchronous and can throw a generic error. It returns [`AccessoryFeatureAuthorizationStatus.unknown`](../accessoryfeatureauthorizationstatus/unknown.md) until your app enrolls the feature with [`requestAuthorization(for:)`](./requestauthorization%28for%29.md), then returns the recorded status on every call after that. Call it before you open a session to confirm the feature is enrolled.

## Parameters

- `accessory`: The accessory to check.

## See Also

### Checking authorization
- [static func requestAuthorization(for: ASAccessory) async throws -> AccessoryFeatureAuthorizationStatus](./requestauthorization%28for%29.md)
  Enrolls the feature for an accessory.
- [enum AccessoryFeatureAuthorizationStatus](../accessoryfeatureauthorizationstatus.md)
  A status that describes whether the system authorizes a feature for an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryworker/authorizationstatus(for:))*