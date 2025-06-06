# startMagnetometerUpdates()

**Framework**: Core Motion  
**Kind**: method

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

#### Discussion

You can get the latest magnetometer data through the [`magnetometerData`](cmmotionmanager/magnetometerdata.md) property. You must call [`stopMagnetometerUpdates()`](cmmotionmanager/stopmagnetometerupdates().md) when you no longer want your app to process magnetometer updates.

## See Also

- [var magnetometerUpdateInterval: TimeInterval](cmmotionmanager/magnetometerupdateinterval.md)
  The interval, in seconds, at which the system delivers magnetometer data to the block handler.
- [func startMagnetometerUpdates(to: OperationQueue, withHandler: CMMagnetometerHandler)](cmmotionmanager/startmagnetometerupdates(to:withhandler:).md)
  Starts magnetometer updates on an operation queue and with a specified handler.
- [func stopMagnetometerUpdates()](cmmotionmanager/stopmagnetometerupdates.md)
  Stops magnetometer updates.
- [var magnetometerData: CMMagnetometerData?](cmmotionmanager/magnetometerdata.md)
  The latest sample of magnetometer data.
- [typealias CMMagnetometerHandler](cmmagnetometerhandler.md)
  The type of block callback for handling magnetometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startmagnetometerupdates())*