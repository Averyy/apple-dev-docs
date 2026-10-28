# cannotRemoveNonBridgeAccessory

**Framework**: HomeKit  
**Kind**: property  
**Role**: Type Property

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
static var cannotRemoveNonBridgeAccessory: HMError.Code { get }
```

## Discussion

You can only remove standalone or bridge accessories.

## See Also

### Detecting bridge errors
- [static var bridgedAccessoryNotReachable: HMError.Code](./bridgedaccessorynotreachable.md)
  An error indicating the bridged accessory cannot be reached.
- [static var cannotUnblockNonBridgeAccessory: HMError.Code](./cannotunblocknonbridgeaccessory.md)
  An error indicating a non-bridge accessory cannot be unblocked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/cannotremovenonbridgeaccessory)*