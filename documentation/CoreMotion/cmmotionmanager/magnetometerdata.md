# magnetometerData

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, nullable) CMMagnetometerData * magnetometerData;
```

#### Discussion

If no magnetometer data is available, the value of this property is `nil`. An app that is receiving magnetometer data after calling [`startMagnetometerUpdates()`](./startmagnetometerupdates%28%29.md) periodically checks the value of this property and processes the magnetometer data.

## See Also

### Managing Magnetometer Updates
- [var magnetometerUpdateInterval: TimeInterval](./magnetometerupdateinterval.md)
  The interval, in seconds, at which the system delivers magnetometer data to the block handler.
- [func startMagnetometerUpdates(to: OperationQueue, withHandler: CMMagnetometerHandler)](./startmagnetometerupdates%28to,withhandler%29.md)
  Starts magnetometer updates on an operation queue and with a specified handler.
- [func startMagnetometerUpdates()](./startmagnetometerupdates%28%29.md)
  Starts magnetometer updates without a block handler.
- [func stopMagnetometerUpdates()](./stopmagnetometerupdates%28%29.md)
  Stops magnetometer updates.
- [typealias CMMagnetometerHandler](../cmmagnetometerhandler.md)
  The type of block callback for handling magnetometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerdata)*