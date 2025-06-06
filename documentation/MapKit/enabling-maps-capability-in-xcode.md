# Enabling Maps capability in Xcode

**Framework**: MapKit

Configure your routing app to support providing directions.

#### Overview

A routing app, an iOS app that provides point-to-point directions, requires Maps capability to make those directions available to Maps and other apps. Maps capability allows an app to provide specific directions beyond what the Maps app supports, including subway routes, hiking trails, and bike paths. Use Xcode to enable Maps capability and select the supported modes.

##### Add Maps Capability to Your Project

1. Open your project with Xcode. In the Project navigator, select your project.
2. Choose the target for the app in the Targets section of the outline view.
3. Click the Signing & Capabilities tab in the project editor.
4. In the toolbar, click the Library button (+) to open the Capabilities library and select Maps capability.
5. Select one or more routing modes using the checkboxes displayed under the Maps capability.

The screenshot below shows the Maps capability:

![A screenshot showing the Maps capability with no route modes selected. ](https://docs-assets.developer.apple.com/published/552515a1d1d61d338158af21ea51563c/media-3737976%402x.png)

For more information on enabling capabilities in your app, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app). For more information on providing directions in your app, see [`MKDirections`](mkdirections.md).

## See Also

- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md)
  Obtain information about a point of interest that persists over its lifetime.
- [class MKMapView](mkmapview.md)
  An embeddable map interface, similar to the one that the Maps app provides.
- [class MKMapItem](mkmapitem.md)
  A point of interest on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/enabling-maps-capability-in-xcode)*