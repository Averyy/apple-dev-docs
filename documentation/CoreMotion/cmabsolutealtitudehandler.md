# CMAbsoluteAltitudeHandler

**Framework**: Core Motion  
**Kind**: typealias

A block for receiving absolute altitude data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
typealias CMAbsoluteAltitudeHandler = (CMAbsoluteAltitudeData?, (any Error)?) -> Void
```

#### Discussion

You pass a block of this type to the altimeter object’s [`startAbsoluteAltitudeUpdates(to:withHandler:)`](cmaltimeter/startabsolutealtitudeupdates(to:withhandler:).md) method when starting the delivery of altitude data.

> **Note**:  Absolute altitude is only available on iPhone 12 and later and Apple Watch 6 or SE and later.

## Parameters

- `altitudeData`: The current altitude for the device. If there’s an error generating the data, this parameter is  .
- `error`: The error object. Returns   if the altimeter successfully delivers the altitude data. When an error occurs, you can use the information in the provided object to recover the data or to alert the user.

## See Also

- [func startAbsoluteAltitudeUpdates(to: OperationQueue, withHandler: CMAbsoluteAltitudeHandler)](cmaltimeter/startabsolutealtitudeupdates(to:withhandler:).md)
  Starts the delivery of absolute altitude data to the specified handler.
- [func stopAbsoluteAltitudeUpdates()](cmaltimeter/stopabsolutealtitudeupdates.md)
  Stops the delivery of absolute altitude data for this altimeter object.
- [func startRelativeAltitudeUpdates(to: OperationQueue, withHandler: CMAltitudeHandler)](cmaltimeter/startrelativealtitudeupdates(to:withhandler:).md)
  Starts the delivery of relative altitude data to the specified handler.
- [func stopRelativeAltitudeUpdates()](cmaltimeter/stoprelativealtitudeupdates.md)
  Stops the delivery of relative altitude data for the altimeter object.
- [typealias CMAltitudeHandler](cmaltitudehandler.md)
  A block for receiving relative altitude data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudehandler)*