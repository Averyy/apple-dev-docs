# CMAltitudeHandler

**Framework**: Core Motion  
**Kind**: typealias  
**Role**: Type Alias

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

```c
typedef void (^)(CMAltitudeData *, NSError *) CMAltitudeHandler;
```

## Discussion

You pass a block of this type to the altimeter object’s [`startRelativeAltitudeUpdates(to:withHandler:)`](./cmaltimeter/startrelativealtitudeupdates%28to,withhandler%29.md) method when starting the delivery of altitude data.

## Parameters

- `altitudeData`: The relative change in altitude data. If there’s an error generating the data, this parameter is `nil`.
- `error`: The error object. Returns `nil` if the altimeter successfully delivers the altitude data. When an error occurs, you can use the information in the provided object to recover the data or to alert the user.

## See Also

### Starting and Stopping Altitude Updates
- [func startAbsoluteAltitudeUpdates(to: OperationQueue, withHandler: CMAbsoluteAltitudeHandler)](./cmaltimeter/startabsolutealtitudeupdates%28to,withhandler%29.md)
  Starts the delivery of absolute altitude data to the specified handler.
- [func stopAbsoluteAltitudeUpdates()](./cmaltimeter/stopabsolutealtitudeupdates%28%29.md)
  Stops the delivery of absolute altitude data for this altimeter object.
- [typealias CMAbsoluteAltitudeHandler](./cmabsolutealtitudehandler.md)
  A block for receiving absolute altitude data.
- [func startRelativeAltitudeUpdates(to: OperationQueue, withHandler: CMAltitudeHandler)](./cmaltimeter/startrelativealtitudeupdates%28to,withhandler%29.md)
  Starts the delivery of relative altitude data to the specified handler.
- [func stopRelativeAltitudeUpdates()](./cmaltimeter/stoprelativealtitudeupdates%28%29.md)
  Stops the delivery of relative altitude data for the altimeter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmaltitudehandler)*