# stopMagnetometerUpdates()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Stops magnetometer updates.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
func stopMagnetometerUpdates()
```

```objc
- (void) stopMagnetometerUpdates;
```

## See Also

### Managing Magnetometer Updates
- [var magnetometerUpdateInterval: TimeInterval](./magnetometerupdateinterval.md)
  The interval, in seconds, at which the system delivers magnetometer data to the block handler.
- [func startMagnetometerUpdates(to: OperationQueue, withHandler: CMMagnetometerHandler)](./startmagnetometerupdates%28to,withhandler%29.md)
  Starts magnetometer updates on an operation queue and with a specified handler.
- [func startMagnetometerUpdates()](./startmagnetometerupdates%28%29.md)
  Starts magnetometer updates without a block handler.
- [var magnetometerData: CMMagnetometerData?](./magnetometerdata.md)
  The latest sample of magnetometer data.
- [typealias CMMagnetometerHandler](../cmmagnetometerhandler.md)
  The type of block callback for handling magnetometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopmagnetometerupdates())*