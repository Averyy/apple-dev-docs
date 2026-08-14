# LAAuthenticationView

**Framework**: Local Authentication Embedded UI  
**Kind**: class

A graphical representation of the state of biometric authentication.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class LAAuthenticationView
```

#### Overview

In the view that you use to manage authentication, add a local authentication view as a subview and provide it with an [`LAContext`](https://developer.apple.com/documentation/localauthentication/lacontext) instance. For example, you can do this in the [`loadView()`](https://developer.apple.com/documentation/appkit/nsviewcontroller/loadview()) method of your view controller:

```swift
func loadView() {
    laContext = LAContext()
    laView = LAAuthenticationView(context: laContext)

    view.addSubview(laView)
    laView.translatesAutoresizingMaskIntoConstraints = false

    // Add more subviews and layout constraints...
}
```

When the view appears, call the context’s [`evaluatePolicy(_:localizedReason:reply:)`](https://developer.apple.com/documentation/localauthentication/lacontext/evaluatepolicy(_:localizedreason:reply:)) method to initiate the authentication:

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

The local authentication view displays an icon that depends on the type of authentication you request, and the types of authentication that the system supports. For example, for a device that supports Touch ID, if you request the [`deviceOwnerAuthenticationWithBiometricsOrWatch`](https://developer.apple.com/documentation/localauthentication/lapolicy/deviceownerauthenticationwithbiometricsorwatch) policy, like in the example above, the view displays the familiar finger print icon:

![A screenshot of a circular icon with a pattern that resembles a finger print.](/images/com.apple.Local-Authentication-Embedded-UI/laauthenticationview-1@2x.png)

In the case above, if the user has a connected Apple Watch, that authentication mechanism works as well. If you limit the authentication to the [`deviceOwnerAuthenticationWithWatch`](https://developer.apple.com/documentation/localauthentication/lapolicy/deviceownerauthenticationwithwatch) policy, the icon shows an Apple Watch in profile:

![A screenshot of a circular icon containing the profile of an Apple Watch.](/images/com.apple.Local-Authentication-Embedded-UI/laauthenticationview-2@2x.png)

You can include other content around this icon that suits your app. The system also displays a message on the Touch Bar or on the user’s Apple Watch, if appropriate. When the evaluation succeeds, the icon transitions into a checkmark:

![A screenshot of a circular icon with a blue checkmark inside.](/images/com.apple.Local-Authentication-Embedded-UI/laauthenticationview-3@2x.png)

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
- [NSView](../appkit/nsview.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSDraggingDestination](../appkit/nsdraggingdestination.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthenticationembeddedui/laauthenticationview)*