# TN3154: Adopting SwiftUI navigation split view

**Framework**: Technotes

Use navigation split view to enable two and three column navigation in your SwiftUI app while maintaining compatibility with earlier OS versions.

#### Overview

[`NavigationSplitView`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/navigationsplitview) is a view that presents views in two or three columns, where selections in leading columns control presentations in subsequent columns. The Navigation split view API is available on iOS 16, macOS 13, tvOS 16, watchOS 9 and visionOS 1.

Transition from the deprecated [`NavigationView`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/navigationview) API if your app has a minimum deployment target of at least iOS 16, macOS 13, tvOS 16, watchOS 9 or visionOS 1. For more information, see [`Migrating to new navigation types`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/migrating-to-new-navigation-types).

This document describes how using a custom wrapper makes it easier to adopt `NavigationSplitView` and ensures your app remains compatible with the deprecated `NavigationView`, without increasing the app deployment target.

#### Using Api Availability Check to Provide Backward Compatibility Using a Custom Wrapper

Use the `#available()` keyword to execute code conditionally based on required platform and version. This allows your app use `NavigationSplitView` if the specified OS versions are iOS 16, macOS 13, tvOS 16, watchOS 9 or visionOS 1 while supporting `NavigationView` for earlier OS versions.

To ensure backward compatibility on earlier versions of iOS, macOS, tvOS and watchOS, create and use a custom wrapper view that conditionally uses either `NavigationSplitView` or `NavigationView` depending on the availability of the API. For apps that use one column navigation view, consider using [`NavigationStack`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/navigationstack).

```swift
struct NavigationSplitViewWrapper<Sidebar, Content, Detail>: View where Sidebar: View, Content: View, Detail: View {
    private var sidebar: Sidebar
    private var content: Content
    private var detail: Detail
    
    init(
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder content: () -> Content,
        @ViewBuilder detail:  () -> Detail
    ) {
        self.sidebar = sidebar()
        self.content = content()
        self.detail = detail()
    }
    
    var body: some View {
        if #available(iOS 16, macOS 13, tvOS 16, watchOS 9, visionOS 1, *) {
            // Use the latest API available
            NavigationSplitView {
                sidebar
            } content: {
                content
            } detail: {
                detail
            }
        } else {
            // Alternative code for earlier versions of OS.
            NavigationView {
                // The first column is the sidebar.
                sidebar
                
                // Initial content of the second column.
                content
                
                // Initial content for the third column.
                detail
            }
            .navigationViewStyle(.columns)
        }
    }
}
```

> **Note**: Navigation split view collapses all of its columns into a stack and shows the last column that displays useful information for [`compact size classes`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/layout), such as on iPhone or in iPad’s Slide Over mode. It also collapses all of its columns into a stack on Apple Watch and Apple TV, regardless of the size class.

#### Revision History

-  First published.

## See Also

- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3154-adopting-swiftui-navigation-split-view)*