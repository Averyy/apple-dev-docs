# TN3210: Optimizing your app for iPhone Mirroring

**Framework**: Technotes

Test your app and improve compatibility with iPhone Mirroring.

#### Overview

iPhone Mirroring lets people control their iPhone from a Mac using a trackpad or mouse. Most apps work without modification, because the system translates Mac input into the same indirect input events that iPad apps already receive from trackpads and mice. Standard UIKit and SwiftUI controls, system-provided sheets and popovers, scroll views, and built-in gesture recognizers continue to behave as people expect.

However, some app behaviors require additional consideration. If your app uses custom gesture recognizers, custom sheets or popovers, or is a game that handles pointer input, these features may not respond correctly to a trackpad or mouse. If your app gates functionality behind biometric authentication, those requests fail by default because Face ID and Touch ID on the iPhone aren’t accessible from the Mac. This guide will help you test for and resolve each of these behaviors.

#### Test Your App During Iphone Mirroring

Use iPhone Mirroring to validate your app’s behavior with a trackpad or mouse.

Look for these specific issues:

- **Indirect input:** Verify that pinch, rotate, and scroll gestures work with a trackpad and scroll gestures work with a mouse.
- **Sheet and popover dismissal:** Verify that custom sheets and popovers dismiss with a trackpad scroll. Sheets should also dismiss with scroll-wheel mice, as they support [`UIScrollType.discrete`](https://developer.apple.com/documentation/UIKit/UIScrollType/discrete).
- **Game input:** If your app is a game, verify that pointer input works correctly with a connected mouse or trackpad.
- **Biometric authentication:** Verify that biometric authentication works when iPhone Mirroring is active.

> **Note**: iPhone Mirroring requires a Mac running macOS Sequoia 15 or later and an iPhone running iOS 18 or later. To enable it, see [`iPhone Mirroring: Use your iPhone from your Mac`](https://developer.apple.comhttps://support.apple.com/en-us/120421).

#### Support Indirect Input

iPhone Mirroring delivers trackpad and mouse events to your app using the same event types as on iPad — `UIEvent.EventType.scroll` for scrolling, and `UIEvent.EventType.transform` for pinch and rotate.

- **Trackpad:** pinch and rotate ([`UIEvent.EventType.transform`](https://developer.apple.com/documentation/UIKit/UIEvent/EventType/transform)).
- **Trackpad:** scroll ([`UIEvent.EventType.scroll`](https://developer.apple.com/documentation/UIKit/UIEvent/EventType/scroll)). Produces `.continuous` scroll events.
- **Magic Mouse:** scroll ([`UIEvent.EventType.scroll`](https://developer.apple.com/documentation/UIKit/UIEvent/EventType/scroll)). Produces `.continuous` scroll events.
- **Scroll-wheel mouse:** scroll ([`UIEvent.EventType.scroll`](https://developer.apple.com/documentation/UIKit/UIEvent/EventType/scroll)). Produces `.discrete` scroll events.

##### Check the Indirect Input Opt Out Key

The [`UIApplicationSupportsIndirectInputEvents`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSupportsIndirectInputEvents) key is a compatibility affordance to ease the adoption of indirect input for a UIKit application. Add or update this key if your app meets either of the following conditions:

- `UIApplicationSupportsIndirectInputEvents` is set to `NO` in your `Info.plist`. Remove the key or change its value to `YES`.
- Your app targets iOS versions earlier than iOS 17 and the key is absent. Add the key with a value of `YES` to override the default value of `NO`.

```xml
<key>UIApplicationSupportsIndirectInputEvents</key>
<false/>
```

For a full list of the indirect input behaviors this key controls, see `UIApplicationSupportsIndirectInputEvents`.

##### Add Built in Recognizers for Indirect Input Event Support

Some indirect input events from trackpads and mice can only be recognized with subclasses of [`UIGestureRecognizer`](https://developer.apple.com/documentation/UIKit/UIGestureRecognizer):

- Use [`UIPinchGestureRecognizer`](https://developer.apple.com/documentation/UIKit/UIPinchGestureRecognizer) to handle `UIEvent.EventType.transform` from pinches on a trackpad.
- Use [`UIRotationGestureRecognizer`](https://developer.apple.com/documentation/UIKit/UIRotationGestureRecognizer) to handle `UIEvent.EventType.transform` from rotations on a trackpad.
- Use [`UIPanGestureRecognizer`](https://developer.apple.com/documentation/UIKit/UIPanGestureRecognizer) and [`allowedScrollTypesMask`](https://developer.apple.com/documentation/UIKit/UIPanGestureRecognizer/allowedScrollTypesMask) to handle `UIEvent.EventType.scroll` from mouse scroll wheels or trackpads. Set `allowedScrollTypesMask` to choose whether you respond to scroll-wheel mice (`.discrete`), trackpad and Magic Mouse (`.continuous`), or both.

If you have a custom `UIGestureRecognizer` subclass, you can keep it for direct touch and add a built-in recognizer alongside it for indirect input. For more information, watch [`Handle trackpad and mouse input`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10094).

##### Verify That Custom Sheets and Popovers Dismiss Correctly

When testing, verify that your sheets and popovers dismiss correctly with a trackpad scroll or a mouse scroll wheel. If they don’t, it’s likely because you’re using a custom implementation. Consider using sheets provided by the system, which respond to trackpad and mouse scrolls automatically. Replace your custom implementation with [`UISheetPresentationController`](https://developer.apple.com/documentation/UIKit/UISheetPresentationController) in UIKit or [`sheet(item:onDismiss:content:)`](https://developer.apple.com/documentation/SwiftUI/View/sheet(item:onDismiss:content:)) in SwiftUI.

If you can’t switch to the standard implementation, set `allowedScrollTypesMask` on your `UIPanGestureRecognizer` to `.continuous` for trackpad, or `.all` to also support a physical scroll wheel.

```swift
let panGestureRecognizer = UIPanGestureRecognizer(target: self, action: #selector(handlePan))
panGestureRecognizer.allowedScrollTypesMask = .continuous
```

If your app runs on iPad, the indirect input support you add for iPhone Mirroring also improves its trackpad and mouse experience on iPad. You can verify this by testing on an iPad paired with an external mouse or trackpad.

#### Use the Game Controller Framework to Handle Pointer Input in Your Game

Games typically use responder-based event delivery rather than gesture recognizers. The pointer event types introduced for indirect input don’t support responder-based delivery. If you’re building a game, use the [`Game Controller`](https://developer.apple.com/documentation/GameController) framework to handle pointing devices instead of adding gesture recognizers, and use [`GCMouse`](https://developer.apple.com/documentation/GameController/GCMouse) for pointer support.

#### Allow Biometric Authentication From a Companion Device

When someone uses your app through iPhone Mirroring, biometric authentication requests fail by default because Face ID and Touch ID sensors on iPhone aren’t accessible from the Mac.

The [`LAPolicy.deviceOwnerAuthenticationWithBiometrics`](https://developer.apple.com/documentation/LocalAuthentication/LAPolicy/deviceOwnerAuthenticationWithBiometrics) policy only accepts biometric authentication on the iPhone itself, so it fails during iPhone Mirroring. Switch to [`LAPolicy.deviceOwnerAuthenticationWithBiometricsOrCompanion`](https://developer.apple.com/documentation/LocalAuthentication/LAPolicy/deviceOwnerAuthenticationWithBiometricsOrCompanion) so people can accept authentication on the Mac or a paired Apple Watch. For more information, see [`LAPolicy`](https://developer.apple.com/documentation/LocalAuthentication/LAPolicy).

```swift
let context = LAContext()
try await context.evaluatePolicy(
    .deviceOwnerAuthenticationWithBiometricsOrCompanion,
    localizedReason: reason
)
```

You can also use the Keychain API to enforce biometric authentication. Apply a [`SecAccessControl`](https://developer.apple.com/documentation/Security/SecAccessControl) object to your keychain item via [`kSecAttrAccessControl`](https://developer.apple.com/documentation/Security/kSecAttrAccessControl), then set the [`biometryAny`](https://developer.apple.com/documentation/Security/SecAccessControlCreateFlags/biometryAny) and [`companion`](https://developer.apple.com/documentation/Security/SecAccessControlCreateFlags/companion) flags in [`SecAccessControlCreateFlags`](https://developer.apple.com/documentation/Security/SecAccessControlCreateFlags). For a complete walkthrough, see [`Restricting keychain item accessibility`](https://developer.apple.com/documentation/Security/restricting-keychain-item-accessibility).

When people authenticate using a companion device, the Secure Enclave on iPhone communicates directly and securely with the Secure Enclave on the companion device. For more information, see [`The Secure Enclave`](https://developer.apple.comhttps://support.apple.com/guide/security/the-secure-enclave-sec59b0b31ff/web).

#### Support Drag and Drop

Support drag and drop so people can move data between iPhone and Mac while using your app through iPhone Mirroring. For design guidance, see [`Drag and drop`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/drag-and-drop) in the Human Interface Guidelines. For implementation details, see [`Drag and drop`](https://developer.apple.com/documentation/UIKit/drag-and-drop).

#### Revision History

- **2026-06-08** First published.

## See Also

- [TN3213: Moving from Multipeer Connectivity to Network framework](tn3213-moving-from-multipeer-connectivity-to-network-framework.md)
  Learn how to migrate your Multipeer Connectivity app to Network framework.
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
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3210-optimizing-your-app-for-iphone-mirroring)*