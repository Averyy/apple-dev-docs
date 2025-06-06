# CMAltitudeHandler

**Framework**: Core Motion  
**Kind**: typealias

A block for receiving relative altitude data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
typealias CMAltitudeHandler = (CMAltitudeData?, (any Error)?) -> Void
```

#### Discussion

You pass a block of this type to the altimeter object’s [`startRelativeAltitudeUpdates(to:withHandler:)`](cmaltimeter/startrelativealtitudeupdates(to:withhandler:).md) method when starting the delivery of altitude data.

## Parameters

- `altitudeData`: The relative change in altitude data. If there’s an error generating the data, this parameter is  .
- `error`: The error object. Returns   if the altimeter successfully delivers the altitude data. When an error occurs, you can use the information in the provided object to recover the data or to alert the user.

## See Also

- [func startAbsoluteAltitudeUpdates(to: OperationQueue, withHandler: CMAbsoluteAltitudeHandler)](cmaltimeter/startabsolutealtitudeupdates(to:withhandler:).md)
  Starts the delivery of absolute altitude data to the specified handler.
- [func stopAbsoluteAltitudeUpdates()](cmaltimeter/stopabsolutealtitudeupdates.md)
  Stops the delivery of absolute altitude data for this altimeter object.
- [typealias CMAbsoluteAltitudeHandler](cmabsolutealtitudehandler.md)
  A block for receiving absolute altitude data.
- [func startRelativeAltitudeUpdates(to: OperationQueue, withHandler: CMAltitudeHandler)](cmaltimeter/startrelativealtitudeupdates(to:withhandler:).md)
  Starts the delivery of relative altitude data to the specified handler.
- [func stopRelativeAltitudeUpdates()](cmaltimeter/stoprelativealtitudeupdates.md)
  Stops the delivery of relative altitude data for the altimeter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmaltitudehandler)*