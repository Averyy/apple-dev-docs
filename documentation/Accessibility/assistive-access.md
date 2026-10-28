# Assistive Access

**Framework**: Accessibility  
**Role**: Assistive Technology

A mode that tailors the iOS and iPadOS experience for people with cognitive disabilities.

## Overview

Assistive Access is an accessibility feature that offers a distinctive interface with high-contrast buttons, large text labels, and visual alternatives to text for people with cognitive disabilities. A trusted supporter, such as a family member or caregiver, sets up this feature in Settings > Accessibility > Assistive Access. They choose the system and third-party apps to make available in Assistive Access.

![](https://developer.apple.com/tutorials/images/com.apple.Accessibility/assistive-access@2x.png)

#### Learn to use Assistive Access

- [Assistive Access User Guide](https://support.apple.com/guide/assistive-access-iphone/welcome/ios)

#### Related videos

- [Customize your app for Assistive Access](https://developer.apple.com/videos/play/wwdc2025/238)
  Assistive Access is a distinctive, focused iOS experience that makes it easier for people with cognitive disabilities to use iPhone and iPad independently. In iOS and iPadOS 26, you can customize your app when it’s running in Assistive Access to give people greater ease and independence. Learn how to tailor your app using the AssistiveAccess SwiftUI scene type, and explore the key design principles that can help you create a high-quality Assistive Access experience for everyone.
- [Meet Assistive Access](https://developer.apple.com/videos/play/wwdc2023/10032)
  Learn how Assistive Access can help people with cognitive disabilities more easily use iPhone and iPad. Discover the design principles that guide Assistive Access and find out how the system experience adapts to lighten cognitive load. We’ll show you how Assistive Access works and what you can do to support this experience in your app.

## Topics

### Develop for Assistive Access
- [Optimizing your app for Assistive Access](./optimizing-your-app-for-assistive-access.md)
  Adjust your app’s UI to make sure it works well for people who use Assistive Access.
- [Performing accessibility testing for your app](./performing-accessibility-testing-for-your-app.md)
  Test your app with accessibility settings and assistive technologies to discover and address accessibility issues.
- [static var isAssistiveAccessEnabled: Bool](./accessibilitysettings/isassistiveaccessenabled.md)
  A Boolean value that indicates whether Assistive Access is running.
- [var accessibilityAssistiveAccessEnabled: Bool](../SwiftUI/environmentvalues/accessibilityassistiveaccessenabled.md)
  A Boolean value that indicates whether Assistive Access is in use.
- [UISupportsFullScreenInAssistiveAccess](../BundleResources/information-property-list/uisupportsfullscreeninassistiveaccess.md)
  A Boolean value that indicates if an iOS or iPadOS app appears as full screen in Assistive Access.

## See Also

### Assistive technologies
- [VoiceOver](./voiceover.md)
  A gesture-based screen reader that provides an auditory description of the content onscreen.
- [Voice Control](./voice-control.md)
  An interface for navigating a device using voice commands to tap, swipe, type, and more.
- [Switch Control](./switch-control.md)
  An interface for navigating a device with a variety of adaptive switch hardware, wireless game controllers, or sounds such as a click or a pop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/assistive-access)*