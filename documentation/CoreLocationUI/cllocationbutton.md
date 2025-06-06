# CLLocationButton

**Framework**: CoreLocationUI  
**Kind**: class

A button that grants one-time location authorization.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
@MainActor
class CLLocationButton
```

#### Overview

`CLLocationButton` simplifies requesting one-time authorization to access location data. Add this button to your user interface in situations when users may want to grant temporary access to their location data each time they use a particular feature of your app.

![Screenshot of the location button with an icon that uses the filled arrow](https://docs-assets.developer.apple.com/published/d9ccebc87fa27074b42df3d0e9a3e263/cllocationbutton-1%402x.png)

The first time a user taps this button, [`Core Location`](https://developer.apple.com/documentation/CoreLocation) asks the user to confirm that they’re comfortable using this UI element when they want to grant temporary access to their location data. If the user agrees, the app receives temporary [`CLAuthorizationStatus.authorizedWhenInUse`](https://developer.apple.com/documentation/CoreLocation/CLAuthorizationStatus/authorizedWhenInUse) authorization, like when the user chooses  in response to your app’s standard location authorization request. This temporary authorization expires when your app is no longer in use.

After the user agrees to using `CLLocationButton`, the button becomes approved to request future authorizations without displaying an additional alert to the user. The next time the user taps it, this button simply grants one-time authorization without requiring confirmation.

After you receive this temporary authorization, fetch the user’s location using the [`Core Location`](https://developer.apple.com/documentation/CoreLocation) API and perform any app-specific tasks related to that location data. Connect the button to initiate the tasks you want to perform after getting authorization by adding a target and action to the button. Keep in mind that this action activates every time the user taps this button, regardless of whether the app already has location authorization.

Create a `CLLocationButton` in Interface Builder or in code, like this:

```swift
let locationButton = CLLocationButton()
locationButton.icon = .arrowFilled
locationButton.label = .currentLocation
locationButton.cornerRadius = 25.0
locationButton.addTarget(self, action: #selector(userPressedLocationButton), for: .touchUpInside)
```

> ❗ **Important**: When a user taps the button, it only provides one-time authorization to fetch location data — not the location data itself. For more details about fetching location data, see [`Configuring your app to use location services`](https://developer.apple.com/documentation/CoreLocation/configuring-your-app-to-use-location-services).

When a user taps the button, it only provides one-time authorization to fetch location data — not the location data itself. For more details about fetching location data, see [`Configuring your app to use location services`](https://developer.apple.com/documentation/CoreLocation/configuring-your-app-to-use-location-services).

Configure the button’s content by specifying its [`icon`](cllocationbutton/icon.md) and [`label`](cllocationbutton/label.md) styles. Customize its appearance using the [`cornerRadius`](cllocationbutton/cornerradius.md) and [`fontSize`](cllocationbutton/fontsize.md) properties, or the standard view appearance properties [`backgroundColor`](https://developer.apple.com/documentation/UIKit/UIView/backgroundColor) and [`tintColor`](https://developer.apple.com/documentation/UIKit/UIView/tintColor). For design guidance, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/accessing-user-data/).

## Topics

### Customizing the icon style
- [var icon: CLLocationButtonIcon](cllocationbutton/icon.md)
  The style of the location arrow icon on the button.
### Customizing the label text
- [var label: CLLocationButtonLabel](cllocationbutton/label.md)
  The text of the button label.
### Customizing the button appearance
- [var cornerRadius: CGFloat](cllocationbutton/cornerradius.md)
  The corner radius of the button.
- [var fontSize: CGFloat](cllocationbutton/fontsize.md)
  The font size of the text on the button.

## Relationships

### Inherits From
- [UIControl](../UIKit/UIControl.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContextMenuInteractionDelegate](../UIKit/UIContextMenuInteractionDelegate.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Sharing Your Location to Find a Park](sharing-your-location-to-find-a-park.md)
  Ask for location access using a customizable location button.
- [struct LocationButton](locationbutton.md)
  A SwiftUI button that grants one-time location authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocationui/cllocationbutton)*