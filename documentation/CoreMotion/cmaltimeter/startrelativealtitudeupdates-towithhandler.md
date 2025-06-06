# startRelativeAltitudeUpdates(to:withHandler:)

**Framework**: Core Motion  
**Kind**: method

Starts the delivery of relative altitude data to the specified handler.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
func startRelativeAltitudeUpdates(to queue: OperationQueue, withHandler handler: @escaping CMAltitudeHandler)
```

#### Discussion

Call this method to initiate the delivery of events. The altimeter object stores a strong reference to the specified queue and makes a copy of your block. If you call the method a second time, the altimeter object releases its references to the previous queue and handler before storing references to the new ones. Only the last installed handler receives events. When you no longer need the altitude data, or when an error occurs, call the [`stopRelativeAltitudeUpdates()`](cmaltimeter/stoprelativealtitudeupdates().md) method to stop the delivery of events.

If altitude data isn’t available on the current device, this method does nothing.

## Parameters

- `queue`: The operation queue on which to execute your handler block. The altimeter object stores a strong reference to this object. This parameter must not be  .
- `handler`: The handler block to execute when new altitude data is available. This parameter must not be  . For information about the format of this block, see  .

## See Also

- [func startAbsoluteAltitudeUpdates(to: OperationQueue, withHandler: CMAbsoluteAltitudeHandler)](cmaltimeter/startabsolutealtitudeupdates(to:withhandler:).md)
  Starts the delivery of absolute altitude data to the specified handler.
- [func stopAbsoluteAltitudeUpdates()](cmaltimeter/stopabsolutealtitudeupdates.md)
  Stops the delivery of absolute altitude data for this altimeter object.
- [typealias CMAbsoluteAltitudeHandler](cmabsolutealtitudehandler.md)
  A block for receiving absolute altitude data.
- [func stopRelativeAltitudeUpdates()](cmaltimeter/stoprelativealtitudeupdates.md)
  Stops the delivery of relative altitude data for the altimeter object.
- [typealias CMAltitudeHandler](cmaltitudehandler.md)
  A block for receiving relative altitude data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmaltimeter/startrelativealtitudeupdates(to:withhandler:))*