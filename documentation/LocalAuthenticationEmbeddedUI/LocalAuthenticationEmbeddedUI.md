# Local Authentication Embedded UI

**Framework**: Local Authentication Embedded UI  
**Kind**: module

Present a standard local authentication view icon in a custom authentication view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

#### Overview

When you authenticate users with the `Local Authentication` framework, the framework handles all user interaction by default. If you want to create a custom authentication user interface, build it around an [`LAAuthenticationView`](laauthenticationview.md) instance. The authentication view displays an icon that users associate with biometric authentication, like the Touch ID icon, and then modifies that icon over time to reflect changes in the authentication state. You can add other text, images, or interactive elements to your custom view as needed.

![A screenshot of a view with the title Access My Transactions above a circular finger print icon, which is in turn above a secure text entry field. The finger print icon is highlighted.](https://docs-assets.developer.apple.com/published/3f09f35196c3578fefba573ce80eb4d3/localauthenticationembeddedui-1%402x.png)

For all local authentication operations, the system manages the underlying biometric data, but with a local authentication view, you can customize the authentication interface to match the design of your app. At the same time, familiar iconography helps users understand what you are asking from them.

## Topics

### The Local Authentication View
- [class LAAuthenticationView](laauthenticationview.md)
  A graphical representation of the state of biometric authentication.
### Reference
- [Local Authentication Embedded UI Data Types](local-authentication-embedded-ui-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/LocalAuthenticationEmbeddedUI)*