# stopAbsoluteAltitudeUpdates()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Stops the delivery of absolute altitude data for this altimeter object.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- watchOS 8.0+

## Declaration

```swift
func stopAbsoluteAltitudeUpdates()
```

```objc
- (void) stopAbsoluteAltitudeUpdates;
```

#### Discussion

Calling this method ends the delivery of absolute altitude events and releases the references to the operation queue and block that you specified in the [`startAbsoluteAltitudeUpdates(to:withHandler:)`](./startabsolutealtitudeupdates%28to,withhandler%29.md) method. If you haven’t started delivering data, or if you’ve already called `stopAbsoluteAltitudeUpdates()`, this method does nothing.

> **Note**:  Absolute altitude is only available on iPhone 12 and later and Apple Watch 6 or SE and later.

## See Also

### Starting and Stopping Altitude Updates
- [func startAbsoluteAltitudeUpdates(to: OperationQueue, withHandler: CMAbsoluteAltitudeHandler)](./startabsolutealtitudeupdates%28to,withhandler%29.md)
  Starts the delivery of absolute altitude data to the specified handler.
- [typealias CMAbsoluteAltitudeHandler](../cmabsolutealtitudehandler.md)
  A block for receiving absolute altitude data.
- [func startRelativeAltitudeUpdates(to: OperationQueue, withHandler: CMAltitudeHandler)](./startrelativealtitudeupdates%28to,withhandler%29.md)
  Starts the delivery of relative altitude data to the specified handler.
- [func stopRelativeAltitudeUpdates()](./stoprelativealtitudeupdates%28%29.md)
  Stops the delivery of relative altitude data for the altimeter object.
- [typealias CMAltitudeHandler](../cmaltitudehandler.md)
  A block for receiving relative altitude data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmaltimeter/stopabsolutealtitudeupdates())*