# CoreLocationUI

**Framework**: CoreLocationUI  
**Kind**: module

Streamline access to users’ location data through a standard, secure UI.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- watchOS 10.0+

#### Overview

The CoreLocationUI framework contains a standardized UI that interacts securely with [`Core Location`](https://developer.apple.com/documentation/CoreLocation) to request authorization to access location data.

CoreLocationUI provides [`LocationButton`](locationbutton.md) for SwiftUI apps and [`CLLocationButton`](cllocationbutton.md) for UIKit apps. Add these buttons to your UI when you want someone to grant one-time authorization for your app to fetch their location. The button’s style is consistent with the standard Core Location design language, giving users a sense of familiarity and trust when they interact with it.

> **Note**: The location button ignores user input on Mac apps built with Mac Catalyst, and on compatible iPad and iPhone apps running in visionOS.

The location button ignores user input on Mac apps built with Mac Catalyst, and on compatible iPad and iPhone apps running in visionOS.

## Topics

### Location authorization
- [Sharing Your Location to Find a Park](sharing-your-location-to-find-a-park.md)
  Ask for location access using a customizable location button.
- [struct LocationButton](locationbutton.md)
  A SwiftUI button that grants one-time location authorization.
- [class CLLocationButton](cllocationbutton.md)
  A button that grants one-time location authorization.
### Button customization
- [enum CLLocationButtonIcon](cllocationbuttonicon.md)
  Constants that specify styles for the location arrow icon on the button.
- [enum CLLocationButtonLabel](cllocationbuttonlabel.md)
  Constants that specify the text of the button label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreLocationUI)*