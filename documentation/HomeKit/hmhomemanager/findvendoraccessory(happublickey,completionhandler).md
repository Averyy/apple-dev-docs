# findVendorAccessory(hapPublicKey:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Finds your vendor HAP accessory using its long-term public key.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- tvOS 26.1+
- visionOS 26.0+
- watchOS 26.1+

## Declaration

```swift
func findVendorAccessory(hapPublicKey: Data, completionHandler completion: @escaping @Sendable (HMAccessory?, (any Error)?) -> Void)
```

```swift
func findVendorAccessory(hapPublicKey: Data) async throws -> HMAccessory?
```

```objc
- (void) findVendorAccessoryWithHAPPublicKey:(NSData *) hapPublicKey completionHandler:(void (^)(HMAccessory *, NSError *)) completion;
```

#### Overview

Use `findVendorAccessory(hapPublicKey:completionHandler:)` to find out if your accessory is currently paired with HomeKit.

## Parameters

- `hapPublicKey`: The HAP long-term public key of the accessory with a length of 32 bytes.
- `completion`: The block that HomeKit runs after the request completes. If HomeKit isn’t paired to a matching accessory, or if the current process doesn’t have access to the matching accessory, the completion block returns `nil` instead of an accessory. The completion block provides an error if you call `findVendorAccessory(hapPublicKey:completionHandler:)` before [`HMHomeManager`](../hmhomemanager.md) can retrieve a home, such as before HomeKit calls the [`homeManagerDidUpdateHomes(_:)`](../hmhomemanagerdelegate/homemanagerdidupdatehomes%28_%29.md) callback method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/findvendoraccessory(happublickey:completionhandler:))*