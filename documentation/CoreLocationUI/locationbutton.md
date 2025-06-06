# LocationButton

**Framework**: CoreLocationUI  
**Kind**: struct

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

#### Overview

`LocationButton` simplifies requesting one-time authorization to access location data. Add this button to your SwiftUI user interface in situations when users may want to grant temporary access to their location data each time they use a particular feature of your app.

![Screenshot of the location button with an icon that uses the filled arrow style and a label that shows Current Location.](https://docs-assets.developer.apple.com/published/d9ccebc87fa27074b42df3d0e9a3e263/locationbutton-1%402x.png)

The first time a user taps this button, [`Core Location`](https://developer.apple.com/documentation/CoreLocation) asks the user to confirm that they’re comfortable using this UI element when they want to grant temporary access to their location data. If the user agrees, the app receives temporary [`CLAuthorizationStatus.authorizedWhenInUse`](https://developer.apple.com/documentation/CoreLocation/CLAuthorizationStatus/authorizedWhenInUse) authorization, like when the user chooses  in response to your app’s standard location authorization request. This temporary authorization expires when your app is no longer in use.

After the user agrees to using `LocationButton`, the button becomes approved to request future authorizations without displaying an additional alert to the user. The next time the user taps it, this button simply grants one-time authorization without requiring confirmation.

After you receive this temporary authorization, fetch the user’s location using the [`Core Location`](https://developer.apple.com/documentation/CoreLocation) API and perform any app-specific tasks related to that location data. Connect the button to initiate the tasks you want to perform after getting authorization by specifying an action when you create the button. Keep in mind that this action activates every time the user taps this button, regardless of whether the app already has location authorization.

Create a `LocationButton` in SwiftUI like this:

```swift
LocationButton(.currentLocation) {
    // Fetch location with Core Location.
}
.symbolVariant(.fill)
.labelStyle(.titleAndIcon)
```

> ❗ **Important**: When a user taps the button, it only provides one-time authorization to fetch location data — not the location data itself. For more details about fetching location data, see [`Configuring your app to use location services`](https://developer.apple.com/documentation/CoreLocation/configuring-your-app-to-use-location-services).

When a user taps the button, it only provides one-time authorization to fetch location data — not the location data itself. For more details about fetching location data, see [`Configuring your app to use location services`](https://developer.apple.com/documentation/CoreLocation/configuring-your-app-to-use-location-services).

Configure the button to display an icon, a label, or both using the [`labelStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/labelStyle(_:)) view modifier. If you include an icon, you can customize its appearance using the [`symbolVariant(_:)`](https://developer.apple.com/documentation/SwiftUI/View/symbolVariant(_:)) modifier. For design guidance, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/accessing-user-data/).

## Topics

### Creating a location button
- [init(LocationButton.Title?, action: () -> Void)](locationbutton/init(_:action:).md)
  Creates a location button with the specified title and action.
- [LocationButton.Title](locationbutton/title.md)
  Constants that specify the text of a button title.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)

## See Also

- [Sharing Your Location to Find a Park](sharing-your-location-to-find-a-park.md)
  Ask for location access using a customizable location button.
- [class CLLocationButton](cllocationbutton.md)
  A button that grants one-time location authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocationui/locationbutton)*