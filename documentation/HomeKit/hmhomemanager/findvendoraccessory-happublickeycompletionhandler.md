# findVendorAccessory(hapPublicKey:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- tvOS 26.1+
- visionOS 26.1+
- watchOS 26.1+

## Declaration

```swift
func findVendorAccessory(hapPublicKey: Data) async throws -> HMAccessory?
```

#### Discussion

Finds a vendor HAP accessory based on its Long Term Public Key.

If no matching accessory exists, or if the current process does not have vendor-level access to the matching accessory, the result will be nil.

An error will be returned if this method is used before available homes have been retrieved by the HMHomeManager, i.e. before the homeManagerDidUpdateHomes: delegate method has been invoked.

## Parameters

- `hapPublicKey`: The HAP Long Term Public Key of the accessory.   This has a length of 32 bytes. Refer to the   HomeKit Accessory Protocol Specification for details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/findvendoraccessory(happublickey:completionhandler:))*