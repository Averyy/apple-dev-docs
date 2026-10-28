# CMAccelerometerHandler

**Framework**: Core Motion  
**Kind**: typealias  
**Role**: Type Alias

The type of block callback for handling accelerometer data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias CMAccelerometerHandler = (CMAccelerometerData?, (any Error)?) -> Void
```

```c
typedef void (^)(CMAccelerometerData *, NSError *) CMAccelerometerHandler;
```

## Discussion

Blocks of type `CMAccelerometerHandler` are called when there is accelerometer data to process. You pass the block into [`startAccelerometerUpdates(to:withHandler:)`](./cmmotionmanager/startaccelerometerupdates%28to,withhandler%29.md) as the second argument. Blocks of this type return no value but take two arguments:

- **`accelerometerData`**: An object that encapsulates a [`CMAcceleration`](./cmacceleration.md) structure with fields holding acceleration values for the three axes of movement.
- **`error`**: An error object representing an error encountered in providing accelerometer updates. If an error occurs, you should stop accelerometer updates and inform the user of the problem. If there is no error, this argument is `nil`. Core Motion errors are of the [`CMErrorDomain`](./cmerrordomain.md) domain and the [`CMError`](./cmerror.md) type.

## See Also

### Managing Accelerometer Updates
- [var accelerometerUpdateInterval: TimeInterval](./cmmotionmanager/accelerometerupdateinterval.md)
  The interval, in seconds, for providing accelerometer updates to the block handler.
- [func startAccelerometerUpdates(to: OperationQueue, withHandler: CMAccelerometerHandler)](./cmmotionmanager/startaccelerometerupdates%28to,withhandler%29.md)
  Starts accelerometer updates on an operation queue and with a specified handler.
- [func startAccelerometerUpdates()](./cmmotionmanager/startaccelerometerupdates%28%29.md)
  Starts accelerometer updates without a handler.
- [func stopAccelerometerUpdates()](./cmmotionmanager/stopaccelerometerupdates%28%29.md)
  Stops accelerometer updates.
- [var accelerometerData: CMAccelerometerData?](./cmmotionmanager/accelerometerdata.md)
  The latest sample of accelerometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler)*