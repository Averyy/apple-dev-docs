# Recommending your app to App Clip users

**Framework**: App Clips

Display an overlay in your App Clip to recommend your app to users.

#### Overview

App Clips only remain on a device for a limited amount of time. If someone uses an App Clip regularly, they might want to get the corresponding app to use additional features and have the app on their home screen. With [`SKOverlay`](https://developer.apple.com/documentation/storekit/skoverlay), you can recommend your full app to users and enable them to install it from within your App Clip.

> **Note**:  Don’t require users to install your app to complete a task. For user experience and design guidance, see [`Human Interface Guidelines > App Clips`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/app-clips/overview/).

If you’re using SwiftUI, make use of the [`appStoreOverlay(isPresented:configuration:)`](https://developer.apple.com/documentation/swiftui/view/appstoreoverlay(ispresented:configuration:)) modifier. For example usage, see [`Fruta: Building a feature-rich app with SwiftUI`](fruta-building-a-feature-rich-app-with-swiftui.md).

To display an overlay when using [`UIKit`](https://developer.apple.com/documentation/uikit):

1. Create an [`SKOverlay.AppClipConfiguration`](https://developer.apple.com/documentation/storekit/skoverlay/appclipconfiguration) object.
2. Initialize [`SKOverlay`](https://developer.apple.com/documentation/storekit/skoverlay) with the configuration object.
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

To respond to the overlay’s appearance, dismissal, or failure to load, set the [`delegate`](https://developer.apple.com/documentation/storekit/skoverlay/delegate), and implement the methods defined in [`SKOverlayDelegate`](https://developer.apple.com/documentation/storekit/skoverlaydelegate).

## See Also

- [Sharing data between your App Clip and your full app](sharing-data-between-your-app-clip-and-your-full-app.md)
  Use CloudKit, Sign in with Apple, shared user defaults or containers, and the keychain to offer a smooth transition from your App Clip to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appclip/recommending-your-app-to-app-clip-users)*