# HMError.Code.cannotRemoveNonBridgeAccessory

**Framework**: HomeKit  
**Kind**: case

An attempt to remove a bridged accessory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case cannotRemoveNonBridgeAccessory
```

#### Discussion

You can only remove standalone or bridge accessories.

## See Also

- [HMError.Code.bridgedAccessoryNotReachable](hmerror/code/bridgedaccessorynotreachable.md)
  An error indicating the bridged accessory cannot be reached.
- [HMError.Code.cannotUnblockNonBridgeAccessory](hmerror/code/cannotunblocknonbridgeaccessory.md)
  An error indicating a non-bridge accessory cannot be unblocked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/code/cannotremovenonbridgeaccessory)*