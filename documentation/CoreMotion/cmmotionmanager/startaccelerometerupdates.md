# startAccelerometerUpdates()

**Framework**: Core Motion  
**Kind**: method

Starts accelerometer updates without a handler.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func startAccelerometerUpdates()
```

## Mentions

- [Getting raw accelerometer events](getting-raw-accelerometer-events.md)

#### Discussion

You can get the latest accelerometer data through the [`accelerometerData`](cmmotionmanager/accelerometerdata.md) property. You must call [`stopAccelerometerUpdates()`](cmmotionmanager/stopaccelerometerupdates().md) when you no longer want your app to process accelerometer updates.

## See Also

- [var accelerometerUpdateInterval: TimeInterval](cmmotionmanager/accelerometerupdateinterval.md)
  The interval, in seconds, for providing accelerometer updates to the block handler.
- [func startAccelerometerUpdates(to: OperationQueue, withHandler: CMAccelerometerHandler)](cmmotionmanager/startaccelerometerupdates(to:withhandler:).md)
  Starts accelerometer updates on an operation queue and with a specified handler.
- [func stopAccelerometerUpdates()](cmmotionmanager/stopaccelerometerupdates.md)
  Stops accelerometer updates.
- [var accelerometerData: CMAccelerometerData?](cmmotionmanager/accelerometerdata.md)
  The latest sample of accelerometer data.
- [typealias CMAccelerometerHandler](cmaccelerometerhandler.md)
  The type of block callback for handling accelerometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates())*