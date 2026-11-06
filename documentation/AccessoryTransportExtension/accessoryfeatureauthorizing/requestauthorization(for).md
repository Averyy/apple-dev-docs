# requestAuthorization(for:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Type Method  
**Required**: Yes

Requests authorization of this feature for an accessory. An authorization that has already been decided is returned unchanged.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
static func requestAuthorization(for accessory: ASAccessory) async throws -> Self.AuthorizationStatus
```

## Default Implementations

### AccessoryFeatureAuthorizing Implementations
- [static func requestAuthorization(for: ASAccessory) async throws -> Self.AuthorizationStatus](./requestauthorization%28for%29-7595m.md)
  Requests authorization of this feature for an accessory. An authorization that has already been decided is returned unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeatureauthorizing/requestauthorization(for:))*