# stopRelativeAltitudeUpdates()

**Framework**: Core Motion  
**Kind**: method

Stops the delivery of relative altitude data for the altimeter object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
func stopRelativeAltitudeUpdates()
```

#### Discussion

Calling this method ends the delivery of relative altitude events and releases the references to the operation queue and block that you specified in the [`startRelativeAltitudeUpdates(to:withHandler:)`](cmaltimeter/startrelativealtitudeupdates(to:withhandler:).md) method. If you haven’t started delivering data, or if you’ve already called [`stopRelativeAltitudeUpdates()`](cmaltimeter/stoprelativealtitudeupdates().md), this method does nothing.

## See Also

- [func startAbsoluteAltitudeUpdates(to: OperationQueue, withHandler: CMAbsoluteAltitudeHandler)](cmaltimeter/startabsolutealtitudeupdates(to:withhandler:).md)
  Starts the delivery of absolute altitude data to the specified handler.
- [func stopAbsoluteAltitudeUpdates()](cmaltimeter/stopabsolutealtitudeupdates.md)
  Stops the delivery of absolute altitude data for this altimeter object.
- [typealias CMAbsoluteAltitudeHandler](cmabsolutealtitudehandler.md)
  A block for receiving absolute altitude data.
- [func startRelativeAltitudeUpdates(to: OperationQueue, withHandler: CMAltitudeHandler)](cmaltimeter/startrelativealtitudeupdates(to:withhandler:).md)
  Starts the delivery of relative altitude data to the specified handler.
- [typealias CMAltitudeHandler](cmaltitudehandler.md)
  A block for receiving relative altitude data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmaltimeter/stoprelativealtitudeupdates())*