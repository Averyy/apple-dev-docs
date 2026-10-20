# isAdvertising

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign, readonly) BOOL isAdvertising;
```

#### Discussion

This value is [`true`](../../Swift/true.md) if the peripheral is advertising data as a result of successfully calling the [`startAdvertising(_:)`](./startadvertising%28_%29.md) method. The value is [`false`](../../Swift/false.md) if the peripheral is no longer advertising its data.

## See Also

### Managing Advertising
- [func startAdvertising([String : Any]?)](./startadvertising%28_%29.md)
  Advertises peripheral manager data.
- [Advertising Data](../advertising-data.md)
- [func stopAdvertising()](./stopadvertising%28%29.md)
  Stops advertising peripheral manager data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/isadvertising)*