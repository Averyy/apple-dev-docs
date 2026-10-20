# startAccelerometerUpdates()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) startAccelerometerUpdates;
```

## Mentions

- [Getting raw accelerometer events](../getting-raw-accelerometer-events.md)

#### Discussion

You can get the latest accelerometer data through the [`accelerometerData`](./accelerometerdata.md) property. You must call [`stopAccelerometerUpdates()`](./stopaccelerometerupdates%28%29.md) when you no longer want your app to process accelerometer updates.

## See Also

### Managing Accelerometer Updates
- [var accelerometerUpdateInterval: TimeInterval](./accelerometerupdateinterval.md)
  The interval, in seconds, for providing accelerometer updates to the block handler.
- [func startAccelerometerUpdates(to: OperationQueue, withHandler: CMAccelerometerHandler)](./startaccelerometerupdates%28to,withhandler%29.md)
  Starts accelerometer updates on an operation queue and with a specified handler.
- [func stopAccelerometerUpdates()](./stopaccelerometerupdates%28%29.md)
  Stops accelerometer updates.
- [var accelerometerData: CMAccelerometerData?](./accelerometerdata.md)
  The latest sample of accelerometer data.
- [typealias CMAccelerometerHandler](../cmaccelerometerhandler.md)
  The type of block callback for handling accelerometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates())*