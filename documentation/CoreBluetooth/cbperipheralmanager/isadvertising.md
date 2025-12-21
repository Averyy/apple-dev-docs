# isAdvertising

**Framework**: Core Bluetooth  
**Kind**: property

A Boolean value that indicates whether the peripheral is advertising data.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isAdvertising: Bool { get }
```

#### Discussion

This value is [`true`](https://developer.apple.com/documentation/Swift/true) if the peripheral is advertising data as a result of successfully calling the [`startAdvertising(_:)`](cbperipheralmanager/startadvertising(_:).md) method. The value is [`false`](https://developer.apple.com/documentation/Swift/false) if the peripheral is no longer advertising its data.

## See Also

- [func startAdvertising([String : Any]?)](cbperipheralmanager/startadvertising(_:).md)
  Advertises peripheral manager data.
- [Advertising Data](advertising-data.md)
- [func stopAdvertising()](cbperipheralmanager/stopadvertising.md)
  Stops advertising peripheral manager data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/isadvertising)*