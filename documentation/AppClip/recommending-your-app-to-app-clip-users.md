# Recommending your app to App Clip users

**Framework**: App Clips

Display an overlay in your App Clip to recommend your app to users.

#### Overview

App Clips only remain on a device for a limited amount of time. If someone uses an App Clip regularly, they might want to get the corresponding app to use additional features and have the app on their home screen. With [`SKOverlay`](https://developer.apple.com/documentation/StoreKit/SKOverlay), you can recommend your full app to users and enable them to install it from within your App Clip.

> **Note**:  Don’t require users to install your app to complete a task. For user experience and design guidance, see [`Human Interface Guidelines > App Clips`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/app-clips/overview/).

If you’re using SwiftUI, make use of the [`appStoreOverlay(isPresented:configuration:)`](https://developer.apple.com/documentation/SwiftUI/View/appStoreOverlay(isPresented:configuration:)) modifier. For example usage, see [`Fruta: Building a Feature-Rich App with SwiftUI`](fruta_building_a_feature-rich_app_with_swiftui.md).

To display an overlay when using [`UIKit`](https://developer.apple.com/documentation/UIKit):

1. Create an [`SKOverlay.AppClipConfiguration`](https://developer.apple.com/documentation/StoreKit/SKOverlay/AppClipConfiguration) object.
2. Initialize [`SKOverlay`](https://developer.apple.com/documentation/StoreKit/SKOverlay) with the configuration object.
3. Present the overlay.

The following code displays the overlay at the bottom of the visible scene:

```swift
func displayOverlay() {
    guard let scene = view.window?.windowScene else { return }

    let config = SKOverlay.AppClipConfiguration(position: .bottom)
    let overlay = SKOverlay(configuration: config)
    overlay.present(in: scene)
}
```

To respond to the overlay’s appearance, dismissal, or failure to load, set the [`delegate`](https://developer.apple.com/documentation/StoreKit/SKOverlay/delegate), and implement the methods defined in [`SKOverlayDelegate`](https://developer.apple.com/documentation/StoreKit/SKOverlayDelegate).

## See Also

- [Sharing data between your App Clip and your full app](sharing-data-between-your-app-clip-and-your-full-app.md)
  Use CloudKit, Sign in with Apple, shared user defaults or containers, and the keychain to offer a smooth transition from your App Clip to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appclip/recommending-your-app-to-app-clip-users)*