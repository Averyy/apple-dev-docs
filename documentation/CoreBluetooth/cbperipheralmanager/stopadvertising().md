# stopAdvertising()

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

Stops advertising peripheral manager data.

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
func stopAdvertising()
```

```objc
- (void) stopAdvertising;
```

## Discussion

Call this method when you no longer want to advertise peripheral manager data.

## See Also

### Managing Advertising
- [func startAdvertising([String : Any]?)](./startadvertising%28_%29.md)
  Advertises peripheral manager data.
- [Advertising Data](../advertising-data.md)
- [var isAdvertising: Bool](./isadvertising.md)
  A Boolean value that indicates whether the peripheral is advertising data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/stopadvertising())*