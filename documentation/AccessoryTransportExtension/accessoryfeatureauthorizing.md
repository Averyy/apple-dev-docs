# AccessoryFeatureAuthorizing

**Framework**: Accessory Transport Extension  
**Kind**: protocol  
**Role**: Protocol

A feature that is authorized separately on each accessory.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
protocol AccessoryFeatureAuthorizing
```

## Topics

### Type Aliases
- [AccessoryFeatureAuthorizing.AuthorizationStatus](./accessoryfeatureauthorizing/authorizationstatus.md)
  The authorization status of this feature.
### Type Methods
- [static func authorizationStatus(for: ASAccessory) async throws -> Self.AuthorizationStatus](./accessoryfeatureauthorizing/authorizationstatus%28for%29.md)
  The feature’s current authorization status for an accessory.
- [static func requestAuthorization(for: ASAccessory) async throws -> Self.AuthorizationStatus](./accessoryfeatureauthorizing/requestauthorization%28for%29.md)
  Requests authorization of this feature for an accessory. An authorization that has already been decided is returned unchanged.

## Relationships

### Conforming Types
- [AccessoryGPUWorker](./accessorygpuworker.md)
- [AccessoryWorker](./accessoryworker.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeatureauthorizing)*