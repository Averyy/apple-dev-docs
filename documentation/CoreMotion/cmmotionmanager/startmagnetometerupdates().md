# startMagnetometerUpdates()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Starts magnetometer updates without a block handler.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
func startMagnetometerUpdates()
```

```objc
- (void) startMagnetometerUpdates;
```

## Discussion

You can get the latest magnetometer data through the [`magnetometerData`](./magnetometerdata.md) property. You must call [`stopMagnetometerUpdates()`](./stopmagnetometerupdates%28%29.md) when you no longer want your app to process magnetometer updates.

## See Also

### Managing Magnetometer Updates
- [var magnetometerUpdateInterval: TimeInterval](./magnetometerupdateinterval.md)
  The interval, in seconds, at which the system delivers magnetometer data to the block handler.
- [func startMagnetometerUpdates(to: OperationQueue, withHandler: CMMagnetometerHandler)](./startmagnetometerupdates%28to,withhandler%29.md)
  Starts magnetometer updates on an operation queue and with a specified handler.
- [func stopMagnetometerUpdates()](./stopmagnetometerupdates%28%29.md)
  Stops magnetometer updates.
- [var magnetometerData: CMMagnetometerData?](./magnetometerdata.md)
  The latest sample of magnetometer data.
- [typealias CMMagnetometerHandler](../cmmagnetometerhandler.md)
  The type of block callback for handling magnetometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates())*