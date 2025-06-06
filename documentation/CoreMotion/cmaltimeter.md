# CMAltimeter

**Framework**: Core Motion  
**Kind**: class

An object that initiates the delivery of altitude-related changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
class CMAltimeter
```

#### Overview

Altitude events report changes in both the relative and absolute altitude. For example, a hiking app could use this object to track the user’s elevation change over the course of a hike, or to report their current absolute altitude during the hike.

Because altitude events may not be available on all devices, always call the [`isRelativeAltitudeAvailable()`](cmaltimeter/isrelativealtitudeavailable().md) method before starting relative altitude updates, and call [`isAbsoluteAltitudeAvailable()`](cmaltimeter/isabsolutealtitudeavailable().md) before starting absolute altitude updates.

After checking the availability of altitude data, call the [`startRelativeAltitudeUpdates(to:withHandler:)`](cmaltimeter/startrelativealtitudeupdates(to:withhandler:).md) method to start receiving relative altitude data, or call the [`startAbsoluteAltitudeUpdates(to:withHandler:)`](cmaltimeter/startabsolutealtitudeupdates(to:withhandler:).md) method for absolute altitude data.

Core Motion generates events at regular intervals (regardless of whether the data has changed) and delivers them to the block you specified. When you no longer need the event data, call the [`stopRelativeAltitudeUpdates()`](cmaltimeter/stoprelativealtitudeupdates().md) or [`stopAbsoluteAltitudeUpdates()`](cmaltimeter/stopabsolutealtitudeupdates().md) methods respectively.

> ❗ **Important**:  To use this API, you must include the [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription) key in your app’s `Info.plist` file and provide a usage description string for this key. The usage description appears in the prompt that the user must accept the first time the system asks the user to access motion data for your app. If you don’t include a usage description string, your app crashes when you call this API.

 To use this API, you must include the [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription) key in your app’s `Info.plist` file and provide a usage description string for this key. The usage description appears in the prompt that the user must accept the first time the system asks the user to access motion data for your app. If you don’t include a usage description string, your app crashes when you call this API.

## Topics

### Determining Altitude Availability
- [class func isAbsoluteAltitudeAvailable() -> Bool](cmaltimeter/isabsolutealtitudeavailable.md)
  Returns a Boolean value indicating whether the current device reports changes in the absolute altitude.
- [class func isRelativeAltitudeAvailable() -> Bool](cmaltimeter/isrelativealtitudeavailable.md)
  Returns a Boolean value indicating whether the current device supports generating data for relative altitude changes.
- [class func authorizationStatus() -> CMAuthorizationStatus](cmaltimeter/authorizationstatus.md)
  Returns a value indicating whether the app is authorized to retrieve altimeter data.
- [enum CMAuthorizationStatus](cmauthorizationstatus.md)
  The authorization status for motion-related features.
### Starting and Stopping Altitude Updates
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
- [typealias CMAltitudeHandler](cmaltitudehandler.md)
  A block for receiving relative altitude data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CMAbsoluteAltitudeData](cmabsolutealtitudedata.md)
  Data that records a change in absolute altitude.
- [class CMAltitudeData](cmaltitudedata.md)
  Data for a recorded change in altitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmaltimeter)*