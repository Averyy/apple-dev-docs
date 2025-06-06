# CMMagnetometerHandler

**Framework**: Core Motion  
**Kind**: typealias

The type of block callback for handling magnetometer data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
typealias CMMagnetometerHandler = (CMMagnetometerData?, (any Error)?) -> Void
```

#### Discussion

Blocks of type `CMMagnetometerHandler` are called when there is magnetometer data to process. You pass the block into the [`startMagnetometerUpdates(to:withHandler:)`](cmmotionmanager/startmagnetometerupdates(to:withhandler:).md) method as the second argument. Blocks of this type return no value but take two arguments:

## See Also

- [var magnetometerUpdateInterval: TimeInterval](cmmotionmanager/magnetometerupdateinterval.md)
  The interval, in seconds, at which the system delivers magnetometer data to the block handler.
- [func startMagnetometerUpdates(to: OperationQueue, withHandler: CMMagnetometerHandler)](cmmotionmanager/startmagnetometerupdates(to:withhandler:).md)
  Starts magnetometer updates on an operation queue and with a specified handler.
- [func startMagnetometerUpdates()](cmmotionmanager/startmagnetometerupdates.md)
  Starts magnetometer updates without a block handler.
- [func stopMagnetometerUpdates()](cmmotionmanager/stopmagnetometerupdates.md)
  Stops magnetometer updates.
- [var magnetometerData: CMMagnetometerData?](cmmotionmanager/magnetometerdata.md)
  The latest sample of magnetometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmagnetometerhandler)*