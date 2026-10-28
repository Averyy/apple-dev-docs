# startAbsoluteAltitudeUpdates(to:withHandler:)

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Starts the delivery of absolute altitude data to the specified handler.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- watchOS 8.0+

## Declaration

```swift
func startAbsoluteAltitudeUpdates(to queue: OperationQueue, withHandler handler: @escaping CMAbsoluteAltitudeHandler)
```

```objc
- (void) startAbsoluteAltitudeUpdatesToQueue:(NSOperationQueue *) queue withHandler:(CMAbsoluteAltitudeHandler) handler;
```

## Discussion

Call [`isAbsoluteAltitudeAvailable()`](./isabsolutealtitudeavailable%28%29.md) to verify that the current device supports absolute altitude updates before calling the `startAbsoluteAltitudeUpdates(to:withHandler:)` method.

> **Note**:  Absolute altitude is only available on iPhone 12 and later and Apple Watch 6 or SE and later.

## Parameters

- `queue`: The operation queue on which to execute your handler block. The altimeter object stores a strong reference to this object. This parameter must not be `nil`.
- `handler`: The handler block to execute when new altitude data is available. This parameter must not be `nil`. For information about the format of this block, see [`CMAbsoluteAltitudeHandler`](../cmabsolutealtitudehandler.md).

## See Also

### Starting and Stopping Altitude Updates
- [func stopAbsoluteAltitudeUpdates()](./stopabsolutealtitudeupdates%28%29.md)
  Stops the delivery of absolute altitude data for this altimeter object.
- [typealias CMAbsoluteAltitudeHandler](../cmabsolutealtitudehandler.md)
  A block for receiving absolute altitude data.
- [func startRelativeAltitudeUpdates(to: OperationQueue, withHandler: CMAltitudeHandler)](./startrelativealtitudeupdates%28to,withhandler%29.md)
  Starts the delivery of relative altitude data to the specified handler.
- [func stopRelativeAltitudeUpdates()](./stoprelativealtitudeupdates%28%29.md)
  Stops the delivery of relative altitude data for the altimeter object.
- [typealias CMAltitudeHandler](../cmaltitudehandler.md)
  A block for receiving relative altitude data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmaltimeter/startabsolutealtitudeupdates(to:withhandler:))*