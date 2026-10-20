# session(for:delegate:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```swift
class func session(for pass: PKSecureElementPass, delegate: any PKVehicleConnectionDelegate, completion: @escaping @Sendable (PKVehicleConnectionSession?, (any Error)?) -> Void)
```

```swift
class func session(for pass: PKSecureElementPass, delegate: any PKVehicleConnectionDelegate) async throws -> PKVehicleConnectionSession
```

```objc
+ (void) sessionForPass:(PKSecureElementPass *) pass delegate:(id<PKVehicleConnectionDelegate>) delegate completion:(void (^)(PKVehicleConnectionSession *session, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkvehicleconnectionsession/session(for:delegate:completion:))*