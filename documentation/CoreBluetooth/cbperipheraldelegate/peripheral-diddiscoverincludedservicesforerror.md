# peripheral(_:didDiscoverIncludedServicesFor:error:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that discovering included services within the indicated service completed.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func peripheral(_ peripheral: CBPeripheral, didDiscoverIncludedServicesFor service: CBService, error: (any Error)?)
```

#### Discussion

Core Bluetooth invokes this method when your app calls the [`discoverIncludedServices(_:for:)`](cbperipheral/discoverincludedservices(_:for:).md) method. If the peripheral successfully discovers services, you can access them through the service’s [`includedServices`](cbservice/includedservices.md) property. If successful, the `error` parameter is `nil`. If unsuccessful, the `error` parameter returns the cause of the failure.

## Parameters

- `peripheral`: The peripheral providing this information.
- `service`: The   object containing the included service.
- `error`: The reason the call failed, or   if no error occurred.

## See Also

- [func peripheral(CBPeripheral, didDiscoverServices: (any Error)?)](cbperipheraldelegate/peripheral(_:diddiscoverservices:).md)
  Tells the delegate that peripheral service discovery succeeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/peripheral(_:diddiscoverincludedservicesfor:error:))*