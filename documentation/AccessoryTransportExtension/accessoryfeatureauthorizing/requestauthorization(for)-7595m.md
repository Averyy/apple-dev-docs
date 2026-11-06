# requestAuthorization(for:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Type Method

Requests authorization of this feature for an accessory. An authorization that has already been decided is returned unchanged.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
static func requestAuthorization(for accessory: ASAccessory) async throws -> Self.AuthorizationStatus
```

Available when `Self` conforms to `AccessoryFeature`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeatureauthorizing/requestauthorization(for:)-7595m)*