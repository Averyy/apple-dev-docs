# init(type:primary:)

**Framework**: Core Bluetooth  
**Kind**: init

Creates a newly initialized mutable service specified by UUID and service type.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+

## Declaration

```swift
init(type UUID: CBUUID, primary isPrimary: Bool)
```

#### Return Value

A newly initialized mutable service.

#### Discussion

For more information, see [`Core Bluetooth Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257).

## Parameters

- `UUID`: A 128-bit UUID that identifies the service.
- `isPrimary`: A Boolean value that indicates whether the type of service is primary or secondary. If the value is  , the type of service is primary. If the value is  , the type of service is secondary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmutableservice/init(type:primary:))*