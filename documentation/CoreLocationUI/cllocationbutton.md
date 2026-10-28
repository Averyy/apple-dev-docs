# CLLocationButton

**Framework**: CoreLocationUI  
**Kind**: class  
**Role**: Class

A button that grants one-time location authorization.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
class CLLocationButton
```

```objc
@interface CLLocationButton : UIControl
```

## Overview

`CLLocationButton` simplifies requesting one-time authorization to access location data. Add this button to your user interface in situations when users may want to grant temporary access to their location data each time they use a particular feature of your app.

![Screenshot of the location button with an icon that uses the filled arrow](https://developer.apple.com/tutorials/images/com.apple.CoreLocationUI/cllocationbutton-1@2x.png)

The first time a user taps this button, [Core Location](../CoreLocation/CoreLocation.md) asks the user to confirm that they’re comfortable using this UI element when they want to grant temporary access to their location data. If the user agrees, the app receives temporary [`CLAuthorizationStatus.authorizedWhenInUse`](../CoreLocation/clauthorizationstatus/authorizedwheninuse.md) authorization, like when the user chooses *Allow Once* in response to your app’s standard location authorization request. This temporary authorization expires when your app is no longer in use.

After the user agrees to using `CLLocationButton`, the button becomes approved to request future authorizations without displaying an additional alert to the user. The next time the user taps it, this button simply grants one-time authorization without requiring confirmation.

After you receive this temporary authorization, fetch the user’s location using the [Core Location](../CoreLocation/CoreLocation.md) API and perform any app-specific tasks related to that location data. Connect the button to initiate the tasks you want to perform after getting authorization by adding a target and action to the button. Keep in mind that this action activates every time the user taps this button, regardless of whether the app already has location authorization.

Create a `CLLocationButton` in Interface Builder or in code, like this:

```swift
let locationButton = CLLocationButton()
locationButton.icon = .arrowFilled
locationButton.label = .currentLocation
locationButton.cornerRadius = 25.0
locationButton.addTarget(self, action: #selector(userPressedLocationButton), for: .touchUpInside)
```

> ❗ **Important**: When a user taps the button, it only provides one-time authorization to fetch location data — not the location data itself. For more details about fetching location data, see [Configuring your app to use location services](../CoreLocation/configuring-your-app-to-use-location-services.md).

Configure the button’s content by specifying its [`icon`](./cllocationbutton/icon.md) and [`label`](./cllocationbutton/label.md) styles. Customize its appearance using the [`cornerRadius`](./cllocationbutton/cornerradius.md) and [`fontSize`](./cllocationbutton/fontsize.md) properties, or the standard view appearance properties [`backgroundColor`](../UIKit/uiview/backgroundcolor.md) and [`tintColor`](../UIKit/uiview/tintcolor.md). For design guidance, see [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/accessing-user-data/).

## Topics

### Customizing the icon style
- [var icon: CLLocationButtonIcon](./cllocationbutton/icon.md)
  The style of the location arrow icon on the button.
### Customizing the label text
- [var label: CLLocationButtonLabel](./cllocationbutton/label.md)
  The text of the button label.
### Customizing the button appearance
- [var cornerRadius: CGFloat](./cllocationbutton/cornerradius.md)
  The corner radius of the button.
- [var fontSize: CGFloat](./cllocationbutton/fontsize.md)
  The font size of the text on the button.

## Relationships

### Inherits From
- [UIControl](../UIKit/uicontrol.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContextMenuInteractionDelegate](../UIKit/uicontextmenuinteractiondelegate.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Location authorization
- [Sharing Your Location to Find a Park](./sharing-your-location-to-find-a-park.md)
  Ask for location access using a customizable location button.
- [struct LocationButton](./locationbutton.md)
  A SwiftUI button that grants one-time location authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocationui/cllocationbutton)*