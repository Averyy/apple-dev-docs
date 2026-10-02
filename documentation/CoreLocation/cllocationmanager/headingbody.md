# headingBody

**Framework**: Core Location  
**Kind**: property

A physical body or view that defines the reference orientation for heading calculations.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var headingBody: (any CLBodyIdentifiable)? { get set }
```

#### Discussion

Set this property to associate heading calculations with a specific body or view, such as a [`UIKit`](https://developer.apple.com/documentation/uikit) [`UIView`](https://developer.apple.com/documentation/uikit/uiview) that conforms to [`CLBodyIdentifiable`](clbodyidentifiable.md).

When this property is `nil`, the location manager uses the physical orientation specified by [`headingOrientation`](cllocationmanager/headingorientation.md). When you assign a view conforming to [`CLBodyIdentifiable`](clbodyidentifiable.md) to this property, Core Location calculates heading relative to the top of that view and ignores [`headingOrientation`](cllocationmanager/headingorientation.md). The system updates this calculation automatically whenever the view rotates or changes position.

On iPhone Duo, setting this property also identifies which display your app occupies. For example, when iPhone Duo rests camera-side down on a surface, setting `headingBody` to your view allows your app to receive heading data relative to that active display and detect which face is up.

```swift
let locationManager = CLLocationManager()

override func viewDidLoad() {
    super.viewDidLoad()
    
    // Align heading updates with this view's orientation.
    locationManager.headingBody = view
    
    locationManager.delegate = self
    locationManager.startUpdatingHeading()
}
```

> **Note**: On platforms where body-relative heading calculation isn’t supported, the location manager reports heading data using the default device orientation.

## Topics

### Heading configuration
- [protocol CLBodyIdentifiable](clbodyidentifiable.md)
  A type that identifies a physical body or view for heading calculations.
- [var headingOrientation: CLDeviceOrientation](cllocationmanager/headingorientation.md)
  The device orientation to use when computing heading values.

## See Also

- [func startUpdatingHeading()](cllocationmanager/startupdatingheading.md)
  Starts the generation of updates that report the user’s current heading.
- [func stopUpdatingHeading()](cllocationmanager/stopupdatingheading.md)
  Stops the generation of heading updates.
- [func dismissHeadingCalibrationDisplay()](cllocationmanager/dismissheadingcalibrationdisplay.md)
  Dismisses the heading calibration view from the screen immediately.
- [var headingFilter: CLLocationDegrees](cllocationmanager/headingfilter.md)
  The minimum angular change in degrees required to generate new heading events.
- [let kCLHeadingFilterNone: CLLocationDegrees](kclheadingfilternone.md)
  A constant indicating that all header values should be reported.
- [typealias CLLocationDegrees](cllocationdegrees.md)
  A latitude or longitude value specified in degrees.
- [var headingOrientation: CLDeviceOrientation](cllocationmanager/headingorientation.md)
  The device orientation to use when computing heading values.
- [enum CLDeviceOrientation](cldeviceorientation.md)
  Constants indicating the physical orientation of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/headingbody)*