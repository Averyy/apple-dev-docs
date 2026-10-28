# TN3210: Optimizing your app for iPhone Mirroring

**Framework**: Technotes  
**Role**: Technote

Test your app and improve compatibility with iPhone Mirroring.

## Overview

iPhone Mirroring lets people control their iPhone from a Mac using a trackpad or mouse. Most apps work without modification, because the system translates Mac input into the same indirect input events that iPad apps already receive from trackpads and mice. Standard UIKit and SwiftUI controls, system-provided sheets and popovers, scroll views, and built-in gesture recognizers continue to behave as people expect.

However, some app behaviors require additional consideration. If your app uses custom gesture recognizers, custom sheets or popovers, or is a game that handles pointer input, these features may not respond correctly to a trackpad or mouse. If your app gates functionality behind biometric authentication, those requests fail by default because Face ID and Touch ID on the iPhone aren’t accessible from the Mac. This guide will help you test for and resolve each of these behaviors.

## Test your app during iPhone Mirroring

Use iPhone Mirroring to validate your app’s behavior with a trackpad or mouse.

Look for these specific issues:

- **Indirect input:** Verify that pinch, rotate, and scroll gestures work with a trackpad and scroll gestures work with a mouse.
- **Sheet and popover dismissal:** Verify that custom sheets and popovers dismiss with a trackpad scroll. Sheets should also dismiss with scroll-wheel mice, as they support [`UIScrollType.discrete`](../UIKit/uiscrolltype/discrete.md).
- **Game input:** If your app is a game, verify that pointer input works correctly with a connected mouse or trackpad.
- **Biometric authentication:** Verify that biometric authentication works when iPhone Mirroring is active.

