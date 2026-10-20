# centralManager(_:didUpdateANCSAuthorizationFor:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the authorization status changed for a ANCS-requiring connected peripheral.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func centralManager(_ central: CBCentralManager, didUpdateANCSAuthorizationFor peripheral: CBPeripheral)
```

```objc
- (void) centralManager:(CBCentralManager *) central didUpdateANCSAuthorizationForPeripheral:(CBPeripheral *) peripheral;
```

## Parameters

- `central`: The central manager providing this information.
- `peripheral`: The [`CBPeripheral`](../cbperipheral.md) that caused the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/centralmanager(_:didupdateancsauthorizationfor:))*