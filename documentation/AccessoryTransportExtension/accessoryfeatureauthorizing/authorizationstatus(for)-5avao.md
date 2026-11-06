# authorizationStatus(for:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Type Method

The feature’s current authorization status for an accessory.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
static func authorizationStatus(for accessory: ASAccessory) async throws -> Self.AuthorizationStatus
```

Available when `Self` conforms to `AccessoryFeature`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeatureauthorizing/authorizationstatus(for:)-5avao)*