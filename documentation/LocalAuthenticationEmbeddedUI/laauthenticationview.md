# LAAuthenticationView

**Framework**: Local Authentication Embedded UI  
**Kind**: class

A graphical representation of the state of biometric authentication.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
class LAAuthenticationView
```

#### Overview

In the view that you use to manage authentication, add a local authentication view as a subview and provide it with an [`LAContext`](https://developer.apple.com/documentation/LocalAuthentication/LAContext) instance. For example, you can do this in the doc://com.apple.documentation/documentation/appkit/nsviewcontroller/1434405-loadview method of your view controller:

```swift
func loadView() {
    laContext = LAContext()
    laView = LAAuthenticationView(context: laContext)

    view.addSubview(laView)
    laView.translatesAutoresizingMaskIntoConstraints = false

    // Add more subviews and layout constraints...
}
```

When the view appears, call the context’s [`evaluatePolicy(_:localizedReason:reply:)`](https://developer.apple.com/documentation/LocalAuthentication/LAContext/evaluatePolicy(_:localizedReason:reply:)) method to initiate the authentication:

```swift
override func viewDidAppear() {
    super.viewDidAppear()

    laContext.evaluatePolicy(
        .deviceOwnerAuthenticationWithBiometricsOrWatch,
        localizedReason: "access your data"
    ) { success, error in
        // Handle the result.
    }
}
```

The local authentication view displays an icon that depends on the type of authentication you request, and the types of authentication that the system supports. For example, for a device that supports Touch ID, if you request the [`LAPolicy.deviceOwnerAuthenticationWithBiometricsOrWatch`](https://developer.apple.com/documentation/LocalAuthentication/LAPolicy/deviceOwnerAuthenticationWithBiometricsOrWatch) policy, like in the example above, the view displays the familiar finger print icon:

![A screenshot of a circular icon with a pattern that resembles a finger print.](https://docs-assets.developer.apple.com/published/63abc31f750ffd3e74f794a1a8a9e37c/laauthenticationview-1%402x.png)

In the case above, if the user has a connected Apple Watch, that authentication mechanism works as well. If you limit the authentication to the [`LAPolicy.deviceOwnerAuthenticationWithWatch`](https://developer.apple.com/documentation/LocalAuthentication/LAPolicy/deviceOwnerAuthenticationWithWatch) policy, the icon shows an Apple Watch in profile:

![A screenshot of a circular icon containing the profile of an Apple Watch.](https://docs-assets.developer.apple.com/published/27733d7dd339bc1a9956c15a7d5f16b7/laauthenticationview-2%402x.png)

You can include other content around this icon that suits your app. The system also displays a message on the Touch Bar or on the user’s Apple Watch, if appropriate. When the evaluation succeeds, the icon transitions into a checkmark:

![A screenshot of a circular icon with a blue checkmark inside.](https://docs-assets.developer.apple.com/published/8172fa3530a97505e520e30b6d4e1845/laauthenticationview-3%402x.png)

If you call the evaluation without first attaching it to a local authentication view, the system shows a standard authentication alert instead.

## Topics

### Creating a local authentication view
- [init(context: LAContext)](laauthenticationview/init(context:).md)
  Creates a new authentication icon that reflects the current authentication state.
- [var context: LAContext](laauthenticationview/context.md)
  The local authentication context associated with the authentication view.
### Controlling the size of a local authentication view
- [init(context: LAContext, controlSize: NSControl.ControlSize)](laauthenticationview/init(context:controlsize:).md)
  Creates a new authentication icon that reflects the current authentication state, using a specified size.
- [var controlSize: NSControl.ControlSize](laauthenticationview/controlsize.md)
  The size of the local authentication view user interface element.

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthenticationembeddedui/laauthenticationview)*