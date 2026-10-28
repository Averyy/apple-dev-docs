# LocationButton

**Framework**: CoreLocationUI  
**Kind**: struct  
**Role**: Structure

A SwiftUI button that grants one-time location authorization.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- watchOS 8.0+

## Declaration

```swift
@MainActor
@preconcurrency struct LocationButton
```

## Overview

`LocationButton` simplifies requesting one-time authorization to access location data. Add this button to your SwiftUI user interface in situations when users may want to grant temporary access to their location data each time they use a particular feature of your app.

![Screenshot of the location button with an icon that uses the filled arrow style and a label that shows Current Location.](https://developer.apple.com/tutorials/images/com.apple.CoreLocationUI/locationbutton-1@2x.png)

The first time a user taps this button, [Core Location](../CoreLocation/CoreLocation.md) asks the user to confirm that they’re comfortable using this UI element when they want to grant temporary access to their location data. If the user agrees, the app receives temporary [`CLAuthorizationStatus.authorizedWhenInUse`](../CoreLocation/clauthorizationstatus/authorizedwheninuse.md) authorization, like when the user chooses *Allow Once* in response to your app’s standard location authorization request. This temporary authorization expires when your app is no longer in use.

After the user agrees to using `LocationButton`, the button becomes approved to request future authorizations without displaying an additional alert to the user. The next time the user taps it, this button simply grants one-time authorization without requiring confirmation.

After you receive this temporary authorization, fetch the user’s location using the [Core Location](../CoreLocation/CoreLocation.md) API and perform any app-specific tasks related to that location data. Connect the button to initiate the tasks you want to perform after getting authorization by specifying an action when you create the button. Keep in mind that this action activates every time the user taps this button, regardless of whether the app already has location authorization.

Create a `LocationButton` in SwiftUI like this:

```swift
LocationButton(.currentLocation) {
    // Fetch location with Core Location.
}
.symbolVariant(.fill)
.labelStyle(.titleAndIcon)
```

> ❗ **Important**: When a user taps the button, it only provides one-time authorization to fetch location data — not the location data itself. For more details about fetching location data, see [Configuring your app to use location services](../CoreLocation/configuring-your-app-to-use-location-services.md).

Configure the button to display an icon, a label, or both using the [`labelStyle(_:)`](../SwiftUI/view/labelstyle%28_%29.md) view modifier. If you include an icon, you can customize its appearance using the [`symbolVariant(_:)`](../SwiftUI/view/symbolvariant%28_%29.md) modifier. For design guidance, see [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/accessing-user-data/).

## Topics

### Creating a location button
- [init(LocationButton.Title?, action: () -> Void)](./locationbutton/init%28_,action%29.md)
  Creates a location button with the specified title and action.
- [LocationButton.Title](./locationbutton/title.md)
  Constants that specify the text of a button title.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)

## See Also

### Location authorization
- [Sharing Your Location to Find a Park](./sharing-your-location-to-find-a-park.md)
  Ask for location access using a customizable location button.
- [class CLLocationButton](./cllocationbutton.md)
  A button that grants one-time location authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocationui/locationbutton)*