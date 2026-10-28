# uuid

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

The Bluetooth-specific UUID of the attribute.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var uuid: CBUUID { get }
```

```objc
@property (nonatomic, readonly) CBUUID * UUID;
```

## Discussion

This property is a 128-bit UUID that identifies the attribute.

For more information, see [Core Bluetooth Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbattribute/uuid)*