> **Note**: iPhone Mirroring requires a Mac running macOS Sequoia 15 or later and an iPhone running iOS 18 or later. To enable it, see [iPhone Mirroring: Use your iPhone from your Mac](https://support.apple.com/en-us/120421).

## Support indirect input

iPhone Mirroring delivers trackpad and mouse events to your app using the same event types as on iPad — `UIEvent.EventType.scroll` for scrolling, and `UIEvent.EventType.transform` for pinch and rotate.

- **Trackpad:** pinch and rotate ([`UIEvent.EventType.transform`](../UIKit/uievent/eventtype/transform.md)).
- **Trackpad:** scroll ([`UIEvent.EventType.scroll`](../UIKit/uievent/eventtype/scroll.md)). Produces `.continuous` scroll events.
- **Magic Mouse:** scroll ([`UIEvent.EventType.scroll`](../UIKit/uievent/eventtype/scroll.md)). Produces `.continuous` scroll events.
- **Scroll-wheel mouse:** scroll ([`UIEvent.EventType.scroll`](../UIKit/uievent/eventtype/scroll.md)). Produces `.discrete` scroll events.

### Check the indirect input opt-out key

The [`UIApplicationSupportsIndirectInputEvents`](../BundleResources/information-property-list/uiapplicationsupportsindirectinputevents.md) key is a compatibility affordance to ease the adoption of indirect input for a UIKit application. Add or update this key if your app meets either of the following conditions:

- `UIApplicationSupportsIndirectInputEvents` is set to `NO` in your `Info.plist`. Remove the key or change its value to `YES`.
- Your app targets iOS versions earlier than iOS 17 and the key is absent. Add the key with a value of `YES` to override the default value of `NO`.

```xml
<key>UIApplicationSupportsIndirectInputEvents</key>
<false/>
```

For a full list of the indirect input behaviors this key controls, see `UIApplicationSupportsIndirectInputEvents`.

### Add built-in recognizers for indirect input event support

Some indirect input events from trackpads and mice can only be recognized with subclasses of [`UIGestureRecognizer`](../UIKit/uigesturerecognizer.md):

- Use [`UIPinchGestureRecognizer`](../UIKit/uipinchgesturerecognizer.md) to handle `UIEvent.EventType.transform` from pinches on a trackpad.
- Use [`UIRotationGestureRecognizer`](../UIKit/uirotationgesturerecognizer.md) to handle `UIEvent.EventType.transform` from rotations on a trackpad.
- Use [`UIPanGestureRecognizer`](../UIKit/uipangesturerecognizer.md) and [`allowedScrollTypesMask`](../UIKit/uipangesturerecognizer/allowedscrolltypesmask.md) to handle `UIEvent.EventType.scroll` from mouse scroll wheels or trackpads. Set `allowedScrollTypesMask` to choose whether you respond to scroll-wheel mice (`.discrete`), trackpad and Magic Mouse (`.continuous`), or both.

If you have a custom `UIGestureRecognizer` subclass, you can keep it for direct touch and add a built-in recognizer alongside it for indirect input. For more information, watch [Handle trackpad and mouse input](https://developer.apple.com/videos/play/wwdc2020/10094).

### Verify that custom sheets and popovers dismiss correctly

When testing, verify that your sheets and popovers dismiss correctly with a trackpad scroll or a mouse scroll wheel. If they don’t, it’s likely because you’re using a custom implementation. Consider using sheets provided by the system, which respond to trackpad and mouse scrolls automatically. Replace your custom implementation with [`UISheetPresentationController`](../UIKit/uisheetpresentationcontroller.md) in UIKit or [`sheet(item:onDismiss:content:)`](../SwiftUI/view/sheet%28item,ondismiss,content%29.md) in SwiftUI.

If you can’t switch to the standard implementation, set `allowedScrollTypesMask` on your `UIPanGestureRecognizer` to `.continuous` for trackpad, or `.all` to also support a physical scroll wheel.

```swift
let panGestureRecognizer = UIPanGestureRecognizer(target: self, action: #selector(handlePan))
panGestureRecognizer.allowedScrollTypesMask = .continuous
```

If your app runs on iPad, the indirect input support you add for iPhone Mirroring also improves its trackpad and mouse experience on iPad. You can verify this by testing on an iPad paired with an external mouse or trackpad.

## Use the Game Controller framework to handle pointer input in your game

Games typically use responder-based event delivery rather than gesture recognizers. The pointer event types introduced for indirect input don’t support responder-based delivery. If you’re building a game, use the [Game Controller](../GameController/GameController.md) framework to handle pointing devices instead of adding gesture recognizers, and use [`GCMouse`](../GameController/gcmouse.md) for pointer support.

## Allow biometric authentication from a companion device

When someone uses your app through iPhone Mirroring, biometric authentication requests fail by default because Face ID and Touch ID sensors on iPhone aren’t accessible from the Mac.

The [`LAPolicy.deviceOwnerAuthenticationWithBiometrics`](../LocalAuthentication/lapolicy/deviceownerauthenticationwithbiometrics.md) policy only accepts biometric authentication on the iPhone itself, so it fails during iPhone Mirroring. Switch to [`LAPolicy.deviceOwnerAuthenticationWithBiometricsOrCompanion`](../LocalAuthentication/lapolicy/deviceownerauthenticationwithbiometricsorcompanion.md) so people can accept authentication on the Mac or a paired Apple Watch. For more information, see [`LAPolicy`](../LocalAuthentication/lapolicy.md).

```swift
let context = LAContext()
try await context.evaluatePolicy(
    .deviceOwnerAuthenticationWithBiometricsOrCompanion,
    localizedReason: reason
)
```

You can also use the Keychain API to enforce biometric authentication. Apply a [`SecAccessControl`](../Security/secaccesscontrol.md) object to your keychain item via [`kSecAttrAccessControl`](../Security/ksecattraccesscontrol.md), then set the [`biometryAny`](../Security/secaccesscontrolcreateflags/biometryany.md) and [`companion`](../Security/secaccesscontrolcreateflags/companion.md) flags in [`SecAccessControlCreateFlags`](../Security/secaccesscontrolcreateflags.md). For a complete walkthrough, see [Restricting keychain item accessibility](../Security/restricting-keychain-item-accessibility.md).

When people authenticate using a companion device, the Secure Enclave on iPhone communicates directly and securely with the Secure Enclave on the companion device. For more information, see [The Secure Enclave](https://support.apple.com/guide/security/the-secure-enclave-sec59b0b31ff/web).

## Support drag and drop

Support drag and drop so people can move data between iPhone and Mac while using your app through iPhone Mirroring. For design guidance, see [Drag and drop](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop) in the Human Interface Guidelines. For implementation details, see [Drag and drop](../UIKit/drag-and-drop.md).

## Revision History

- **2026-06-08** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3210-optimizing-your-app-for-iphone-mirroring)*