# locationManagerShouldDisplayHeadingCalibration(_:)

**Framework**: Core Location  
**Kind**: method

Asks the delegate whether the heading calibration alert should be displayed.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
optional func locationManagerShouldDisplayHeadingCalibration(_ manager: CLLocationManager) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if you want to allow the heading calibration alert to be displayed; [`false`](https://developer.apple.com/documentation/Swift/false) if you do not.

#### Discussion

Core Location may call this method in an effort to calibrate the onboard hardware used to determine heading values. Typically, Core Location calls this method at the following times:

- The first time heading updates are ever requested
- When Core Location observes a significant change in magnitude or inclination of the observed magnetic field

If you return [`true`](https://developer.apple.com/documentation/Swift/true) from this method, Core Location displays the heading calibration alert on top of the current window immediately. The calibration alert prompts the user to move the device in a particular pattern so that Core Location can distinguish between the Earth’s magnetic field and any local magnetic fields. The alert remains visible until calibration is complete or until you explicitly dismiss it by calling the [`dismissHeadingCalibrationDisplay()`](cllocationmanager/dismissheadingcalibrationdisplay().md) method. In the latter case, you can use this method to set up a timer and dismiss the interface after a specified amount of time has elapsed.

> **Note**:  The calibration process is able to filter out only those magnetic fields that move with the device. To calibrate a device that is near other sources of magnetic interference, the user must either move the device away from the source or move the source in conjunction with the device during the calibration process.

If you return [`false`](https://developer.apple.com/documentation/Swift/false) from this method or do not provide an implementation for it in your delegate, Core Location does not display the heading calibration alert. Even if the alert is not displayed, calibration can still occur naturally when any interfering magnetic fields move away from the device. However, if the device is unable to calibrate itself for any reason, the value in the [`headingAccuracy`](clheading/headingaccuracy.md) property of any subsequent events will reflect the uncalibrated readings.

## Parameters

- `manager`: The location manager object coordinating the display of the heading calibration alert.

## See Also

- [func locationManager(CLLocationManager, didUpdateHeading: CLHeading)](cllocationmanagerdelegate/locationmanager(_:didupdateheading:).md)
  Tells the delegate that the location manager received updated heading information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanagershoulddisplayheadingcalibration(_:))*