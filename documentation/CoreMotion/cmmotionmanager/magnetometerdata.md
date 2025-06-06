# magnetometerData

**Framework**: Core Motion  
**Kind**: property

The latest sample of magnetometer data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
var magnetometerData: CMMagnetometerData? { get }
```

#### Discussion

If no magnetometer data is available, the value of this property is `nil`. An app that is receiving magnetometer data after calling [`startMagnetometerUpdates()`](cmmotionmanager/startmagnetometerupdates().md) periodically checks the value of this property and processes the magnetometer data.

## See Also

- [var magnetometerUpdateInterval: TimeInterval](cmmotionmanager/magnetometerupdateinterval.md)
  The interval, in seconds, at which the system delivers magnetometer data to the block handler.
- [func startMagnetometerUpdates(to: OperationQueue, withHandler: CMMagnetometerHandler)](cmmotionmanager/startmagnetometerupdates(to:withhandler:).md)
  Starts magnetometer updates on an operation queue and with a specified handler.
- [func startMagnetometerUpdates()](cmmotionmanager/startmagnetometerupdates.md)
  Starts magnetometer updates without a block handler.
- [func stopMagnetometerUpdates()](cmmotionmanager/stopmagnetometerupdates.md)
  Stops magnetometer updates.
- [typealias CMMagnetometerHandler](cmmagnetometerhandler.md)
  The type of block callback for handling magnetometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerdata)*