# peripheral(_:didDiscoverServices:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that peripheral service discovery succeeded.

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
optional func peripheral(_ peripheral: CBPeripheral, didDiscoverServices error: (any Error)?)
```

#### Discussion

Core Bluetooth invokes this method when your app calls the [`discoverServices(_:)`](cbperipheral/discoverservices(_:).md) method. If the peripheral successfully discovers services, you can access them through the peripheral’s [`services`](cbperipheral/services.md) property. If successful, the `error` parameter is `nil`. If unsuccessful, the `error` parameter returns the cause of the failure.

For more information, see [`Core Bluetooth Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257).

## Parameters

- `peripheral`: The peripheral to which the services belong.
- `error`: The reason the call failed, or   if no error occurred.

## See Also

- [func peripheral(CBPeripheral, didDiscoverIncludedServicesFor: CBService, error: (any Error)?)](cbperipheraldelegate/peripheral(_:diddiscoverincludedservicesfor:error:).md)
  Tells the delegate that discovering included services within the indicated service completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate/peripheral(_:diddiscoverservices:))*