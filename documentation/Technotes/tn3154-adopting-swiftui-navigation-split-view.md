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

- **2023-08-29** First published.

## See Also

- [TN3213: Moving from Multipeer Connectivity to Network framework](tn3213-moving-from-multipeer-connectivity-to-network-framework.md)
  Learn how to migrate your Multipeer Connectivity app to Network framework.
- [TN3210: Optimizing your app for iPhone Mirroring](tn3210-optimizing-your-app-for-iphone-mirroring.md)
  Test your app and improve compatibility with iPhone Mirroring.
- [TN3211: Resolving SwiftUI source incompatibilities for State and ContentBuilder](tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder.md)
  Update existing code for two foundational changes in SwiftUI built with Xcode 27.
- [TN3212: Adopting gesture recognizers for Sidecar touch support](tn3212-adopting-gesture-recognizers-for-sidecar-touch-support.md)
  Use gesture recognizers to handle Sidecar touch input and update your event-handling code for macOS 27.
- [TN3208: Preparing your app’s launch screen to meet App Store requirements](tn3208-preparing-your-apps-launch-screen-to-meet-app-store-requirements.md)
  Understand the launch screen requirement for App Store submission starting in iOS 27 and iPadOS 27.
- [TN3205: Low-latency communication with RDMA over Thunderbolt](tn3205-low-latency-communication-with-rdma-over-thunderbolt.md)
  Learn how to use RDMA over Thunderbolt to enable low-latency communication between clusters of Mac computers.
- [TN3206: Updating Apple Pay certificates](tn3206-updating-apple-pay-certificates.md)
  Learn how to create, manage, and rotate Apple Pay certificates to maintain uninterrupted payment processing.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3154-adopting-swiftui-navigation-split-view)*