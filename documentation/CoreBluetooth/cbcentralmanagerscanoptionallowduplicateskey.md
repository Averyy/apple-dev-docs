# CBCentralManagerScanOptionAllowDuplicatesKey

**Framework**: Core Bluetooth  
**Kind**: var  
**Role**: Global Variable

A Boolean value that specifies whether the scan should run without duplicate filtering.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
let CBCentralManagerScanOptionAllowDuplicatesKey: String
```

```c
extern NSString * const CBCentralManagerScanOptionAllowDuplicatesKey;
```

#### Discussion

The value for this key is an [`NSNumber`](../Foundation/nsnumber.md) object. If [`true`](../Swift/true.md), the central disables filtering and generates a discovery event each time it receives an advertising packet from the peripheral. If [`false`](../Swift/false.md) (the default), the central coalesces multiple discoveries of the same peripheral into a single discovery event.

> ❗ **Important**:  Disabling this filtering can have an adverse effect on battery life; use it only if necessary.

## See Also

### Constants
- [let CBCentralManagerScanOptionSolicitedServiceUUIDsKey: String](./cbcentralmanagerscanoptionsolicitedserviceuuidskey.md)
  An array of service UUIDs that you want to scan for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerscanoptionallowduplicateskey)*