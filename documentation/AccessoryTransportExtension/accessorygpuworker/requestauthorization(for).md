# requestAuthorization(for:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Type Method

Enrolls the feature for an accessory.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
static func requestAuthorization(for accessory: ASAccessory) async throws -> AccessoryFeatureAuthorizationStatus
```

## Discussion

Enrollment doesn’t prompt the person, and it lasts for the life of the accessory’s pairing. If the app already enrolled the feature, the method returns the recorded status.

This method throws [`AccessoryTransportSession.Error.unavailable`](../accessorytransportsession/error/unavailable.md) when the device isn’t eligible for the feature. It also throws a generic error when the system can’t record the enrollment, for example, when the accessory hasn’t finished setup or isn’t paired with your app.

## Parameters

- `accessory`: The accessory for which to enroll the feature.

## See Also

### Checking authorization
- [static func authorizationStatus(for: ASAccessory) async throws -> AccessoryFeatureAuthorizationStatus](./authorizationstatus%28for%29.md)
  Returns the feature’s current authorization status for an accessory.
- [enum AccessoryFeatureAuthorizationStatus](../accessoryfeatureauthorizationstatus.md)
  A status that describes whether the system authorizes a feature for an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorygpuworker/requestauthorization(for:))*